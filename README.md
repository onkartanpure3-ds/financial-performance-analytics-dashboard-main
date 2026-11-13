# 📊 Financial Performance Analytics Dashboard

An end-to-end analytics project that turns raw financial sales data into clean, structured tables, runs SQL analysis on it, and presents the results in an interactive 3-page **Microsoft Power BI** dashboard.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
</p>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Tech Stack](#️-tech-stack)
- [Dashboard Pages](#-dashboard-pages)
- [Key Insights](#-key-insights)
- [KPIs](#-kpis)
- [Workflow](#-workflow)
- [Repository Structure](#-repository-structure)
- [Setup Guide](#-setup-guide)
- [Author](#-author)

---

## 📌 Project Overview

Businesses need a clear view of how revenue, profit, products and discounts connect. This project builds a simple pipeline to answer questions such as:

- How much revenue and profit are we making, and when does demand peak?
- Which customer segments and countries drive revenue?
- Which products are the most profitable?
- How do discounts affect profit margins?

## 🛠️ Tech Stack

| Purpose | Tool |
|---|---|
| Data cleaning & loading | Python, Pandas, PyMySQL |
| Storage & analysis | MySQL (SQL queries, views) |
| Visualization | Microsoft Power BI (DAX measures, slicers) |

---

## 📈 Dashboard Pages

The Power BI report has three connected pages. Use the navigation buttons at the top (**Overview**, **Product Performance**, **Discount Analysis**) to switch between them.

---

### 1️⃣ Overview Dashboard

<p align="center">
  <img src="screenshots/overview.jpeg" alt="Financial Performance Dashboard - Overview" width="100%" />
</p>

**What it shows:** A high-level view of the company's financial health across time, customer segments and countries.

| Visual | Explanation |
|---|---|
| **KPI Cards** | Total Profit **15.45M**, Total Revenue **112.47M**, Profit Margin **13.74%**, Total Units Sold **1,067,593** |
| **Monthly Revenue Trend** | Revenue stays around 6M-8M for most of the year, then climbs from September and **peaks in October (20M+)**, showing strong seasonal demand |
| **Revenue by Segment** | Government (**46M**) and Small Business (**42M**) lead, followed by Enterprise (20M), Midmarket (2M) and Channel Partners (2M) |
| **Revenue by Country** | Waterfall chart showing how the USA, Germany, Canada, France and Mexico add up to the total revenue |
| **Slicers** | Filter the whole page by **Segment** and **Year** (2013 / 2014) |

**Insight:** Revenue peaks in October, and high discount levels reduce profit margins.

---

### 2️⃣ Product Performance Dashboard

<p align="center">
  <img src="screenshots/product-analysis.jpeg" alt="Product Performance Dashboard" width="100%" />
</p>

**What it shows:** Which products earn the most, and how healthy their margins are.

| Visual | Explanation |
|---|---|
| **Summary Cards** | Total Products **6**, Total Profit **15.45M**, Avg Profit per Product **2.58M**, Top Product **Paseo** |
| **Profit by Product** | Ranking: Paseo (4.1M) > VTT (3.0M) > Amarilla (2.7M) > Montana (2.1M) > Velo (2.0M) > Carretera (1.6M) |
| **Product Profitability Analysis** | Scatter plot of units sold vs profit; Paseo sits far ahead of the other products |
| **Revenue vs Profit by Product** | Side-by-side bars of sales and profit for each product (Paseo: 30.1M sales, 4.1M profit) |
| **Product Profitability Matrix** | Table of sales, profit, units sold and margin %. **Amarilla** has the best margin (**15.67%**), **Velo** the lowest (**12.14%**) |
| **Slicers** | Filter by **Product**, **Segment** and **Year** |

**Insight:** Paseo contributes the highest profit and revenue, while lower-margin products need pricing optimization.

---

### 3️⃣ Discount Impact Analysis Dashboard

<p align="center">
  <img src="screenshots/discount-analysis.jpeg" alt="Discount Impact Analysis Dashboard" width="100%" />
</p>

**What it shows:** How different discount levels (None, Low, Medium, High) affect volume, revenue and profit.

| Visual | Explanation |
|---|---|
| **Summary Cards** | Discount Revenue **105.10M**, Profit After Discount **15.45M**, Avg Discount Impact **1.62K**, Profit Margin **13.74%** |
| **Profit Margin by Discount Level** | Margin drops steadily as discounts increase: None **21.44%** > Low **17.33%** > Medium **13.97%** > High **8.68%** |
| **Revenue & Profit by Discount Band** | Medium discounts give the highest revenue (37M); None earns the least revenue (7M) |
| **Units Sold by Discount Level** | Volume grows with discounts: High 0.38M, Medium 0.35M, Low 0.25M, None 0.08M |
| **Discount Band Matrix** | Table of sales, profit, units sold and margin % for each band |
| **Slicers** | Filter by **Segment**, **Year** and **Country** |

**Insight:** High discounts increase sales volume but reduce profit margins. Medium discounts balance revenue and profitability, and low discounts give higher margins with controlled growth.

---

## 💡 Key Insights

- 🏆 **Paseo** is the top product: highest sales ($30.1M) and profit ($4.08M).
- ✅ **Amarilla** has the best margin (15.67%), while **Velo** has the lowest (12.14%), so lower-margin products need pricing review.
- 📅 **October** is the revenue peak, which points to strong seasonal demand.
- 🏢 **Government** ($46M) and **Small Business** ($42M) generate most of the revenue.
- 🏷️ **Discounts boost volume but hurt margin:**

| Discount Band | Profit Margin | Units Sold |
|---|---|---|
| None | 21.44% | 82,753 |
| Low | 17.33% | 254,427 |
| Medium | 13.97% | 345,452 |
| High | 8.68% | 384,961 |

> **Takeaway:** Medium discounts balance revenue and profit; low discounts give the best margins with controlled growth.

---

## 🎯 KPIs

| KPI | Value |
|---|---|
| Total Revenue | $112.47M |
| Total Profit | $15.45M |
| Profit Margin | 13.74% |
| Total Units Sold | 1,067,593 |
| Discount Revenue | $105.10M |
| Avg Profit per Product | $2.58M |

---

## 🏗️ Workflow

```text
CSV Dataset → Python (clean & load) → MySQL (QA, dedupe, views) → Power BI (3-page dashboard)
```

1. **Load:** Python + Pandas clean the column names and handle null values, then PyMySQL loads the data into MySQL.
2. **Clean:** SQL checks for invalid values and removes duplicates (`ROW_NUMBER()`).
3. **Analyze:** SQL queries and a reporting view calculate revenue, profit, margin and discount metrics.
4. **Visualize:** Power BI connects to the data and presents the interactive dashboard.

---

## 📁 Repository Structure

```text
financial-performance-analytics-dashboard/
├── dataset/          # Source CSV data
├── screenshots/      # Dashboard images used in this README
│   ├── overview.jpeg
│   ├── product-analysis.jpeg
│   └── discount-analysis.jpeg
├── *.sql             # Table creation, cleaning and analysis queries
├── *.py              # Python data loading script
├── *.pbix            # Power BI dashboard file
└── README.md
```

> Update file names above to match the actual files in your repository.

---

## 🚀 Setup Guide

**Prerequisites:** Python 3.8+, MySQL Server, Power BI Desktop

```bash
# 1. Clone the repository
git clone https://github.com/onkartanpure3-ds/financial-performance-analytics-dashboard-main.git
cd financial-performance-analytics-dashboard-main

# 2. Install dependencies
pip install pandas pymysql
```

3. Run the SQL script in MySQL Workbench to create the database and tables.
4. Set your database host, user and password in the Python script, then run it to load the data.
5. Run the remaining SQL queries to clean the data and create the reporting view.
6. Open the `.pbix` file in Power BI Desktop, point it to your MySQL database, and click **Refresh**.

---

## 👤 Author

**Onkar Tanpure**
GitHub: [onkartanpure3-ds](https://github.com/onkartanpure3-ds)

Distributed under the MIT License.
