# 📊 Financial Performance Analytics Dashboard

An end-to-end analytics project that turns raw financial sales data into clean SQL tables and a 3-page interactive **Power BI** dashboard for tracking revenue, profit, product performance, and discount impact.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
</p>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Tech Stack](#️-tech-stack)
- [Dashboard Pages](#-dashboard-pages)
- [Key Metrics](#-key-metrics)
- [Key Insights](#-key-insights)
- [Repository Structure](#-repository-structure)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 📌 Project Overview

Businesses collect large amounts of sales data, but it only becomes useful once it is cleaned, analysed, and visualised. This project answers:

- How much revenue and profit are we generating?
- Which segments, countries, and products perform best?
- How do discounts affect profit margins?

---

## 🏗️ Architecture

![Architecture](Financial%20Analytics%20Dashboard%20Architecture.png)

**Flow:** CSV dataset → Python (clean & load) → MySQL (validate, de-duplicate, reporting view) → Power BI (dashboard)

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Data Preparation | Python, Pandas, PyMySQL | Clean column names, handle nulls, load data into MySQL |
| Database | MySQL | Validate data, remove duplicates, run KPI queries, create reporting view |
| Visualisation | Microsoft Power BI | Interactive 3-page dashboard |

---

## 📈 Dashboard Pages

### 1. Executive Overview

![Dashboard Overview](Dashboard%20Overview.jpeg)

A high-level view of overall financial health.

- 📊 **KPI Cards:** Total Profit (15.45M), Total Revenue (112.47M), Profit Margin (13.74%), Total Units Sold (1,067,593)
- 📈 **Monthly Revenue Trend:** Steady through most of the year and **peaks in October (~20M)**, showing seasonal demand
- 🏢 **Revenue by Segment:** Government (46M) and Small Business (42M) lead, then Enterprise (20M); Midmarket and Channel Partners ~2M each
- 🌍 **Revenue by Country:** Waterfall chart of each country's contribution (USA, Germany, Canada, France, Mexico)
- 🔍 **Slicers:** Segment and Year (2013, 2014)

---

### 2. Product Performance

![Product Performance](Product%20Performance.jpeg)

Shows which products drive profit and which need pricing attention.

- 📦 **KPI Cards:** 6 Total Products, 15.45M Total Profit, 2.58M Avg Profit per Product, Top Product: **Paseo**
- 🏆 **Profit by Product:** Paseo (4.1M) > VTT (3.0M) > Amarilla (2.7M) > Montana (2.1M) > Velo (2.0M) > Carretera (1.6M)
- 🔵 **Profitability Analysis:** Scatter plot of units sold vs profit
- 📊 **Revenue vs Profit:** Sales and profit side by side for every product
- 📋 **Profitability Matrix:** Sales, profit, units, and margin per product. **Amarilla** has the best margin (15.67%); **Velo** the lowest (12.14%)
- 🔍 **Slicers:** Product, Segment, and Year

---

### 3. Discount Impact Analysis

![Discount Analysis](DIscount%20Analysis.jpeg)

Explains how discount levels affect sales volume and profitability.

- 💰 **KPI Cards:** Discount Revenue (105.10M), Profit After Discount (15.45M), Avg Discount Impact (1.62K), Profit Margin (13.74%)
- 📉 **Profit Margin by Discount Level:** Margin falls as discounts rise

| Discount Band | Profit Margin | Units Sold |
|---|---|---|
| None | 21.44% | 82,753 |
| Low | 17.33% | 254,427 |
| Medium | 13.97% | 345,452 |
| High | 8.68% | 384,961 |

- 📊 **Revenue & Profit by Discount Band** and **Units Sold by Discount Level** compare volume against profit
- 🔍 **Slicers:** Segment, Year, and Country

---

## 💡 Key Metrics

| Metric | Value |
|---|---|
| Total Revenue | 112.47M |
| Total Profit | 15.45M |
| Profit Margin % | 13.74% (`Profit / Sales × 100`) |
| Total Units Sold | 1,067,593 |
| Avg Discount Impact | 1.62K |

---

## 🔎 Key Insights

- 📅 Revenue peaks in **October**, indicating strong seasonal demand.
- 🏛️ **Government** and **Small Business** generate the most revenue.
- 🥇 **Paseo** is the top product in both revenue and profit.
- ⚠️ Lower-margin products (**Velo**, **Carretera**) need pricing optimisation.
- 🏷️ **High discounts** boost sales volume but cut margin to 8.68%.
- ✅ **Low/Medium discounts** give a better balance of revenue and profit.

---

## 📁 Repository Structure

```text
financial-performance-analytics-dashboard-main/
│
├── dataset/
│   └── Financial_Sample_dataset.csv          # Source data
├── Dashboard Overview.jpeg                   # Dashboard page 1
├── Product Performance.jpeg                  # Dashboard page 2
├── DIscount Analysis.jpeg                    # Dashboard page 3
├── Financial Analytics Dashboard Architecture.png
├── financial_data_analysis.sql               # Table creation, cleaning, KPI queries, reporting view
├── load_data.py                              # Python ingestion script
├── Financial_Performance_Dashboard.pbix      # Power BI dashboard file
└── README.md
```

---

## 🚀 How to Run

**Prerequisites:** Python 3.8+, MySQL Server, Power BI Desktop

```bash
# 1. Clone the repository
git clone https://github.com/onkartanpure3-ds/financial-performance-analytics-dashboard-main.git
cd financial-performance-analytics-dashboard-main

# 2. Install dependencies
pip install pandas pymysql
```

3. In MySQL, run **Steps 1–2** of `financial_data_analysis.sql` to create the `financialanalyticsdb` database and the `financial_data` table.
4. Set your MySQL credentials in `load_data.py`, then load the data:
   ```bash
   python load_data.py
   ```
5. Run the **remaining SQL steps** to validate data, remove duplicates (`ROW_NUMBER()`), create the `financial_cleaned` table, and create the `financial_dashboard_view`.
6. Open `Financial_Performance_Dashboard.pbix` in **Power BI Desktop**, point the data source to your MySQL database, and click **Refresh**.

> 🔒 Never commit database passwords. Read them from environment variables instead.

---

## 👤 Author

**Onkar Tanpure**
GitHub: [@onkartanpure3-ds](https://github.com/onkartanpure3-ds)

---

## 📜 License

Distributed under the MIT License.
