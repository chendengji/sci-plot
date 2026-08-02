# Sci-Plot

<div align="center">

📊 **一键生成专业级科研图表** — 30+ 期刊风格，500+ 参考代码，开箱即用

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.5%2B-red.svg)](https://matplotlib.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

## 概述

Sci-Plot 是一个基于 matplotlib 的**科研绘图风格化库**，提供：

- **30+ 期刊风格**：Nature、Science、IEEE、Cell、Lancet、PLOS ONE 等
- **50+ 图表类型**：涵盖基础、统计、网格、3D、非结构化数据
- **510+ 参考代码**：来自官方 gallery 的标准实现
- **42+ 参考示例**：教程和图表类型速查
- **CLI + API 双入口**：命令行一键出图，Python 灵活调用

## 快速开始

### 安装

```bash
# 方式一：conda（推荐）
conda env create -f environment.yml
conda activate geo3.13

# 方式二：pip
pip install scienceplots pandas numpy matplotlib
```

### 命令行使用

```bash
# 交互模式（推荐新手）
python src/sci_plot.py --interactive

# 命令行一键出图
python src/sci_plot.py \
  --input data.csv \
  --dtype paired \
  --columns group,value \
  --chart bar \
  --style nature \
  --output figs/bar_nature.png
```

### Python API 使用

```python
import sys
sys.path.insert(0, 'src')
from sci_plot_api import plot_chart

# 加载数据
df = plot_chart.read_data('data.csv')
columns = plot_chart.auto_detect_columns(df, 'paired')

# 生成图表
fig, ax = plot_chart(
    df,
    data_type='paired',
    chart_type='violin',
    style='science',
    columns=columns
)
fig.savefig('figs/violin_science.png', dpi=300, bbox_inches='tight')
```

## 支持的图表类型

### 基础图表 (basic)

| 图表 | 函数 | 适用场景 |
|------|------|----------|
| 柱状图 | `bar()` | 分组对比 |
| 折线图 | `line()` | 趋势、时序 |
| 散点图 | `scatter()` | 相关性分析 |
| 面积图 | `stackplot()` | 构成分析 |
| 填充图 | `fill_between()` | 置信区间 |
| 阶梯图 | `stairs()` | 累积分布 |
| stem 图 | `stem()` | 离散信号 |

### 统计图表 (stats)

| 图表 | 函数 | 适用场景 |
|------|------|----------|
| 箱线图 | `boxplot()` | 分布统计 |
| 小提琴图 | `violin()` | 密度分布 |
| 直方图 | `histogram()` | 单变量分布 |
| ECDF | `ecdf()` | 累积分布函数 |
| 误差棒图 | `errorbar()` | 带误差的数据 |
| 饼图 | `pie()` | 比例构成 |
| 2D 直方图 | `hist2d()` | 双变量密度 |
| 六角蜂群图 | `hexbin()` | 大数据散点 |

### 网格/场数据 (arrays)

| 图表 | 函数 | 适用场景 |
|------|------|----------|
| 伪彩色图 | `pcolormesh()` | 规则网格场 |
| 等高线图 | `contour()` / `contourf()` | 地形、等值线 |
| 图像显示 | `imshow()` | 矩阵可视化 |
| 箭头场 | `quiver()` | 矢量场 |
| 流线图 | `streamplot()` | 流体轨迹 |
| 风羽图 | `barbs()` | 气象数据 |

### 三维图表 (plot3d)

| 图表 | 函数 | 适用场景 |
|------|------|----------|
| 3D 曲线 | `plot3d()` | 空间轨迹 |
| 3D 散点 | `scatter3d()` | 三维点云 |
| 3D 曲面 | `surface3d()` | 函数曲面 |
| 3D 线框 | `wire3d()` | 结构框架 |
| 3D 柱状图 | `bar3d()` | 三维对比 |
| 体素图 | `voxels()` | 体数据 |

### 非规则网格 (unstructured)

| 图表 | 函数 | 适用场景 |
|------|------|----------|
| 三角等高线 | `tricontour()` / `tricontourf()` | 不规则网格 |
| 三角伪彩色 | `tripcolor()` | 散点插值场 |
| 三角网格 | `triplot()` | Delaunay 三角网 |

## 支持的期刊风格

| 风格 | 对应期刊 |
|------|----------|
| `nature` | Nature |
| `science` | Science |
| `ieee` | IEEE Transactions |
| `ieee tran` | IEEEtran |
| `cell` | Cell |
| `plos` | PLOS ONE |
| `elsevier` | Elsevier 期刊 |
| `springer` | Springer 期刊 |
| `aps` | APS 物理期刊 |
| `jgr` | JGR (地球物理) |
| `glt` | 地学线性图 |
| `grid` | 基础网格风格 |
| `scienceplain` | 简洁科学风 |

> 完整列表见 `src/config.py` 中的 `STYLES` 字典。

## 项目结构

```
sci-plot/
├── src/                          # 核心源代码
│   ├── sci_plot.py               # CLI 主程序
│   ├── sci_plot_api.py           # Python API 入口
│   ├── config.py                 # 配置（风格、路径、数据）
│   ├── process_data.py           # 数据处理（6 种数据类型）
│   ├── charts/                   # 43 个图表脚本
│   │   ├── basic/               # 基础图表 (8)
│   │   ├── stats/               # 统计图表 (10)
│   │   ├── arrays/              # 网格/场数据 (8)
│   │   ├── plot3d/              # 三维图表 (11)
│   │   └── unstructured/        # 非规则网格 (5)
│   └── gallery_python/          # 510+ 官方参考代码
│       ├── lines_bars_and_markers/
│       ├── statistics/
│       ├── mplot3d/
│       ├── images_contours_and_fields/
│       ├── specialty_plots/
│       └── ... (共 22 个分类)
├── references/                   # 参考示例
│   ├── plot_types_python/        # 图表类型速查
│   └── tutorials_python/         # 教程
├── tests/                        # 测试脚本和测试数据
├── tools/                        # 辅助工具
├── environment.yml               # conda 环境配置
└── README.md                     # 本文档
```

## 数据类型与推荐图表

| 数据类型 | 说明 | 推荐图表 |
|----------|------|----------|
| `paired` | 成对分组数据 | bar, boxplot, violin, hist |
| `xy_series` | 连续 XY 序列 | line, scatter |
| `distribution` | 统计分布 | violin, hist, ecdf, pie |
| `gridded` | 规则网格 (X,Y,Z) | pcolormesh, contour, quiver |
| `irregular` | 非规则网格 (x,y,z) | tricontour, tripcolor |
| `3d_volume` | 三维/体数据 | surface3d, voxels, scatter3d |

## 数据规范

输入文件支持 **CSV** 和 **Excel (.xlsx/.xls)** 格式。

### 成对数据 (paired)
```csv
group,value
Control,12.5
Control,13.1
Treated,15.2
Treated,14.8
```

### 网格数据 (gridded)
```csv
X,Y,Z
1,1,23.5
1,2,24.1
2,1,22.8
2,2,23.9
```

## 使用技巧

### 推荐图表自动检测
```bash
python src/sci_plot.py --input data.csv --dtype paired --recommend
```
自动分析数据并推荐最佳图表类型。

### 交互式模式
```bash
python src/sci_plot.py --interactive
```
按提示一步步完成数据加载 → 类型选择 → 图表选择 → 风格选择 → 出图。

### 批量生成多风格对比
```python
from sci_plot_api import plot_chart
for style in ['nature', 'science', 'ieee', 'grid']:
    fig, ax = plot_chart(df, 'paired', 'bar', style, columns)
    fig.savefig(f'figs/bar_{style}.png', dpi=300, bbox_inches='tight')
```

## 依赖

- Python ≥ 3.10
- pandas
- numpy
- matplotlib ≥ 3.5
- scienceplots（可选，用于部分期刊风格）

详见 `environment.yml`。

## 许可证

MIT License — 可自由用于学术和商业项目。

## 引用

如果你在使用 Sci-Plot 发表论文，请引用：

```bibtex
@misc{sciplot2024,
  title={{Sci-Plot: A Matplotlib Style Library for Scientific Plotting}},
  author={{chendengji}},
  year={2024},
  url={https://github.com/chendengji/sci-plot}
}
```

## 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/xxx`)
3. 提交更改 (`git commit -am 'Add xxx'`)
4. 推送到分支 (`git push origin feature/xxx`)
5. 创建 Pull Request

---

**Made with ❤️ for the scientific community**
