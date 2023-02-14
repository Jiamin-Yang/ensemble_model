# Predicting GPR40 Agonists with A Deep Learning-Based Ensemble Model
this repository describes the calculation steps and optimization process of an ensemble model, as well as various results and related intermediate files.

<a href="url"><img src="./docs/molmap.log.png" align="center" height="350" width="270" ></a>

Table of Contents:

1. Ensemble model architecture
2. Calculation and analysis of the model
3. Optimization of the Ensemble Model

## Ensemble model architecture
png

## Calculation and analysis of the model
note: We used chemprop to partition the main dataset and then performed training and evaluation of the model. We also utilized an external dataset for additional evaluation of the model's performance.

### Script: **1_baseline_models_chemprop1.4.0.ipynb** (build baseline models and get predictive score of compounds in main set)

### **2_baselines_load_pred_ext_sim.ipynb** (load models and predict the probability of compounds in different external datasets)

### **3_anal_baseline_models.ipynb** (analysis the results of baseline model such as ROC AUC, and average the performance values of the model over five calculations)

### **3b_anal_group_mdels_all_metric.ipynb** (caculate the performance values in all metric)

## Optimization of the Ensemble Model

### **4_ensemble.ipynb** (build ensemble model and optimize the ensmeble model)

### **5_anal_ensemble.ipynb** (evaluate the ensmeble)

### **6_check_compare_chiral_FP.ipynb** (explore the impact of chiral fingerprints on the models)

### **7_search_fcnn_param.ipynb** (explore the impact of different parameters in FCNN on the ensemble model)











