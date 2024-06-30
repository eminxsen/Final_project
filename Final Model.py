#Importing libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from catboost import CatBoostClassifier
import lightgbm as lgb



# Create user and product specific features
user_features = data.groupby('user_id').agg({
    'order_number': 'max',
    'days_since_prior_order': 'mean'
}).reset_index()

product_features = data.groupby('product_id').agg({
    'reordered': 'mean',
    'add_to_cart_order': 'mean'
}).reset_index()

# Merge features with the main data
data = data.merge(user_features, on='user_id', suffixes=('', '_user'))
data = data.merge(product_features, on='product_id', suffixes=('', '_product'))

# Prepare features and target
features = ['order_dow', 'order_hour_of_day', 'days_since_prior_order', 'add_to_cart_order', 
            'order_number_user', 'days_since_prior_order_user', 'reordered_product', 'add_to_cart_order_product']
X = data[features]
y = data['is_reordered']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))


def predict_next_products(user_id, model, data, features):
    # Get data for the specific user
    user_data = data[data['user_id'] == user_id]

    # Predict probabilities
    user_data['prediction'] = model.predict_proba(user_data[features])[:, 1]

    # Get top 5 product predictions
    top_products = user_data.sort_values('prediction', ascending=False).head(2)['product_id']
    return top_products

# Predict top 5 products for user 49125
user_id = 49125
top_products = predict_next_products(user_id, model, data, features)
print(f"Top products for user {user_id}: {top_products}")

# Map product IDs to product names
product_names = data.set_index('product_id')['product_name'].to_dict()
top_product_names = [product_names[prod_id] for prod_id in top_products]
print(f"Top product names for user {user_id}: {top_product_names}")

# Generate predictions for all users
all_users = data['user_id'].unique()
predictions = []

for user_id in all_users:
    top_products = predict_next_products(user_id, model, data, features)
    for product_id in top_products:
        predictions.append({'user_id': user_id, 'product_id': product_id})

# Create DataFrame for predictions
predictions_df = pd.DataFrame(predictions)

# Map product IDs to product names
product_names = data.set_index('product_id')['product_name'].to_dict()
predictions_df['product_name'] = predictions_df['product_id'].map(product_names)

# Save predictions to CSV
predictions_df.to_csv('user_product_predictions.csv4', index=False)

print("Predictions saved to user_product_predictions.csv")