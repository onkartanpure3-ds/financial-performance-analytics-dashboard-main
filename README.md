# 📊 Financial Performance Analytics Dashboard

An end-to-end analytics project that turns raw financial transaction data into clean SQL tables and an interactive **Power BI** dashboard for tracking revenue, profit, products, and discount impact.

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
- [Key Metrics](#-key-metrics)
- [Key Insights](#-key-insights)
- [Project Workflow](#-project-workflow)
- [Repository Structure](#-repository-structure)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 📌 Project Overview

Businesses collect large amounts of sales data, but it only becomes useful when it is cleaned, analysed, and visualised. This project answers questions such as:

- How much revenue and profit are we generating?
- Which segments, countries, and products perform best?
- How do discounts affect profit margins?

The pipeline covers data ingestion (Python), storage and analysis (MySQL), and reporting (Power BI).

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Data Preparation | Python, Pandas | Clean headers, handle nulls, format data types |
| Database | MySQL | Store data, remove duplicates, run analytical queries |
| Visualisation | Microsoft Power BI | Interactive 3-page dashboard |

---

## 📈 Dashboard Pages

### 1. Executive Overview

![Overview Dashboard](screenshots/overview.jpeg)

A high-level view of overall financial health.

- 📊 **KPI Cards:** Total Profit (15.45M), Total Revenue (112.47M), Profit Margin (13.74%), Total Units Sold (1,067,593)
- 📈 **Monthly Revenue Trend:** Revenue stays steady for most of the year and **peaks in October (~20M)**, showing strong seasonal demand
- 🏢 **Revenue by Segment:** Government (46M) and Small Business (42M) lead, followed by Enterprise (20M); Midmarket and Channel Partners contribute ~2M each
- 🌍 **Revenue by Country:** Waterfall chart showing each country's contribution (USA, Germany, Canada, France, Mexico) to total revenue
- 🔍 **Slicers:** Filter by Segment and Year (2013, 2014)

---

### 2. Product Performance

![Product Performance Dashboard](screenshots/product-performance.jpeg)

Shows which products drive profit and which need pricing attention.

- 📦 **KPI Cards:** 6 Total Products, 15.45M Total Profit, 2.58M Avg Profit per Product, Top Product: **Paseo**
- 🏆 **Profit by Product:** Paseo (4.1M) > VTT (3.0M) > Amarilla (2.7M) > Montana (2.1M) > Velo (2.0M) > Carretera (1.6M)
- 🔵 **Profitability Analysis:** Scatter plot of units sold vs profit
- 📊 **Revenue vs Profit:** Compares sales and profit for every product
- 📋 **Profitability Matrix:** Sales, profit, units, and margin per product. **Amarilla** has the best margin (15.67%); **Velo** has the lowest (12.14%)
- 🔍 **Slicers:** Product, Segment, and Year

---

### 3. Discount Impact Analysis

![Discount Analysis Dashboard](screenshots/discount-analysis.jpeg)

Explains how discount levels affect sales volume and profitability.

- 💰 **KPI Cards:** Discount Revenue (105.10M), Profit After Discount (15.45M), Avg Discount Impact (1.62K), Profit Margin (13.74%)
- 📉 **Profit Margin by Discount Level:** Margin falls as discounts rise

| Discount Band | Profit Margin | Units Sold |
|---|---|---|
| None | 21.44% | 82,753 |
| Low | 17.33% | 254,427 |
| Medium | 13.97% | 345,452 |
| High | 8.68% | 384,961 |

- 📊 **Revenue & Profit by Discount Band** and **Units Sold by Discount Level** compare volume against profit for each band
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
- 🏛️ **Government** and **Small Business** segments generate the most revenue.
- 🥇 **Paseo** is the top product in both revenue and profit.
- ⚠️ Lower-margin products (e.g., Velo, Carretera) need **pricing optimisation**.
- 🏷️ **High discounts** increase sales volume but cut margins to 8.68%.
- ✅ **Medium/Low discounts** give a better balance of revenue and profit.

---

## 🏗️ Project Workflow

1. **Source Data:** Raw financial sales CSV file
2. **Python Ingestion:** Clean column names, handle nulls, load into MySQL
3. **MySQL Processing:** Check data quality, remove duplicates (`ROW_NUMBER()`), create a reporting view
4. **Power BI:** Connect to the database and build the 3-page interactive dashboard
5. **Insights:** Use slicers and charts to support business decisions

---

## 📁 Repository Structure

```text
financial-performance-analytics-dashboard/
│
├── dataset/                              # Source CSV data
├── screenshots/
│   ├── overview.jpeg                     # Dashboard page 1
│   ├── product-performance.jpeg          # Dashboard page 2
│   └── discount-analysis.jpeg            # Dashboard page 3
├── financial_data_analysis.sql           # Table creation, cleaning, KPI queries
├── load_data.py                          # Python ingestion script
├── Financial_Performance_Dashboard.pbix  # Power BI dashboard file
└── README.md
```

> Update file names above if they differ in your repository.

---

## 🚀 How to Run

**Prerequisites:** Python 3.8+, MySQL Server, Power BI Desktop

```bash
# 1. Clone the repository
git clone https://github.com/onkartanpure3-ds/financial-performance-analytics-dashboard-main.git
cd financial-performance-analytics-dashboard-main

# 2. Install dependencies
pip install pandas pymysql

# 3. Set up the database: run the table-creation steps in financial_data_analysis.sql

# 4. Load the data (update DB credentials in the script first)
python load_data.py

# 5. Run the remaining SQL queries to create the cleaned table and reporting view
```

6. Open the `.pbix` file in **Power BI Desktop**, point the data source to your MySQL database, and click **Refresh**.

> 🔒 Never commit database passwords. Use environment variables instead.

---

## 👤 Author

**Onkar Tanpure**
GitHub: [@onkartanpure3-ds](https://github.com/onkartanpure3-ds)

---

## 📜 License

Distributed under the MIT License.
