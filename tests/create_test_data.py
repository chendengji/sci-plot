#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试数据生成
"""
import os
import pandas as pd
import numpy as np

np.random.seed(42)
n = 50
df = pd.DataFrame({
    'group': ['Control'] * n + ['Treated'] * n,
    'value': np.concatenate([
        23.5 + np.random.normal(0, 2, n),
        31.2 + np.random.normal(0, 2, n)
    ])
})

output_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'test_data.csv')
df.to_csv(output_path, index=False)
print(f"Test data created: {output_path}")
