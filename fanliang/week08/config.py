# -*- coding: utf-8 -*-
import os
"""
配置参数信息
"""

Config = {
    "model_path": "model_output",
    "schema_path": os.path.dirname(os.path.abspath(__file__))+"/../data/schema.json",
    "train_data_path": os.path.dirname(os.path.abspath(__file__))+"/../data/train.json",
    "valid_data_path": os.path.dirname(os.path.abspath(__file__))+"/../data/valid.json",
    "vocab_path":os.path.dirname(os.path.abspath(__file__))+"/../chars.txt",
    "max_length": 20,
    "hidden_size": 128,
    "epoch": 100,
    "batch_size": 32,
    "epoch_data_size": 200,     #每轮训练中采样数量
    "positive_sample_rate":0.5,  #正样本比例
    "optimizer": "adam",
    "learning_rate": 1e-3,
}