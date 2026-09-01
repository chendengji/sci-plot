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

## 字号与间距约定（重要）

scienceplots 的期刊样式是「**figsize + font.size 配套**」设计的，不可单独放大其一：

| 样式 | 自带 figsize | 自带 font.size | 适用 |
|------|-------------|---------------|------|
| `nature` | (3.3, 2.5) | 7.0 | 期刊单栏（默认） |
| `science` | (3.3, 2.5) | 7.0 | 通用科学风 |
| `ieee` | (3.5, 2.6) | 8.0 | IEEE |
| `grid` | (3.3, 2.5) | 7.0 | 带网格 |

**默认行为**：`plot_chart` 不再覆盖样式自带 figsize，字号也保持样式基准——图按原尺寸放进论文版面时比例正好。

**调整字号/尺寸的 kwarg**：

```python
plot_chart(df, 'line', x_col='x', y_col='y',
           style='nature',
           figsize=(6, 4),     # 自定义尺寸：字号会按 新宽/3.3 比例自动放大，保持比例
           fontsize=10,        # 或直接指定基准字号(pt)，作为主控钮覆盖一切
           constrained_layout=True,   # 约束布局：多子图/colorbar/legend 不打架（2D 默认开）
           legend_loc='upper left',   # 图例位置
           legend_frame=False)        # 图例边框，默认关
```

- **只放大图不改字号 → 字会偏小**：已被 `_apply_typography` 修复，传 `figsize=` 时字号按比例同步放大。
- **多子图/带 colorbar 的图**：保持 `constrained_layout=True`（默认），不要退回 `tight_layout`，否则易裁切/重叠。
- **3D 图**：`constrained_layout` 对 3D 支持有限，自动回退 `tight_layout`。
- **中文**：自动注册 WSL2 挂载的 SimHei/SimSun，无需额外配置；`axes.unicode_minus` 已置 False。

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
