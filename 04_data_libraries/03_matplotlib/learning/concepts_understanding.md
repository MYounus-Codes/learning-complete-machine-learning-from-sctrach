# 📊 Matplotlib - Concepts Understanding

> My personal notes for learning Matplotlib from beginner to advanced for Data Analysis and Machine Learning.

---

# What is Matplotlib?

Matplotlib is a Python library used for creating visualizations.

It helps us convert numbers into graphs so that we can easily understand patterns, trends, relationships, and outliers in data.

Without visualization:

```
Sales:
100
120
150
180
210
```

With visualization:

```
|
|        *
|      *
|    *
|  *
|*
+-----------------
```

A graph tells the story much faster than raw numbers.

---

# Why Do We Use Matplotlib?

We use Matplotlib to:

- Explore data
- Understand trends
- Detect outliers
- Compare values
- Analyze distributions
- Present findings
- Create reports
- Understand machine learning datasets

Matplotlib is one of the most important libraries in Data Science.

---

# Where is Matplotlib Used?

- Data Analysis
- Machine Learning
- Deep Learning
- Research
- Business Intelligence
- Finance
- Healthcare
- Scientific Computing

---

# Matplotlib Workflow

Every graph follows the same workflow:

```
Import Library
       ↓
Prepare Data
       ↓
Create Figure
       ↓
Plot Graph
       ↓
Customize
       ↓
Display Graph
```

---

# Pyplot Module

The most commonly used module is:

```python
import matplotlib.pyplot as plt
```

Think of `pyplot` as a drawing toolbox.

It provides functions like:

- plot()
- scatter()
- bar()
- hist()
- pie()
- show()
- figure()
- subplot()

---

# Figure

A Figure is the entire canvas.

Think of it as a blank sheet of paper.

```
+------------------------------------+
|                                    |
|          Entire Figure             |
|                                    |
+------------------------------------+
```

Create:

```python
plt.figure()
```

---

# Axes

Axes are the actual plotting area.

```
Figure
+-----------------------------+
|                             |
|   +-------------------+     |
|   |                   |     |
|   |      Graph        |     |
|   |                   |     |
|   +-------------------+     |
|                             |
+-----------------------------+
```

One Figure can contain multiple Axes.

---

# Plot

A plot connects data points with lines.

Example:

```python
plt.plot(x, y)
```

Used for:

- trends
- time series
- continuous values

---

# Scatter Plot

Shows individual points.

```python
plt.scatter(x, y)
```

Used for:

- relationships
- correlation
- clustering

---

# Bar Chart

Compares categories.

```python
plt.bar(categories, values)
```

Example:

```
Python    ██████████

Java      ███████

C++       █████
```

---

# Horizontal Bar Chart

```python
plt.barh(categories, values)
```

Useful when category names are long.

---

# Histogram

Shows distribution of numerical values.

```python
plt.hist(data)
```

Example:

```
*
**
****
******
****
**
*
```

Used to understand:

- frequency
- spread
- skewness

---

# Pie Chart

Shows percentage contribution.

```python
plt.pie(values)
```

Best for:

- proportions
- percentages

---

# Line Styles

Different line styles:

```
-
--
-.
:
```

Example:

```python
plt.plot(x, y, linestyle="--")
```

---

# Colors

Common colors:

```
blue
red
green
black
yellow
cyan
magenta
orange
purple
```

Example:

```python
plt.plot(x, y, color="red")
```

---

# Markers

Markers highlight data points.

Example:

```python
plt.plot(x, y, marker="o")
```

Common markers:

```
o
s
^
*
x
+
D
```

---

# Line Width

Controls thickness.

```python
plt.plot(x, y, linewidth=3)
```

---

# Marker Size

```python
plt.plot(x, y, markersize=10)
```

---

# Marker Edge Color

```python
plt.plot(
    x,
    y,
    marker='o',
    markeredgecolor='black'
)
```

---

# Marker Face Color

```python
plt.plot(
    x,
    y,
    marker='o',
    markerfacecolor='red'
)
```

---

# Title

Adds graph title.

```python
plt.title("Monthly Sales")
```

---

# X Label

```python
plt.xlabel("Months")
```

---

# Y Label

```python
plt.ylabel("Sales")
```

---

# Legend

Used when multiple plots exist.

```python
plt.legend()
```

Example:

```
Blue → Sales

Red → Profit
```

---

# Grid

Improves readability.

```python
plt.grid(True)
```

---

# Figure Size

```python
plt.figure(figsize=(8,5))
```

---

# DPI

Image quality.

```python
plt.figure(dpi=150)
```

Higher DPI = Better Quality

---

# Multiple Lines

```python
plt.plot(x, sales)

plt.plot(x, profit)
```

---

# Subplots

Multiple graphs inside one figure.

```
+-------+-------+

| Plot1 | Plot2 |

+-------+-------+

| Plot3 | Plot4 |

+-------+-------+
```

Example:

```python
plt.subplot(2,2,1)
```

Meaning:

2 rows

2 columns

Current graph = 1

---

# Tight Layout

Automatically adjusts spacing.

```python
plt.tight_layout()
```

---

# Save Figure

Instead of displaying:

```python
plt.savefig("graph.png")
```

Useful for reports.

---

# Show Graph

Displays graph.

```python
plt.show()
```

Always call it after plotting.

---

# Object-Oriented Method

Recommended for professional work.

Instead of:

```python
plt.plot()
```

Use:

```python
fig, ax = plt.subplots()

ax.plot(x, y)
```

Advantages:

- Cleaner code
- Better customization
- Multiple plots become easier

---

# Common Plot Types

| Plot | Purpose |
|------|----------|
| plot() | Trends |
| scatter() | Relationship |
| bar() | Category comparison |
| barh() | Horizontal comparison |
| hist() | Distribution |
| pie() | Percentage |
| boxplot() | Outliers |
| violinplot() | Distribution shape |
| stem() | Discrete signals |
| step() | Step graph |
| stackplot() | Cumulative data |

---

# Common Customizations

- Title
- Labels
- Grid
- Legend
- Colors
- Markers
- Line Width
- Figure Size
- Font Size
- Axis Limits
- Tick Labels

---

# Visualization Workflow in Data Science

```
Dataset
    ↓

Cleaning
    ↓

EDA
    ↓

Matplotlib
    ↓

Insights
    ↓

Feature Engineering
    ↓

Machine Learning
```

---

# Matplotlib vs Seaborn

| Matplotlib | Seaborn |
|------------|----------|
| Low-level | High-level |
| More customization | Easier syntax |
| Basic styling | Beautiful styling |
| Foundation | Built on Matplotlib |

---

# Best Practices

- Always label axes.
- Add a meaningful title.
- Use legends when plotting multiple datasets.
- Avoid too many colors.
- Keep graphs simple.
- Choose the correct chart type.
- Add grid when helpful.
- Use readable figure sizes.
- Save figures with high DPI for reports.
- Prefer the object-oriented API (`fig, ax = plt.subplots()`) for larger projects.

---

# Where Matplotlib Fits in ML Pipeline

```
CSV Dataset

      ↓

Pandas

      ↓

Cleaning

      ↓

Matplotlib

      ↓

EDA

      ↓

Feature Engineering

      ↓

NumPy Arrays

      ↓

Scikit-Learn

      ↓

Model Training

      ↓

Evaluation
```

---

# Key Takeaways

- Matplotlib is the foundation of Python visualization.
- Every graph starts with data.
- A Figure is the canvas, and Axes are the plotting area.
- Different plot types answer different questions.
- Customization makes graphs easier to understand.
- Visualization is an essential part of Exploratory Data Analysis (EDA).
- Learning Matplotlib well makes it easier to use libraries like Seaborn and Plotly later.

---