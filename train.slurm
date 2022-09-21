#!/bin/bash
#SBATCH --nodes 1
#SBATCH --partition gpgpu
#SBATCH --gres=gpu:1
#SBATCH --time 12:00:00
#SBATCH --cpus-per-task=2
#SBATCH --account punim1800
#SBATCH --qos gpgpumse

## Use an account that has GPGPU access

python src/train.py -n "/data/gpfs/projects/punim1800/global-wheat-detection/train" -t "/data/gpfs/projects/punim1800/global-wheat-detection/train"