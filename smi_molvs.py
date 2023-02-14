# coding:utf-8
from __future__ import print_function
import os,sys,glob
import pandas as pd
import argparse
from molvs import standardize_smiles
#>>> standardize_smiles('C[n+]1c([N-](C))cccc1')
#'CN=c1ccccn1C'
base=os.getcwd()

def standardize_smiles_file(a_file,s_col): 
	if a_file.endswith('.xlsx'):
		df = pd.read_excel(a_file,engine='openpyxl')
		## pip install xlrd==1.2.0
	if a_file.endswith('.csv'): 
		df = pd.read_csv(a_file)
	smiles_col = df.columns[int(s_col)] if s_col.isdigit() else s_col
	#smiles_list= df[smiles_col]
	df['standardize_smiles'] = df[smiles_col].apply(standardize_smiles)
	new_file = a_file.split('.')[0] + "_std.csv"
	df.to_csv(new_file,sep=',', index=False);return

os.chdir(base)
parser = argparse.ArgumentParser(description='require column name "smiles"')
	  
parser.add_argument( '-f','--files', nargs='*',default=[],help="input csv|txt|xlsx|can")
parser.add_argument('-s',dest='smiles_col', type=str, default='smiles', help="default smiles ") 

args = parser.parse_args()
files = args.files;smiles_col = args.smiles_col

if len(files) == 0: raise IOError('no input files')	
print('files = ', files)
for a_file in files: 
	standardize_smiles_file(a_file,smiles_col)

