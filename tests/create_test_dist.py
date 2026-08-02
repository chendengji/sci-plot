#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成测试数据 - 用于分布图测试
"""
import os
import pandas as pd
import numpy as np

np.random.seed(42)
n = 50
groups = ['Control'] * n + ['Treatment A'] * n + ['Treatment B'] * n
values = np.concatenate([
    23.5 + np.random.normal(0, 2, n),      # Control
    31.2 + np.random.normal(0, 2, n),      # Treatment A
    28.0 + np.random.normal(0, 2, n)       # Treatment B
])

df = pd.DataFrame({'group': groups, 'value': values})
output_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'test_distribution.csv')
df.to_csv(output_path, index=False)
print(f"Test data created: {output_path}")
print(f"Groups: {df['group'].unique()}, Shape: {df.shape}")
