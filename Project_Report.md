# Project Report: E-commerce Intelligent Systems Analysis

**Author:** John Deladem Kpormegbe

**Date:** 19/02/2026

**Assignment:** Intelligent Systems and Security Officer (Data Science & Analytics)

---


## 1. Executive Summary
This project analyzes customer behavior on an e-commerce platform to extract actionable insights for improving sales and engagement. Using a synthetic dataset simulating 2,000 customers and 1,000 transactions, we developed a data processing pipeline that includes data cleaning, feature engineering, and predictive modeling. Additionally, a real-time big data streaming architecture was simulated using Apache Kafka and Docker.

## 2. Methodology

### 2.1 Data Generation & Processing
*   **Synthetic Data:** We generated a realistic dataset using `numpy` and `pandas` to simulate customer demographics (Age, Gender, Location), product details (Category, Price), and transactional history (Timestamp, Quantity).
*   **Data Cleaning:** The raw data was inspected for missing values and duplicates. Timestamps were converted to `datetime` objects to facilitate time-series analysis.
*   **Feature Engineering:** To enhance model performance, we engineered several features:
    *   **Temporal Features:** Extracted `hour_of_day`, `day_of_week`, and `month` to capture seasonal and daily trends.
    *   **Customer Profiling:** Calculated a proxy for Customer Lifetime Value (CLV) based on total historical spending.
    *   **Price Categorization:** Segmented products into 'Low', 'Medium', and 'High' price bins.

### 2.2 Predictive Modeling
*   **Goal:** Predict the **Product Category** a customer is likely to purchase based on their demographics and transaction time.
*   **Algorithm:** Random Forest Classifier (Ensemble Learning).
*   **Validation:** The data was split into 80% training and 20% testing sets. We evaluated the model using Accuracy Score and a Classification Report (Precision, Recall, F1-Score).

### 2.3 Big Data Architecture
To demonstrate readiness for high-velocity data environments, we implemented a streaming pipeline:
*   **Tool:** **Apache Kafka** (running via **Docker**).
*   **Implementation:** A Python producer script (`stream_simulation.py`) simulates a live feed of transaction events, serializing data into JSON and pushing it to a Kafka topic (`ecommerce_transactions`). This architecture allows for real-time analytics and decoupling of data sources from consumers.

---

## 3. Key Insights & Visualizations

Our analysis revealed several critical trends:

1.  **Sales Seasonality:**
    *   *Observation:* Sales volume fluctuates significantly by month.
    *   *Business Implication:* Marketing budgets should be allocated dynamically, with higher spend during identified peak months to maximize ROI.

2.  **Product Popularity:**
    *   *Observation:* Certain categories outperform others significantly in transaction volume.
    *   *Business Implication:* Inventory management should be optimized to prevent stockouts on high-velocity categories.

3.  **Demographic Targeting:**
    *   *Observation:* The age distribution of our customers shows a specific concentration (e.g., 25-40 demographic).
    *   *Business Implication:* Ad creatives and UI/UX design should be tailored to appeal to this primary age group.

4.  **Drivers of Purchase Behavior:**
    *   *Observation:* The Random Forest model identified `hour_of_day` and `age` as top predictors for product choice.
    *   *Business Implication:* **Time-based marketing is viable.** Sending push notifications or emails during peak active hours for specific demographics will likely increase conversion rates.

---

## 4. Business Recommendations

Based on the data analysis and modeling results, we recommend the following actions:

1.  **Implement Real-Time Personalization:** Utilize the Predictive Model to recommend products dynamically on the homepage based on the time of day and the user's demographic profile.
2.  **Dynamic Pricing & Promotions:** Launch "Happy Hour" flash sales during the specific hours identified as high-traffic but low-conversion to boost sales velocity.
3.  **Infrastructure Investment:** Continue scaling the Kafka pipeline to handle clickstream data (views, clicks) alongside transaction data, enabling a 360-degree view of the customer journey in real-time.
