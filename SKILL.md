# Sci-Plot 技能

根据用户提供的原始数据，生成 SCI 期刊品质的科学图表。

## 前置条件

- **环境**: `conda geo`（已装 scienceplots；不是 geo3.13）
- **技能根目录**: `/home/chen/claude/.claude/skills/sci-plot`（本 SKILL.md 所在目录）
- **统一 API 入口**: `src/sci_plot_api.py` 中的 `plot_chart()`

### 导入方式（任选其一）

```python
# 方式 A（推荐）：把技能根目录加入 sys.path，输出写到用户当前工作目录/plot/
import sys
sys.path.insert(0, '/home/chen/claude/.claude/skills/sci-plot')
from src.sci_plot_api import plot_chart, read_data, auto_detect_columns, recommend_charts, list_charts, list_styles
```

```bash
# 方式 B：cd 到技能根目录后用 -m 运行（输出会写到技能目录/plot/，不建议）
cd /home/chen/claude/.claude/skills/sci-plot && python -m src.sci_plot_api -i data.csv -ch line --xcol x --ycol y
```

> 旧写法 `from src.sci_plot_api import ...` 若不先把技能根目录加入 `sys.path`，会报 `ModuleNotFoundError: No module named 'config'`。务必先 `sys.path.insert`。

## 样式与美化规定

技能的绘图美化分两层管：**集中默认**（在 `plot_chart` 里统一缩放/配色/布局/轴线）+ **图表模块就近处理**（结构性参数）。下列规定对齐 SCI 期刊图面习惯，默认值即期刊合理态；同时暴露 kwarg，让 LLM 按具体图情自主微调。

### 1. 样式选择

scienceplots 的 4 个样式，每个自带一套配套 rcParams（figsize / font.size / 线宽 / 刻度），恒定加 `'no-latex'`（不依赖本地 LaTeX）：

| 样式 | 自带 figsize | 自带 font.size | 适用 |
|------|-------------|---------------|------|
| `nature` | (3.3, 2.5) | 7.0 | 期刊单栏（默认） |
| `science` | (3.3, 2.5) | 7.0 | 通用科学风 |
| `ieee` | (3.5, 2.6) | 8.0 | IEEE |
| `grid` | (3.3, 2.5) | 7.0 | 带网格 |

> 默认 `style='nature'`。图按原尺寸放进论文单栏（~3.3–3.5in）时字号/线宽比例正合适。

### 2. 统一缩放（figsize ↔ 字号 ↔ 线宽 ↔ 刻度）

`_apply_typography(figsize, fontsize)` 保证「字号、数据线宽、轴宽、刻度尺寸」按同一比例同步缩放，避免大图小字细线。规则：

- 都不传 → 完全沿用样式自带值（推荐）。
- 传 `figsize=(w,h)` → 按比例同步放大字号/线宽/刻度。
- 传 `fontsize=N` → 按比例同步放大线宽/刻度。
- 3.3in→6in 时 font 7→12.7pt、lines.linewidth 1.0→1.82、axes.linewidth 0.5→0.91（实测）。

### 3. 配色

- **场数据图**（contour/imshow/pcolormesh/hexbin/hist2d/surface3d/trisurf3d/scatter3d/…）默认 `cmap='viridis'`（感知均匀 + 色盲友好，SCI 通用），用 `cmap=` kwarg 覆盖。备选：`plasma`（暖向）、`cividis`（纯色盲友好）、`coolwarm`（双向发散数据）、`gray`（印刷黑白）。
- **分类数据**（line/bar/violin/scatter 分组）颜色跟随样式色环（`ax._get_lines.get_next_color()`），不硬编码；色环为 scienceplots 默认（蓝/橙/绿/红/紫/棕），≤6 组区分清晰。
- 需自定义配色时，LLM 可在调 `plot_chart` 前设 `plt.rcParams['axes.prop_cycle']`，或对场数据传 `cmap=`。

### 4. 线宽与刻度

- 数据线宽默认跟随样式（随 figsize 统一缩放）；`line`/`scatter`/`fill_between` 等接受 `linewidth=` kwarg 覆盖。
- 等高线标号字号（`clabel`）跟随 `font.size` 缩放（不再写死 8pt）。
- 轴线/刻度宽度由样式 + `_apply_typography` 统一缩放，不单独暴露。

### 5. 图例

- 默认**无边框**（`legend_frame=False`）、位置可配（`legend_loc=`，如 `'best'`/`'upper left'`）。
- 模块内 `ax.legend()` 的标签会被保留，`plot_chart` 统一重建以套用边框/位置。
- 无分组标签的图（如单线 scatter、bar）自动不加图例。

### 6. 布局与轴线

- 2D 默认 `constrained_layout=True`（多子图 / colorbar / legend 不打架，不裁切）；3D 因支持有限自动回退 `tight_layout` + `bbox_inches='tight'`。
- **去轴线**：2D 折线/柱/散点/统计类默认去顶/右两条 spine（`despine`，干净风格，SCI 习惯）；场数据图（contour/imshow/…）与 3D 默认保留四框（数据填满画布）。`despine=` kwarg 可强制 True/False。
- 中文：自动注册 WSL2 挂载的 SimHei/SimSun，`axes.unicode_minus=False`。

### 7. SCI 美化原则（LLM 判断依据）

下列为期刊图面共识，**默认已套**，LLM 按图情判断是否偏离：

- **最小 chartjunk**：默认无网格（除 `grid` 样式）、无图例边框、去多余 spine；除非数据确实需要参考线。
- **不要为 2D 数据用 3D**：柱状/饼图别加 3D 投影，降读图精度。
- **误差棒带 cap**：`errorbar`/`bar` 默认 `capsize=5`。
- **标签含单位**：`set_xlabel`/`set_ylabel` 用列名时，LLM 应在标题/标签补单位（如 `Axial strain (%)`、`Stress (MPa)`）。
- **单栏宽度优先**：多图拼版时优先单栏宽（~3.3in）+ 多子图，而非一张超大图。
- **分组≤6**：分类色环超 6 组区分度下降，多于此改用 `tab10`/`Set2` 或换图表类型。
- **不过度修饰**：不加阴影/渐变/3D 斜面/背景色；线宽/字号按比例即可，别逐元素手调。

### 8. 美化 kwargs 总表

| kwarg | 默认 | 作用 |
|-------|------|------|
| `style` | `'nature'` | 期刊样式 |
| `figsize` | `None`(用样式) | 图片尺寸；字号/线宽/刻度同比例缩放 |
| `fontsize` | `None`(用样式) | 基准字号主控钮 |
| `linewidth` | `None`(用样式) | 数据线宽，line/scatter/fill_between 生效 |
| `cmap` | `'viridis'` | 场数据图 colormap |
| `despine` | 自动 | 去顶/右轴线（2D 折线类 True，场/3D False） |
| `constrained_layout` | `True`(2D) | 约束布局 |
| `legend_loc` | `None`(默认) | 图例位置 |
| `legend_frame` | `False` | 图例边框 |
| `dpi` | `300` | 输出 DPI |

### 9. LLM 自主性

以上是**默认 + 原则**，不是逐元素硬规。LLM 应：① 默认值通常够用，先按默认出图；② 仅在数据/版式确有需要时改对应 kwarg（如双向数据换 `coolwarm`、多子图加大 `figsize`、标签补单位）；③ 避免无意义堆砌修饰。给具体图情留判断空间，不必每张图都把 kwarg 调满。

## 工作流程

### Step 1: 询问数据位置

- 问用户数据文件在哪里（CSV / Excel / TXT / DAT）
- 读取后展示：前 5 行、列名、数据类型

```python
df = read_data("用户提供的路径")
print(df.head()); print(df.dtypes)
```

### Step 2: 分析数据 + 列映射

```python
col_info = auto_detect_columns(df)   # {'numeric': [...], 'categorical': [...], 'other': [...]}
recs = recommend_charts(df)          # [(chart_type, 说明), ...]
```

与用户确认列映射：哪列是 x、哪列是 y、是否需要 group_col。

### Step 3: 选择图表类型

| 数据类型 | 列需求 | 可用图表 |
|---------|--------|---------|
| **成对数据** | 1 分类 + 1 数值 | `bar boxplot violin hist ecdf pie stem errorbar eventplot stairs stackplot fill_between` |
| **连续 XY 数据** | 2 数值 + 可选分组 | `line` `scatter` `hexbin` `hist2d` ← 应力应变、时间序列、二维密度 |
| **网格数据** | x, y, z | `contour contourf pcolormesh imshow quiver streamplot barbs` |
| **不规则数据** | x, y, z | `tricontour tricontourf tripcolor triplot` |
| **3D 数据** | x, y, z (+可选 c/v) | `plot3d scatter3d surface3d wire3d bar3d stem3d voxels trisurf3d` |

> ⚠️ 图表类型名用 `line` / `scatter`，**不是** `xy_line` / `xy_scatter`（旧文档写法已废弃，注册表无此类型会报 `Unknown chart type`）。
> `hexbin` / `hist2d` 需要两个**数值**列（属 xy_series），不要当成分组柱状图用。

```python
all_charts = list_charts()   # 37 种
```

### Step 4: 选择样式

```python
styles = list_styles()   # ['science', 'nature', 'ieee', 'grid']
```

| 样式 | 适用 |
|------|------|
| `science` | 通用科学风格 |
| `nature` | **Nature 期刊风格（默认）** |
| `ieee` | IEEE 期刊风格 |
| `grid` | 带网格线的科学风格 |

> 旧文档列的 `ieeetran / cell / plos / elsevier / springer / aps / jgr` 等样式 scienceplots **未提供**，调用会抛 `OSError`。仅上述 4 种可用。

### Step 5: 生成图表

**成对数据（分组统计图）**:
```python
path = plot_chart(df, 'bar',
                  x_col='group', y_col='value',
                  style='science', title='Bar Plot')
print(f"Saved: {path}")
```

**连续 XY 数据（应力应变曲线、时间序列）**:
```python
path = plot_chart(df, 'line',              # 不是 'xy_line'
                  x_col='axial_strain',
                  y_col='axial_stress_mpa',
                  group_col='sample_code',   # 可选分组
                  style='nature',
                  title='Stress-Strain Curve')
```

数据会自动标准化处理（去空值、排序、保存到 `plot/data/`）。

### Step 6: 展示结果

- 告诉用户图片路径（`<当前工作目录>/plot/fig_{type}_{timestamp}.png`）
- 展示图片预览，询问是否调整参数或换图表类型

## 批量生成多图

```python
for chart in ['bar', 'boxplot', 'violin', 'scatter']:
    path = plot_chart(df, chart, x_col='group', y_col='value', style='nature')
    print(f"  {chart}: {path}")
```

## 一键快捷绘图

```python
from src.sci_plot_api import quick_plot
path = quick_plot("data.csv", "line", x_col='x', y_col='y', group_col='group')
```

## 输出文件

- 图片: `<当前工作目录>/plot/fig_{type}_{timestamp}.png`，300 DPI
- 时间戳命名，不覆盖
- 标准化数据自动存到 `<当前工作目录>/plot/data/`
- 输出根目录可用环境变量 `SCI_PLOT_OUTPUT_DIR` 覆盖（如不想污染当前目录）

## 注意事项

1. 原始数据文件**不存进项目**，用户自行管理
2. `plot_chart` 会自动调 `process_data` 做标准化预处理
3. 所有图表用 `scienceplots` 样式，已包含 `no-latex`（无需本地 LaTeX）
4. 3D 图表自动创建 `projection='3d'` 坐标轴
5. 网格/不规则/3D 类图表需要 x, y, z 三列
6. `line`/`scatter` 的 `group_col` 是可选参数
7. matplotlib ≥ 3.9 已移除 `boxplot`/`eventplot` 的 `labels=` 参数，本技能已改用 `tick_labels` / 手动设刻度
