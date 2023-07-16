#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python3 soloist_train.py \
--output_dir=models/$2 \
--model_type=gpt2 \
--model_name_or_path=gtg_pretrained \
--do_train \
--train_data_file=data/$1 \
--per_gpu_train_batch_size 1 \
--num_train_epochs 10 \
--learning_rate 5e-5 \
--overwrite_cache \
--save_steps 10000 \
--max_seq 100 \
--overwrite_output_dir \
--max_turn 1 \
--mc_loss_efficient 1 