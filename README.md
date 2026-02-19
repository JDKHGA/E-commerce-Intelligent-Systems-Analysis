# E-commerce Intelligent Systems Analysis

**Author:** John Deladem Kpormegbe  
**Assignment:** Analyzing Customer Behavior for E-commerce Insights 

## 📋 Project Overview
This project analyzes customer behavior on an e-commerce platform to extract actionable insights for improving sales and engagement. It demonstrates a full data science workflow, including:
*   **Synthetic Data Generation:** Creating a realistic dataset of customers and transactions.
*   **Data Analysis & Cleaning:** preparing data for modeling.
*   **Feature Engineering:** Creating meaningful features like Customer Lifetime Value (CLV) and time-based metrics.
*   **Predictive Modeling:** Using a Random Forest Classifier to predict product category preferences.
*   **Big Data Simulation:** Simulating a real-time data stream using **Apache Kafka** and **Docker**.

## 🛠️ Tech Stack
*   **Language:** Python 3.9+
*   **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
*   **Big Data Tools:** Apache Kafka, Zookeeper, Docker
*   **Environment:** Jupyter Notebook

## 📂 Project Structure
*   `analysis.ipynb`: The main Jupyter Notebook containing the data generation, analysis, modeling, and visualization.
*   `Project_Report.md`: A detailed report of methodologies, insights, and business recommendations.
*   `stream_simulation.py`: A Python script that acts as a Kafka producer, simulating real-time transaction events.
*   `docker-compose.yml`: Configuration to run Apache Kafka and Zookeeper in Docker containers.
*   `main.py`: A CLI dashboard to easily check project status and run simulations.
*   `requirements.txt`: List of Python dependencies.

## 🚀 How to Run the Project

### 1. Prerequisites
*   Python 3.8 or higher
*   Docker Desktop (for the big data simulation)

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
```

### 3. Running the Analysis
Open the Jupyter Notebook to view the code, visualizations, and model training:
```bash
jupyter notebook analysis.ipynb
```
Run all cells from top to bottom to generate the dataset (`ecommerce_data.csv`) and perform the analysis.

### 4. Running the Big Data Simulation (Kafka)
To demonstrate real-time data handling:

1.  **Start Kafka:** Ensure Docker Desktop is running, then run:
    ```bash
    docker-compose up -d
    ```
2.  **Run the Stream:** Execute the simulation script:
    ```bash
    python stream_simulation.py
    ```
    You will see transaction events being generated and sent to the Kafka topic `ecommerce_transactions` in real-time.

3.  **Stop Kafka:** When finished, clean up resources:
    ```bash
    docker-compose down
    ```

### 5. Using the Main Menu
For convenience, you can use the main entry point script:
```bash
python main.py
```
This provides an interactive menu to check file status and run the simulation.

## 📊 Key Insights
*   **Time Matters:** The model identified `hour_of_day` as a key predictor for purchase behavior.
*   **Seasonality:** Sales show distinct monthly trends that can be targeted with specific marketing campaigns.
*   **Demographics:** The 25-40 age group represents the core customer base.

