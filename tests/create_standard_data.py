#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成标准化的测试数据，用于验证 sci-plot 各图表类型的功能。

数据结构设计：
- standard_xy.csv: 成对数值数据（line, scatter, fill_between）
- standard_categorized.csv: 分类数据（bar, histogram, boxplot, violin, pie）
- standard_grid.csv: 网格数据（contour, pcolormesh, surface3d）
- standard_vector.csv: 向量场数据（quiver, streamplot）
- standard_3d.csv: 3D 数据（scatter3d, bar3d）
"""

import os
import pandas as pd
import numpy as np

# 设置随机种子以确保可重复性
np.random.seed(42)

# 定义输出目录
output_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(output_dir, exist_ok=True)

# =============================================================================
# 1. 成对数值数据 (XY data)
# =============================================================================
"""
用途：line, scatter, fill_between, hexbin, hist2d, ecdf
数据结构：x(数值), y(数值), [group(分类)]
"""
n_points = 50
x_data = np.linspace(0, 10, n_points)
y_data_sin = np.sin(x_data) + np.random.normal(0, 0.1, n_points)
y_data_cos = np.cos(x_data) + np.random.normal(0, 0.1, n_points)

# 创建带分组的 DataFrame
df_xy = pd.DataFrame({
    'x': np.concatenate([x_data, x_data]),
    'y': np.concatenate([y_data_sin, y_data_cos]),
    'group': ['Series_A'] * n_points + ['Series_B'] * n_points
})

df_xy.to_csv(os.path.join(output_dir, 'standard_xy.csv'), index=False)
print(f"Created: standard_xy.csv ({len(df_xy)} rows)")

# 创建无分组的简化版本
df_xy_simple = pd.DataFrame({
    'x': x_data,
    'y': y_data_sin
})
df_xy_simple.to_csv(os.path.join(output_dir, 'standard_xy_simple.csv'), index=False)
print(f"Created: standard_xy_simple.csv ({len(df_xy_simple)} rows)")

# =============================================================================
# 2. 分类数据 (Categorized data)
# =============================================================================
"""
用途：bar, histogram, boxplot, violin, pie, ecdf, eventplot
数据结构：category(分类), value(数值)
"""
categories = ['Control', 'Treated_A', 'Treated_B', 'Treated_C']
n_per_group = 30

values = []
cats = []
for cat in categories:
    # 每个组有不同的均值和方差
    mean = 20 + categories.index(cat) * 5
    std = 2 + categories.index(cat) * 0.5
    values.extend(np.random.normal(mean, std, n_per_group))
    cats.extend([cat] * n_per_group)

df_categorized = pd.DataFrame({
    'category': cats,
    'value': values
})

df_categorized.to_csv(os.path.join(output_dir, 'standard_categorized.csv'), index=False)
print(f"Created: standard_categorized.csv ({len(df_categorized)} rows)")

# =============================================================================
# 3. 网格数据 (Grid data)
# =============================================================================
"""
用途：contour, contourf, pcolormesh, surface3d
数据结构：x(数值), y(数值), z(数值) - 网格化数据
"""
x_grid = np.linspace(0, 5, 20)
y_grid = np.linspace(0, 5, 20)
X, Y = np.meshgrid(x_grid, y_grid)
Z = np.sin(X) * np.cos(Y) + 0.1 * np.random.randn(*X.shape)

# 转换为长格式（用于 CSV）
df_grid = pd.DataFrame({
    'x': X.ravel(),
    'y': Y.ravel(),
    'z': Z.ravel()
})

df_grid.to_csv(os.path.join(output_dir, 'standard_grid.csv'), index=False)
print(f"Created: standard_grid.csv ({len(df_grid)} rows)")

# =============================================================================
# 4. 向量场数据 (Vector field data)
# =============================================================================
"""
用途：quiver, streamplot, barbs
数据结构：x(数值), y(数值), u(数值), v(数值)
"""
x_vec = np.linspace(0, 4, 15)
y_vec = np.linspace(0, 4, 15)
X_vec, Y_vec = np.meshgrid(x_vec, y_vec)
U = -1 - X_vec**2 + Y_vec
V = 1 + X_vec - Y_vec**2

df_vector = pd.DataFrame({
    'x': X_vec.ravel(),
    'y': Y_vec.ravel(),
    'u': U.ravel(),
    'v': V.ravel()
})

df_vector.to_csv(os.path.join(output_dir, 'standard_vector.csv'), index=False)
print(f"Created: standard_vector.csv ({len(df_vector)} rows)")

# =============================================================================
# 5. 3D 散点/柱状图数据
# =============================================================================
"""
用途：scatter3d, bar3d, wire3d, stem3d
数据结构：x(数值/分类), y(数值/分类), z(数值), [category(分类)]
"""
n_3d = 40
x_3d = np.random.rand(n_3d) * 10
y_3d = np.random.rand(n_3d) * 10
z_3d = np.sin(x_3d) * np.cos(y_3d) + np.random.normal(0, 0.1, n_3d)
cat_3d = np.random.choice(['A', 'B', 'C'], n_3d)

df_3d = pd.DataFrame({
    'x': x_3d,
    'y': y_3d,
    'z': z_3d,
    'category': cat_3d
})

df_3d.to_csv(os.path.join(output_dir, 'standard_3d.csv'), index=False)
print(f"Created: standard_3d.csv ({len(df_3d)} rows)")

# =============================================================================
# 6. 累积分布数据 (ECDF)
# =============================================================================
"""
用途：ecdf
数据结构：group(分类), value(数值)
"""
groups = ['Group_X', 'Group_Y']
n_ecdf = 100

values_ecdf = []
groups_ecdf = []
for g in groups:
    if g == 'Group_X':
        values_ecdf.extend(np.random.normal(50, 10, n_ecdf))
    else:
        values_ecdf.extend(np.random.normal(60, 15, n_ecdf))
    groups_ecdf.extend([g] * n_ecdf)

df_ecdf = pd.DataFrame({
    'group': groups_ecdf,
    'value': values_ecdf
})

df_ecdf.to_csv(os.path.join(output_dir, 'standard_ecdf.csv'), index=False)
print(f"Created: standard_ecdf.csv ({len(df_ecdf)} rows)")

# =============================================================================
# 总结
# =============================================================================
print("\n" + "="*60)
print("标准化测试数据生成完成！")
print("="*60)
print(f"输出目录: {output_dir}")
print("\n生成的文件:")
for f in sorted(os.listdir(output_dir)):
    if f.endswith('.csv'):
        filepath = os.path.join(output_dir, f)
        df = pd.read_csv(filepath)
        print(f"  - {f}: {len(df)} 行, {len(df.columns)} 列")
