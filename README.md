# Sci-Plot

<div align="center">

📊 **一键生成专业级科研图表** — 4 种期刊风格，37 种图表，500+ 参考代码，开箱即用

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.5%2B-red.svg)](https://matplotlib.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

## 概述

Sci-Plot 是一个面向科研场景的 **matplotlib 风格化绘图框架**，旨在**显著降低科研图表的绘制成本**，提升数据可视化的效率与规范性。

传统科研绘图中，研究者往往需要投入大量时间理解 matplotlib API、调试样式参数、查阅官方示例，导致**绘图成为科研 workflow 中的瓶颈环节**。Sci-Plot 通过以下设计解决这一痛点：

| 核心价值 | 说明 |
|----------|------|
| **零样板代码** | 预置 510+ 官方 gallery 参考实现，用户无需从零编写绘图代码，直接调用即可生成符合期刊规范的图表 |
| **Agent 友好** | 标准化 API 接口支持自动化调用，可无缝集成至 AI Agent 工作流，实现"数据输入 → 图表生成"的全自动 pipeline |
| **期刊级规范** | 内置 4 种期刊风格（Nature / Science / IEEE / grid），确保输出图表满足投稿要求 |
| **效率与稳定性** | 统一的图表接口 + 完整测试覆盖，消除样式调试的不确定性，将绘图时间从数小时缩短至分钟级 |

### 适用场景

- **学术研究**：快速生成符合目标期刊格式的图表，无需反复调整样式
- **自动化分析**：集成至数据处理 pipeline，实现"分析 → 绘图"一键输出
- **批量处理**：对多组数据批量生成对比图表，保持风格一致性
- **AI 辅助科研**：作为 Agent 的绘图工具，支持自然语言指令驱动可视化

### 技术特点

- **模块化设计**：基础图表、统计图表、网格/场数据、三维可视化、非规则网格五大模块，覆盖 37 种图表类型
- **多数据格式支持**：原生支持 CSV、Excel，自动处理分组、网格化、插值等数据预处理
- **双入口架构**：CLI 命令行适合交互式使用，Python API 适合程序化调用

## 快速开始

### 安装

```bash
# 方式一：conda（推荐）
conda env create -f environment.yml
conda activate geo

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
sys.path.insert(0, '<技能目录>')   # 技能根目录（本仓库根目录）
from src.sci_plot_api import plot_chart, read_data

# 加载数据
df = read_data('data.csv')

# 生成图表（返回保存路径字符串，不是 (fig, ax)）
path = plot_chart(df, chart_type='violin',
                  x_col='group', y_col='value',
                  style='science')
print(path)
```

`plot_chart` 完整 kwargs：`x_col / y_col / z_col / group_col`（列映射）、`style`（默认 `nature`）、`title`、`figsize`（None=样式自带，字号按比例联动）、`fontsize`（主控钮）、`dpi`、`constrained_layout`（默认 True）、`legend_loc`、`legend_frame`（默认 False）。

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

| 风格 | 对应期刊 | 自带 figsize | font.size |
|------|----------|-------------|-----------|
| `nature` | Nature | (3.3, 2.5) | 7.0 |
| `science` | Science | (3.3, 2.5) | 7.0 |
| `ieee` | IEEE Transactions | (3.5, 2.6) | 8.0 |
| `grid` | 带网格科学风 | (3.3, 2.5) | 7.0 |

> figsize / font.size / 线宽 / 刻度配套设计；`plot_chart` 默认不覆盖，传 `figsize=` 或 `fontsize=` 时四者按同比例统一缩放。场数据图默认 `cmap='viridis'`（可 `cmap=` 覆盖）；2D 折线/柱类默认去顶右轴线（`despine`）。完整美化规定见 `SKILL.md` 的「样式与美化规定」。完整样式列表见 `src/sci_plot_api.py` 的 `AVAILABLE_STYLES`。

## 项目结构

```
sci-plot/
├── src/                          # 核心源代码
│   ├── sci_plot.py               # CLI 主程序
│   ├── sci_plot_api.py           # Python API 入口
│   ├── config.py                 # 配置（风格、路径、数据）
│   ├── process_data.py           # 数据处理（6 种数据类型）
│   ├── charts/                   # 37 个图表脚本
│   │   ├── basic/               # 基础图表 (7)
│   │   ├── stats/               # 统计图表 (9)
│   │   ├── arrays/              # 网格/场数据 (7)
│   │   ├── plot3d/              # 三维图表 (10)
│   │   └── unstructured/        # 非规则网格 (4)
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
| `xy_series` | 连续 XY 序列 | line, scatter, hexbin, hist2d |
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
from src.sci_plot_api import plot_chart
for style in ['nature', 'science', 'ieee', 'grid']:
    path = plot_chart(df, 'bar', x_col='group', y_col='value', style=style)
    print(style, path)
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
