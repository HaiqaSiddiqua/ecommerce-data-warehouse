# ecommerce-data-warehouse
Centralized analytical system for UK-based e-commerce data
# E-commerce Retail Data Warehouse

## Project Overview
The **E-commerce Retail Data Warehouse Project** aims to design and implement a centralized analytical system for online retail operations. Using a UK-based e-commerce dataset as the primary source, transactional, customer, and product data were extracted, transformed, and loaded (ETL) into **BigQuery** to support fast, reliable, and scalable business insights. 

The data warehouse integrates information from multiple heterogeneous sources, including three OLTP systems (sales, customers, and products) and several external flat files simulating API feeds such as exchange rates, holiday calendars, customer feedback, website traffic, and shipping data.

The data was modeled using a **Star Schema architecture** comprising multiple dimension tables (`Customer`, `Product`, `Holiday`, `Shipping`, `Traffic`, `Exchange Rate`) linked to a central `FactSales` table. Each dataset was cleaned, validated, and enriched using **Python** and **Faker** to ensure data accuracy, consistency, and completeness. The design emphasizes scalability, automation, and flexibility for future analytical extensions, including sales forecasting, customer segmentation, and anomaly detection.

Through this implementation, the warehouse enables comprehensive performance tracking such as total sales, customer engagement, top-performing products, and region-wise revenue trends. The BI-ready model supports visualization in **Power BI**, providing interactive dashboards for real-time, data-driven decision-making. Overall, the project demonstrates the complete data warehousing lifecycle, from multi-source integration and ETL to analytical modeling, validation, and visualization.

---

## Tech Stack
- **BigQuery** – Data warehousing and analytics  
- **Python** – ETL, data cleaning, and enrichment  
- **Faker** – Synthetic data generation  
- **Power BI** – Data visualization and dashboards  
- **CSV / Flat Files** – Sample external data sources  

---

## Repository Structure
