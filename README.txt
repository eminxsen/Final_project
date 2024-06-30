Next Purchase Predictor
This project demonstrates how to predict the next product purchase for users using machine learning models. It involves data preprocessing, feature engineering, model training, and prediction generation.
Requirements
To run this project, you need:
* Python 3.x
* Libraries specified in requirements.txt
* Access to the dataset Consumer Behavior.csv
Installation
Clone the repository:

git clone https://github.com/eminxsen/Final_project


Install dependencies:


!pip install catboost
!pip install lightgbm



Usage
Step-by-Step Guide
1. Data Exploration and Visualization:
   * Import necessary libraries.
   * Load and inspect the dataset using pandas.
   * Explore data characteristics (shape, description, info, unique values).
   * Visualize product popularity and other insights using matplotlib and seaborn.
2. Data Preprocessing:
   * Handle missing values, if any.
   * Perform feature engineering to create user-specific and product-specific features.
3. Model Training:
   * Split the data into training and testing sets.
   * Train machine learning models (RandomForestClassifier, CatBoostClassifier, LGBMClassifier).
4. Model Evaluation:
   * Evaluate model performance using classification metrics (classification_report).
5. Prediction Generation:
   * Implement functions to predict the next product purchases for users based on trained models.
   * Save predictions to CSV files (user_product_predictions.csv, user_product_predictions2.csv, etc.).
6. Running the App:
* Execute predictor.py to predict the next purchase for a user based on the generated predictions (user_product_predictions4.csv).