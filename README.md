# Data Analysis with AIC | PURE 2022

# Data Analysis and Linear Regression with AIC

This repository contains Python scripts for data analysis and linear regression using the Akaike Information Criterion (AIC) for model selection. It also includes a simple linear regression analysis of a dataset. Let's explore the contents and how to use these scripts.

## Contents

### `computingAIC.py`

#### `computeAIC(X, Y, k=2)`

This function calculates the AIC (Akaike Information Criterion) for a linear regression model.

- `X`: The feature matrix (independent variables).
- `Y`: The target variable (dependent variable).
- `k`: The penalty term for model complexity (default is 2).

#### `stepAIC(X, Y, features, AIC=True)`

This function performs stepwise selection of features using AIC.

- `X`: The feature matrix (independent variables).
- `Y`: The target variable (dependent variable).
- `features`: List of feature column names.
- `AIC`: If `True`, uses AIC for model selection (default). If `False`, uses BIC (Bayesian Information Criterion).

### `linearregressionalanalysis.py`

This script performs a simple linear regression analysis on a dataset.

1. Loads the dataset from an Excel file (`puredataset.csv`).
2. Prepares the data, handles missing values, and separates features and the target variable.
3. Splits the data into training and testing sets.
4. Fits a linear regression model to the data.
5. Makes predictions and visualizes the results.

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/data-analysis-using-Akaike-Information-Criterion.git
cd data-analysis-using-Akaike-Information-Criterion
```

2. Make sure you have the required Python dependencies installed (NumPy, pandas, sklearn, matplotlib, scipy, seaborn). You can install them using pip.

3. Run the scripts as needed:

For AIC-based feature selection, use computingAIC.py.
For simple linear regression analysis, use linearregressionalanalysis.py.

## Akaike Information Criterion (AIC) in Machine Learning
The Akaike Information Criterion (AIC) is a measure of the goodness of fit of a statistical model. It balances the quality of the model's fit to the data with the complexity of the model. Lower AIC values indicate better models. In the context of linear regression:

AIC accounts for the model's ability to explain the variance in the data.
It penalizes models with more parameters to prevent overfitting.
A lower AIC suggests a more parsimonious model that fits the data well.




![Slide1 2](https://github.com/asmita002/data-analysis-using-Akaike-Information-Criterion/assets/97020024/4d5927f4-9f69-4cf7-9fc5-09f86a919747)
