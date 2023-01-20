#!/bin/bash -l
#SBATCH --job-name=scvi_GPU                                                                      # Job name
##SBATCH --ntasks=10
#SBATCH --nodelist=node7
##SBATCH --mem=100G
#SBATCH --output=/home/lugli/spuccio/Projects/Tmp/jupyternotebook%j.log # whatever needed
##SBATCH --cpus-per-task=40
##SBATCH -n 15
##SBATCH --ntasks=16
##SBATCH --nodes=1
##SBATCH --mem-per-cpu=MaxMemPerCPU
# Request one node:
#SBATCH --nodes=1
#
# Specify one task:
#SBATCH --ntasks-per-node=1
#
# Number of processors for single task needed for use case (example):
#SBATCH --cpus-per-task=4


##SBATCH --mail-type=END,FAIL                                    # Mail events (NONE, BEGIN, END, FAIL, ALL)
##SBATCH --mail-user=simone.puccio@humanitasresearch.it       # Where to send mail
##SBATCH --ntasks=5
##SBATCH --nodelist=node7                                                             # Run on a N CPU
##SBATCH --mem=40gb                                                   # Job memory request
##SBATCH --time=24:00:00                                              # Time limit hrs:min:sec
#SBATCH --output=scvi%j.log                                  # Standard output and error logpwd; hostname; date
##SBATCH --gres=gpu:1

source /home/lugli/spuccio/anaconda3/etc/profile.d/conda.sh 
source /home/lugli/spuccio/anaconda3/bin/activate scanpy19
#conda activate scvi


python /home/lugli/spuccio/Projects/SP039/scvi_1.py

