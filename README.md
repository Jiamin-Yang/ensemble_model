# Predicting GPR40 Agonists with A Deep Learning-Based Ensemble Model
this repository describes the calculation steps and optimization process of an ensemble model, as well as various results and related intermediate files.

<a href="url"><img src="./docs/molmap.log.png" align="left" height="350" width="270" ></a>

Table of Contents:

1. Ensemble model architecture
2. Calculation and analysis of the model
3. Optimization of the Ensemble Model

## Ensemble model architecture
png

## Calculation and analysis of the model
note: We used chemprop to partition the main dataset and then performed training and evaluation of the model. We also utilized an external dataset for additional evaluation of the model's performance.
output files: 		



### Script: 1_baseline_models_chemprop1.4.0.ipynb (build baseline models and get predictive score)
input files: rand_MorganFP (split_indices_fold{i}.pckl, i=fold number);fp folder (molecular representation of main set and external dataset); Ext.csv
output files: {algorithm} (**p_{data}_{feature}_fold{i}.csv**. data=train, val, test and Ext. feature= AtomPairFP, MOE.... i=0,1, 2, 3, 4(fold number). algorithm=xgb,fcnn,rf,svm,logreg)
