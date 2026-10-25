# 🌬️ Smart Renewable Energy Forecasting Platform

### Machine Learning-Based Wind Power Prediction and Model Comparison

An end-to-end machine learning project designed to estimate wind power output using meteorological parameters and compare the performance of different regression and ensemble learning algorithms.

---

## 📌 Project Overview

Renewable energy forecasting plays an important role in modern energy planning and smart grid resource management. This project explores how machine learning can be applied to estimate wind power output from environmental parameters—including wind speed, atmospheric temperature, and relative humidity. 

The pipeline covers data preparation, exploratory data analysis (EDA), regression model training, cross-validation, and systematic performance comparison.

> **Note on Data:** Power output is calculated using a physical estimation method rather than being confirmed as measured electricity generation from an operational wind turbine.

---

## 🎯 Objectives

* Explore weather-based wind power estimation using physics-informed approximations.
* Analyze relationships between environmental parameters and power generation.
* Implement and benchmark multiple machine learning regression algorithms.
* Compare individual base models against bagging ensemble methods.
* Evaluate prediction performance using train-test splits and cross-validation.
* Establish a modular foundation for future renewable energy forecasting applications.

---

## 📊 Dataset Features

The dataset comprises the following variables retrieved via the NASA POWER API:

| Feature | Description | Unit |
| :--- | :--- | :--- |
| **Date** | Observation date/timestamp | `YYYY-MM-DD` |
| **Wind Speed** | Measured or retrieved wind speed | `m/s` |
| **Temperature** | Atmospheric temperature | `°C` |
| **Humidity** | Relative humidity | `%` |
| **Power Output** *(Target)* | Estimated wind power output | `kW` |

---

## 🤖 Machine Learning Models

The following regression and ensemble algorithms are implemented and evaluated:

1. **Linear Regression** (Baseline parametric model)
2. **Support Vector Regression (SVR)** (Kernel-based non-linear regression)
3. **Decision Tree Regressor** (Non-linear partitioning)
4. **Random Forest Regressor** (Ensemble of randomized decision trees)
5. **K-Nearest Neighbors (KNN) Regressor** (Instance-based learning)
6. **Bagging Regressor** (Variance reduction with diverse base estimators)

---

## ⚙️ Methodology

```text
Data Collection (NASA POWER API) 
       ↓
Data Preprocessing & Cleaning
       ↓
Feature Selection & Scaling
       ↓
Model Training (80:20 Train-Test Split)
       ↓
Cross-Validation & Benchmark Comparison
       ↓
Model Evaluation (RMSE, MAE, R² Score)
```

---

## 🛠️ Technology Stack

* **Programming Language:** Python 3.x
* **Development Environment:** Jupyter Notebook / Visual Studio Code
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn, Joblib
* **Data Visualization:** Matplotlib, Seaborn
* **Data Retrieval:** Requests, NASA POWER API

---

## 📁 Project Structure

```text
smart-renewable-energy-forecasting/
├── notebooks/
│   └── model_comparison.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd smart-renewable-energy-forecasting
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate the Environment
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux (Bash/Zsh):**
  ```bash
  source .venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Prepare the Dataset
Place your generated `wind_dataset.csv` file inside the expected working directory or update the file path inside `notebooks/model_comparison.ipynb` before running the execution cells.

### 6. Run the Notebook
Launch Jupyter Notebook or open the workspace in VS Code:
```bash
jupyter notebook notebooks/model_comparison.ipynb
```
Execute the cells sequentially from top to bottom.

---

## 📈 Model Evaluation

The pipeline evaluates and compares models using cross-validation and out-of-sample testing metrics (such as R², RMSE, and MAE). 

*Detailed comparative metrics and residual plots will be populated directly inside the notebook after running the experimental suite.*

---

## 🔮 Future Enhancements

* [ ] Implement **time-series-aware cross-validation** (e.g., TimeSeriesSplit) to prevent data leakage.
* [ ] Perform systematic **hyperparameter tuning** using GridSearchCV / RandomizedSearchCV.
* [ ] Develop an **interactive prediction dashboard** via Streamlit or Dash.
* [ ] Integrate live, real-time meteorological data streams.
* [ ] Extend validation to real-world SCADA data from actual wind turbines.

---

## 👨‍💻 Author

**Ravitej Jadar**  
Computer Science Engineering — Artificial Intelligence & Machine Learning  
**Dayananda Sagar University**  

* **Project Domain:** Machine Learning | Renewable Energy | Predictive Analytics
