# Sci-Plot 技能

根据用户提供的原始数据，生成 SCI 期刊品质的科学图表。

## 前置条件

- 环境: `conda geo3.13` (或安装了 scienceplots 的 Python 环境)
- 工作目录: `D:\CODE\sci-plot`
- 脚本路径: `src/sci_plot_api.py` (统一API入口)

## 工作流程

### Step 1: 询问数据位置

- 问用户数据文件在哪里
- 支持 CSV, Excel, TXT, DAT
- 读取后展示: 前 5 行、列名、数据类型

```python
from src.sci_plot_api import read_data
df = read_data("用户提供的路径")
print(df.head())
print(df.dtypes)
```

### Step 2: 分析数据 + 列映射

**自动检测列类型:**
```python
from src.sci_plot_api import auto_detect_columns
col_info = auto_detect_columns(df)
# 返回: {'numeric': [...], 'categorical': [...], 'other': [...]}
```

**推荐图表:**
```python
from src.sci_plot_api import recommend_charts
recs = recommend_charts(df)
# 返回: [(chart_type, description), ...]
```

**与用户确认列映射:**
> 检测到以下列:
>   数值列: axial_strain, axial_stress_mpa
>   分类列: sample_code
> 推荐图表: xy_line (连续x-y折线图)
> 哪列是 x(自变量)? [axial_strain]
> 哪列是 y(因变量)? [axial_stress_mpa]
> 是否需要分组列? [sample_code]

### Step 3: 选择图表类型

根据数据类型选择:

| 数据类型 | 列需求 | 可用图表 |
|---------|--------|---------|
| **成对数据** | 1 分类 + 1 数值 | bar, boxplot, violin, scatter, line, hist, ecdf, pie, stem, point, swarm, errorbar, stairs, stackplot, fill_between, eventplot |
| **连续XY数据** | 2 数值 + 可选分组 | **xy_line**, **xy_scatter** ← 应力应变曲线、时间序列 |
| **网格数据** | x, y, z 三列 | contour, contourf, pcolormesh, imshow, quiver, streamplot, barbs |
| **不规则数据** | x, y, z 三列 | tricontour, tricontourf, tripcolor, triplot |
| **3D数据** | x, y, z 三列+ | plot3d, scatter3d, surface3d, wire3d, bar3d, voxels, trisurf3d |

完整列表:
```python
from src.sci_plot_api import list_charts
all_charts = list_charts()  # 41 种图表
```

### Step 4: 选择样式

```python
from src.sci_plot_api import list_styles
styles = list_styles()  # ['science', 'nature', 'ieee', 'ieeetran', 'grid']
```

| 样式 | 适用场景 |
|------|---------|
| `science` | 通用科学风格 |
| `nature` | **Nature 期刊风格（默认）** |
| `ieee` | IEEE 期刊风格 |
| `ieeetran` | IEEE 双栏排版 |
| `grid` | 带网格线的科学风格 |

### Step 5: 生成图表

**成对数据 (分组统计图):**
```python
from src.sci_plot_api import plot_chart

path = plot_chart(df, 'bar',          # 图表类型
                  x_col='group',       # 分组列
                  y_col='value',       # 数值列
                  style='science',     # 样式
                  title='Bar Plot')    # 可选标题
print(f"Saved: {path}")
```

**连续XY数据 (应力应变曲线、时间序列):**
```python
path = plot_chart(df, 'xy_line',               # 连续x-y折线图
                  x_col='axial_strain',         # x轴列
                  y_col='axial_stress_mpa',     # y轴列
                  group_col='sample_code',      # 分组列(可选)
                  style='nature',               # 样式
                  title='Stress-Strain Curve')  # 标题
print(f"Saved: {path}")
```

**数据会自动标准化处理** (去空值、排序、保存到 data/ 目录)。

### Step 6: 展示结果

- 告诉用户图片保存路径 (`D:\CODE\sci-plot\figs\`)
- 展示图片给用户预览
- 询问是否要调整参数或换一种图表类型

## 批量生成多图

```python
charts = ['bar', 'boxplot', 'violin', 'scatter']
for chart in charts:
    path = plot_chart(df, chart, x_col='group', y_col='value', style='nature')
    print(f"  {chart}: {path}")
```

## 一键快捷绘图

```python
from src.sci_plot_api import quick_plot
path = quick_plot("data.csv", "xy_line", x_col='x', y_col='y', group_col='group')
```

## 输出文件

- 图片: `D:\CODE\sci-plot\figs\fig_{type}_{timestamp}.png`
- 300 DPI, bbox_inches='tight'
- 时间戳命名，不会覆盖
- 处理后的标准化数据自动保存到 `data/` 目录

## 注意事项

1. 原始数据文件**不存储在项目中**，用户自行管理
2. `plot_chart` 会自动调用 `process_data.py` 进行数据标准化预处理
3. 所有图表使用 `scienceplots` 库的样式，符合期刊美观要求
4. 3D 图表会自动创建 `projection='3d'` 坐标轴
5. 网格类图表 (contour, pcolormesh, surface3d等) 需要 x, y, z 三列
6. 连续XY图表 (xy_line, xy_scatter) 的 `group_col` 是可选参数