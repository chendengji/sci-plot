# Sci-Plot Skill

根据原始数据生成 SCI 期刊品质的科学图表，由 Claude Code 全程管理。

## 快速开始

```bash
# 1. 激活环境
conda activate geo3.13

# 2. 进入项目
cd D:\CODE\sci-plot

# 3. 在 Claude Code 中直接说：
# "帮我画图，数据在 D:\data\exp.csv"
```

## 目录结构

```
sci-plot/
├── SKILL.md                       ← Claude Code 技能定义
├── README.md                      ← 本文件
├── src/                           ← 核心代码
│   ├── sci_plot_api.py            ← 统一 API 入口
│   ├── sci_plot.py                ← CLI 模式
│   ├── process_data.py            ← 数据处理
│   ├── config.py                  ← 路径配置
│   ├── charts/                    ← 常规绘图库 (43个脚本)
│   │   ├── basic/        9种      bar, line, scatter, stem, ...
│   │   ├── stats/         9种     boxplot, violin, histogram, ecdf, ...
│   │   ├── arrays/        7种     contour, pcolormesh, imshow, ...
│   │   ├── plot3d/       10种    surface3d, scatter3d, voxels, ...
│   │   └── unstructured/  4种    tricontour, tripcolor, ...
│   └── gallery_python/           ← 高阶绘图库 (510个脚本参考)
├── references/                    ← 原始参考代码（已备份）
│   ├── gallery_python/
│   ├── plot_types_python/ 37个
│   └── tutorials_python/   5个
├── tests/                         ← 测试数据与脚本
│   ├── data/
│   │   ├── standard_xy.csv           标准XY数据 (x, y)
│   │   ├── standard_categorized.csv  分组数据 (category, value)
│   │   ├── standard_grid.csv         网格数据 (x, y, z)
│   │   ├── standard_3d.csv           3D数据 (x, y, z)
│   │   ├── standard_vector.csv       矢量数据 (x, y, u, v)
│   │   ├── standard_xy_simple.csv    简单XY数据
│   │   ├── standard_ecdf.csv         ECDF数据
│   │   ├── test_data.csv             (2组: Control, Treated)
│   │   └── test_distribution.csv     (3组: Control, A, B)
│   ├── create_test_data.py
│   └── create_test_dist.py
├── figs/                          ← 输出图表
├── data/                          ← 处理后的标准化数据
└── archive/                       ← 旧版本备份
```

## 功能

| 功能 | 说明 |
|------|------|
| **数据输入** | CSV, Excel, TXT, DAT — 任意位置文件 |
| **自动分析** | 自动检测数值列、分类列，推荐图表类型 |
| **图表类型** | 39种，覆盖基础/统计/网格/3D/不规则数据 |
| **样式** | science, nature, ieee, ieeetran, grid |
| **输出** | 300 DPI PNG，时间戳命名不覆盖 |

## 图表类型 39 种

### basic (连续XY数据: x_col, y_col, 可选 group_col)
`bar` `line` `scatter` `stem` `stairs` `stackplot` `fill_between`

### stats (成对数据: x_col=分组, y_col=数值)
`boxplot` `violin` `hist` `ecdf` `pie` `errorbar` `hexbin` `hist2d` `eventplot`

### arrays (网格数据: x, y, z)
`contour` `contourf` `pcolormesh` `imshow` `quiver` `streamplot` `barbs`

### plot3d (3D数据: x, y, z)
`plot3d` `scatter3d` `surface3d` `wire3d` `bar3d` `stem3d` `voxels` `trisurf3d` `quiver3d` `fill_between3d`

### unstructured (不规则数据: x, y, z)
`tricontour` `tricontourf` `tripcolor` `triplot`

## Python API

```python
from src.sci_plot_api import plot_chart, read_data, auto_detect_columns, list_charts, list_styles

# 1. 读数据
df = read_data("实验数据.csv")

# 2. 自动检测列
col_info = auto_detect_columns(df)

# 3. 绘图
path = plot_chart(df, 'violin', x_col='group', y_col='value', style='nature')
print(f"Saved: {path}")
```

## 技术细节

- **环境**: conda geo3.13
- **依赖**: pandas, numpy, matplotlib, scienceplots
- **样式**: `plt.style.use(['{style}', 'no-latex'])`
- **DPI**: 300
- **图片尺寸**: 5×4 inches (可自定义)
- **命名**: `fig_{type}_{YYYYMMDD_HHMMSS}.png`

## 项目演进

- ✅ 510个参考脚本中 490个已改造为使用标准化 CSV 数据
- ✅ 项目结构重组：`charts/` 常规绘图库 + `gallery_python/` 高阶绘图库
- ✅ 标准化测试数据 7 种类型覆盖所有图表类型
