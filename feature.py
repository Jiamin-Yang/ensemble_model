import os,sys,time,glob

sys.path.append('/home/phzd/AI/bidd-molmap_v1_3')
from molmap.feature import descriptor
from molmap.feature import fingerprint
from molmap import feature
import pandas as pd
import numpy as np
import argparse
import csv
##==========
fingerprint_list = ['MorganFP', 'RDkitFP', 'AtomPairFP', 'TorsionFP', 'AvalonFP', 
'EstateFP', 'MACCSFP', 'PharmacoErGFP', 'PharmacoPFP', 'PubChemFP', 'MHFP6', 'MAP4']
descriptor_list = ['Property', 'Constitution', 'Autocorr', 'Fragment', 'Charge', 
'Estate', 'MOE', 'Connectivity', 'Topology', 'Kappa', 'Path', 'Matrix', 'InfoContent']
bool_dtype_list = ['MorganFP','RDkitFP','AtomPairFP','TorsionFP','AvalonFP','EstateFP',
'MACCSFP','PharmacoErGFP','PharmacoPFP','PubChemFP','MHFP6','MAP4']
int_dtype_list = ['Constitution','Fragment','Estate','Path',]
float_dtype_list =['Property','Autocorr','Charge','MOE','Connectivity','Topology',
'Kappa','Matrix','InfoContent']

"""
fingerprint.Extraction().factory
{'MorganFP': <function molmap.feature.fingerprint.morganfp.GetMorganFPs(mol, nBits=2048, radius=2, return_bitInfo=False)>,
 'RDkitFP': <function molmap.feature.fingerprint.rdkitfp.GetRDkitFPs(mol, nBits=2048, return_bitInfo=False)>,
 'AtomPairFP': <function molmap.feature.fingerprint.atompairs.GetAtomPairFPs(mol, nBits=2048, binary=True)>,
 'TorsionFP': <function molmap.feature.fingerprint.torsions.GetTorsionFPs(mol, nBits=2048, binary=True)>,
 'AvalonFP': <function molmap.feature.fingerprint.avalonfp.GetAvalonFPs(mol, nBits=2048)>,
 'EstateFP': <function molmap.feature.fingerprint.estatefp.GetEstateFPs(mol)>,
 'MACCSFP': <function molmap.feature.fingerprint.maccskeys.GetMACCSFPs(mol)>,
 'PharmacoErGFP': <function molmap.feature.fingerprint.pharmErGfp.GetPharmacoErGFPs(mol, fuzzIncrement=0.3, maxPath=21, binary=True, return_bitInfo=False)>,
 'PharmacoPFP': <function molmap.feature.fingerprint.pharmPointfp.GetPharmacoPFPs(mol, bins=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20)], minPointCount=2, maxPointCount=2, return_bitInfo=False)>,
 'PubChemFP': <function molmap.feature.fingerprint.pubchemfp.GetPubChemFPs(mol)>,
 'MHFP6': <function molmap.feature.fingerprint.mhfp6.GetMHFP6(mol, nBits=2048, radius=3)>,
 'MAP4': <function molmap.feature.fingerprint.map4.GetMAP4(mol, nBits=2048, radius=2, fold_dimensions=None)>}

descriptor.Extraction().factory
{'Property': <function molmap.feature.descriptor.property.GetProperty(mol)>,
 'Constitution': <function molmap.feature.descriptor.constitution.GetConstitution(mol)>,
 'Autocorr': <function molmap.feature.descriptor.autocorr.GetAutocorr(mol)>,
 'Fragment': <function molmap.feature.descriptor.fragment.GetFragment(mol)>,
 'Charge': <function molmap.feature.descriptor.charge.GetCharge(mol)>,
 'Estate': <function molmap.feature.descriptor.estate.GetEstate(mol)>,
 'MOE': <function molmap.feature.descriptor.moe.GetMOE(mol)>,
 'Connectivity': <function molmap.feature.descriptor.connectivity.GetConnectivity(mol)>,
 'Topology': <function molmap.feature.descriptor.topology.GetTopology(mol)>,
 'Kappa': <function molmap.feature.descriptor.kappa.GetKappa(mol)>,
 'Path': <function molmap.feature.descriptor.path.GetPath(mol)>,
 'Matrix': <function molmap.feature.descriptor.matrix.GetMatrix(mol)>,
 'InfoContent': <function molmap.feature.descriptor.infocontent.GetInfoContent(mol)>}

fingerprint.Extraction().factory.keys()
dict_keys(['MorganFP', 'RDkitFP', 'AtomPairFP', 'TorsionFP', 'AvalonFP', 'EstateFP', 'MACCSFP', 'PharmacoErGFP', 'PharmacoPFP', 'PubChemFP', 'MHFP6', 'MAP4'])

descriptor.Extraction().factory.keys()
dict_keys(['MorganFP', 'RDkitFP', 'AtomPairFP', 'TorsionFP', 'AvalonFP', 'EstateFP', 'MACCSFP', 'PharmacoErGFP', 'PharmacoPFP', 'PubChemFP', 'MHFP6', 'MAP4'])
"""

astype_dic = {'int':'int','bool':'int','float':np.float16}

fp_feat_dir = './fp'
if not os.path.exists(fp_feat_dir):os.mkdir(fp_feat_dir)

base=os.getcwd()

def gen_one_type_fp(csv_file,s_col,fp,threads):
	csv_base = csv_file.split('.')[0]
	save_name = f'{fp_feat_dir}/{csv_base}_{fp}.csv'  
	df=pd.read_csv(csv_file)
	smiles_col = df.columns[int(s_col)] if s_col.isdigit() else s_col
	smiles_list= df[smiles_col]
	x_dict = {fp:{}}
	if fp in fingerprint_list:
		extractor=fingerprint.Extraction(feature_dict=x_dict)
		bitsinfo = fingerprint.Extraction().bitsinfo
		##['PubChemFP0','PubChemFP1',…]				
	elif fp in descriptor_list:
		extractor=descriptor.Extraction(feature_dict=x_dict)
		bitsinfo = descriptor.Extraction().bitsinfo
	else: raise IOError('not supp fp: {}'.format(fp))
	res=extractor.batch_transform(smiles_list=smiles_list, n_jobs = threads)
	flist = bitsinfo[bitsinfo.Subtypes.isin([fp])].IDs.tolist()	

	if fp in bool_dtype_list:dtype = 'int'
	elif fp in int_dtype_list:dtype = 'int'
	elif fp in float_dtype_list:dtype = 'float'
	else: raise IOError('not supp fp')

	x_astype = astype_dic[dtype]
	print('before res =',res)
	res=np.array(res).astype(x_astype)    #('int')

	save_name = f'{fp_feat_dir}/{csv_base}_{fp}.csv'
	w_res = res.tolist();
	w_res.insert(0,flist)
	with open(save_name,'w',newline='') as f:
	    writer = csv.writer(f)   
	    writer.writerows(w_res)	
	print(f'done {save_name}')
	return save_name

def main():
	os.chdir(base)
	parser = argparse.ArgumentParser(description='better to gen bool int float fp in sep fold')	
	  
	parser.add_argument('-f',dest='csv_file', type=str, help="supp only csv") 
	parser.add_argument('-s',dest='smiles_col', type=str, default='smiles', help="default smiles ") 
	parser.add_argument('-fps', nargs='*',default=[],
		help="choice of fps bool int float or empty(default, gen all") 
	parser.add_argument('-t',dest='threads', type=int,default=20,help="multitheads to accelerate calc, default 20")
	parser.add_argument('-a',dest='action', type=str, default='gen', 
		help="choice gen(gen feat), show_fp_dict, show_fp_list, show_bool_list, show_int_list,show_float_list") 

	args = parser.parse_args()
	csv_file = args.csv_file;	smiles_col = args.smiles_col
	r_fps = args.fps;action = args.action;threads=args.threads

	if action=='show_fp_dict':
		print(descriptor.Extraction().factory);print(fingerprint.Extraction().factory);return
	if action=='show_fp_list':
		print('fingerprint_list=',' '.join(fingerprint_list))
		print('descriptor_list=',' '.join(descriptor_list))
		return
	if action=='show_bool_list':
		print('fingerprint_list=',' '.join(bool_dtype_list));return
	if action=='show_int_list':
		print('show_int_list=',' '.join(int_dtype_list));return
	if action=='show_float_list':
		print('show_float_list=',' '.join(float_dtype_list));return	
	fps=[]
	if len(r_fps)==0: fps=fingerprint_list+descriptor_list
	if 'bool' in r_fps: fps.extend(bool_dtype_list)	
	if 'int' in r_fps: fps.extend(int_dtype_list)
	if 'float' in r_fps: fps.extend(float_dtype_list)
	for fp in r_fps:
		if fp not in ['bool','int','float']:
			if fp not in fps:
				fps.append(fp)
	print('fps = ', fps)
	#gen_fps(csv_file,smiles_col,fps)
	for fp in fps:
		print('fp = ',fp)
		feat_file = gen_one_type_fp(csv_file,smiles_col,fp,threads)
		print('done feat_file: {}'.format(feat_file))
	print('all done; the desc fp file might need to be further standardised')

if __name__=='__main__':
	main()




