#!/bin/bash
#SBATCH -J fairseq
#SBATCH -p plgrid-gpu-v100
#SBATCH -N 1
#SBATCH -n 8
#SBATCH -A lemkingpu2
#SBATCH --gres=gpu:1
#SBATCH --output="./eval_lemmatization4/output.out"
#SBATCH --error="./eval_lemmatization4/error.err"
#SBATCH --time=02:00:00

source /net/people/plgagneska/venv_intel/bin/activate
./generate_eval_lemmatization3.sh


