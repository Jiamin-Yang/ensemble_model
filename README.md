# Predicting GPR40 Agonists with A Deep Learning-Based Ensemble Model
This repository describes the calculation steps and optimization process of an ensemble model, as well as various results and related intermediate files.  
For all the script and all meta files, please visit and download it from zenodo (DOI 10.5281/zenodo.7641975).

<a href="url"><img src="./docs/image1.png" align="center" height="350" width="270" ></a>

Table of Contents:

1. Ensemble model architecture
2. Calculation and analysis of the model
3. Optimization of the Ensemble Model
4. Introduce of different folders and files

## Ensemble model architecture
<a href="url"><img src="./docs/image2.png" align="center" height="700" width="830" ></a>

## Calculation and analysis of the model
note: We used chemprop to partition the main dataset and then performed training and evaluation of the model. We also utilized an external dataset for additional evaluation of the model's performance.

### Script: **1_baseline_models_chemprop1.4.0.ipynb**  
(We constructed baseline models and obtained predictive scores for compounds in the main dataset.)

### Script: **2_baselines_load_pred_ext_sim.ipynb**  
(We loaded the models and used them to predict the probabilities of compounds in various external datasets.)

### Script: **3_anal_baseline_models.ipynb**  
(We analyzed the results of the baseline model, including metrics such as ROC AUC, and averaged the model's performance values over five iterations.)

### Script: **3b_anal_group_mdels_all_metric.ipynb**  
(We calculated the performance values of the baseline models for all metrics and averaged them over five iterations.)

## Optimization of the Ensemble Model

### Script: **4_ensemble.ipynb**  
(We constructed an ensemble model and optimized its performance.)

### Script: **5_anal_ensemble.ipynb**  
(We evaluated the ensmeble in all metrics and averaged the performance values over five iteration)

### Script: **6_check_compare_chiral_FP.ipynb**  
(We explored the impact of chiral fingerprints on the models)

### Script: **7_search_fcnn_param.ipynb**  
(We examined the effect of various parameters in the FCNN on the ensemble model.)

## Introduce of different folders and files

folders：

1. **rand_{fearue}** ：the split main set (including compound SMILES, feature, label)  
(feature= , AtomPairFP, Autocorr, AvalonFP, Charge, Connectivity, Constitution, Estate, EstateFP, Fragment, InfoContent, Kappa, MACCSFP, MAP4, Matrix, MHFP6, MOE, MorganFP, Path, PharmacoErGFP, PharmacoPFP, Property, PubChemFP, RDkitFP, Topology, TorsionFP)  
The full files is available on Zenodo (DOI 10.5281/zenodo.7641975).

2. **xgb, svm, log, DMPNN, rf and fcnn**  
(The predictive probabilities of the various baseline models)  
These folders are at Zenodo.

3. **esb, esb_01, voting**  
(We present the evaluation results of various ensemble models with changes made to the number of nodes in the FCNN (esb/**esb.csv**) and the number of baseline models (esb/**esb_topN.csv**), binary options in layer 2 (esb_01/**esb_topN.csv**), and the use of stacking or voting (voting/**vot_topN.csv**). We also assessed the performance of these models with different external datasets (esb/**esb_rmSim.csv**).)  

4. **fp** (Molecular representations for compounds in the main and external datasets)  
 **fp2** (Molecular representations for compounds in various external datasets)  
Both folders are at Zenodo.

5. **grouped_esb_metric** (Performance values of ensemble model for different metrics)  
**grouped_metric** (Performance values of baseline models for different metrics)

6. **fcnn_AtomPairFP_search_param1, fcnn_AtomPairFP_search_param2_2layer** (parameter optimization of FCNN)

7. **dataset** (original dataset: ChEMBL dataset, BindingDB dataset and manually collected dataset)

files：

1. **Ext.csv, Ext_rm_sim_0_7.csv, Ext_rm_sim_0_8.csv, Ext_rm_sim_0_7.csv** (External datasets with varying numbers of compounds)  
**Main.csv** (SMILES and labels for the main set compound)

2. **eva_Morgan_chiral.csv**  
(Performance of various ensemble models with chiral fingerprints)

3. **eva_with_rmSim_hyper.csv, eva_with_rmSim_hyper_2layer.csv**  
(Performance of ensemble models with varying FCNN parameters)

4. **eva_with_rmSim.csv** (Evaluation of baseline models using various external datasets)  
**eva_ensemble_with_rmSim.csv** (Evaluation of ensemble models using various external datasets)
