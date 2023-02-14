#!/bin/bash
#SBATCH --job-name=chemp         # create a short name for your job
#SBATCH --ntasks=1              # total number of tasks across all nodes
#SBATCH --gres=gpu:1
#SBATCH --mem=8G
export PATH=/home/phzd/test/amber20/miniconda/bin:$PATH;source activate chemprop1.40;export PATH=/usr/local/cuda-11.4/bin:$PATH;export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64:$LD_LIBRARY_PATH
srun chemprop_predict --test_path Ext_rm_sim_0_9.csv --checkpoint_path rand_Topology/fold_4/model_0/model.pt --preds_path DMPNN/p_Ext_rm_sim_0_9_Topology_fold4.csv --features_path ./fp2/Ext_rm_sim_0_9_Topology.csv