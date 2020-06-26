#!/bin/bash
#SBATCH -J fairseq3
#SBATCH -p plgrid-gpu-v100
#SBATCH -N 1
#SBATCH -n 8
#SBATCH -A lemkingpu2
#SBATCH --gres=gpu:1
#SBATCH --output="./train_lemmatization5/output.out"
#SBATCH --error="./train_lemmatization5/error.err"
#SBATCH --time=10:00:00

source /net/people/plgagneska/venv_intel/bin/activate
./train_lemmatization3.sh


