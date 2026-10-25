# Smart Renewable Energy Forecasting Platform

A machine learning project for forecasting wind power output using meteorological and environmental features.

## Overview

This project explores regression-based approaches to renewable energy forecasting. It compares multiple machine learning algorithms and evaluates their ability to predict wind power output.

## Objectives

- Explore and prepare wind power data.
- Identify input features and the target variable.
- Train and compare regression models.
- Evaluate model performance using appropriate validation techniques.
- Investigate ensemble learning through bagging.

## Models Implemented

- Linear Regression
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN)
- Bagging Regressor

## Technology Stack

- Python
- Jupyter Notebook
- NumPy and Pandas
- Matplotlib and Seaborn
- Scikit-learn

## Project Structure

```text
smart-renewable-energy-forecasting/
├── notebooks/
│   └── model_comparison.ipynb
├── data/
├── results/
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-renewable-energy-forecasting.git
cd smart-renewable-energy-forecasting
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

Place the authorized dataset at the path expected by the notebook. The notebook currently references `wind_dataset.csv`.

### 5. Run the notebook

Open `notebooks/model_comparison.ipynb` in Jupyter Notebook or VS Code and execute the cells in order.

## Evaluation

The project uses cross-validation and train-test evaluation workflows to compare model performance. Final metrics and the best-performing model will be documented after validating the experiments.

## Future Improvements

- Add a reproducible preprocessing pipeline.
- Compare models using consistent evaluation metrics.
- Add visualizations of actual versus predicted power output.
- Investigate time-series-aware validation for forecasting.
- Build an interactive dashboard for predictions.

## Author

**Ravitej**

Computer Science Engineering — Artificial Intelligence and Machine Learning

## License

A license will be added after confirming the intended reuse permissions.
