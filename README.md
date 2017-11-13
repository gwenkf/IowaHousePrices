# IowaHousePrices
The following repository contains code for predicting house prices in Ames, Iowa from the Kaggle Competition: https://www.kaggle.com/c/house-prices-advanced-regression-techniques

python codes:
boxcoxplot.py - boxcox transformation and visualization function for feature engineering
outliers.py - function that detects outliers used in feature engineering

The following is a description of each folder in the repository:

## Feature Engineering
There are two parts: the first python notebook is only from one hot encoding variables and the second feature engineering file is for label encoding of categorical variables.

## Data
The Data folder contains both featured engineered data sets:
1. train_x.csv, train_y.csv, and text_x.csv all correspond to the first feature engineering notebook: FeatureEngineeringRound1.ipynb
2. train_x2.csv, train_y2.csv, and text_x2.csv all correspond to the second feature engineering notebook: FeatureEngineeringRound2.ipynb

The best scoring Kaggle predictions are in this folder as well called:
1. Final_Prediction_1.csv - Prediction run from Elastic Net and SVR Average. Scored 0.1169 on Public Leaderboard
2. Final_PredictionBestScore.csv - Prediction run from weighted average of Elastic Net, SVR, KRR, and GBR Scored 0.1154 on Public Leaderboard which was in the top 9%

## Individual Model Predictions
In this folder each model prediction was ran in a separate ipython notebook listed by title:
1. Lin_Reg_nb.ipynb - all linear regression model hyper parameter tuning and predictions: Ridge, Elastic Net, Lasso, and Kernel Ridge Regression
2. RandomForest.ipynb - random forest model tuning and prediction
3. SVR.ipynb - support vector regression model hyper parameter tuning and predictions
4. Boosting Models.ipynb -  gradient boosting tree model hyper parameter tuning and predictions

## Ensembling Predictions
1. Ensembling_v1.ipynb -  ensembling Averaged and Stacking models for feature engineering notebook: FeatureEngineeringRound1.ipynb
2. Ensembling_v2.ipynb -  ensembling Averaged and Stacking models for feature engineering notebook: FeatureEngineeringRound2.ipynb
3. Ensembling_Weighted_Averages.ipynb - "Kaggle Hacking" average weight ensembling method

## Data Visualizations and testing
This folder is an extra folder containing extra EDA and Data visualizations
