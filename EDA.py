#Importing libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv('Consumer Behavior.csv')

data.head()

data.shape

data.describe()

data.info()

data.nunique()
#See how many products in each department
product_count_per_department = data.groupby('department')['product_id'].nunique()

print(product_count_per_department)

#Display top products
orders = data['product_name'].value_counts()
top_products = orders.head(10)
top_products



# Display 
top_products.plot(kind='bar', title='Top 10 Most Popular Products (Total Orders)')
plt.xlabel('Product Name')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')
plt.show()



# Handle missing values
data['days_since_prior_order'].fillna(data['days_since_prior_order'].mean(), inplace=True)

# Analyze product frequency
product_counts = data['product_name'].value_counts()
print(product_counts)

sns.countplot(data=data, x='order_dow')
plt.title('Number of Orders by Day of the Week')
plt.show()

sns.scatterplot(data=data, x='order_hour_of_day', y='add_to_cart_order')
plt.title('Order Hour and Items Added to Cart')
plt.show()


sns.histplot(data=data, x='order_hour_of_day', bins=24, kde=True)
plt.title('Distribution of Orders by Hour of the Day')
plt.show()

# finding the relationship between the days of the week and the number of orders
plt.bar(data.groupby('order_dow').size().index, data.groupby('order_dow').size().values)
plt.title('The number of orders in each day of the week')
plt.xlabel('Days of the week')
plt.ylabel('Number of the orders')
plt.show()


df = data


# finding the relationship between the hours in a day and the number of orders
plt.bar(df.groupby('order_hour_of_day').size().index, df.groupby('order_hour_of_day').size().values)
plt.title('The number of orders in the hours of a day')
plt.xlabel('Hours of the day')
plt.ylabel('Number of the orders')
plt.show()

# Find the most popular departments  
counts = df[df['department'] != 'produce']['department'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=counts.index, y=counts.values)
plt.title('Most Popular Departments')
plt.xticks(rotation=90)
plt.show()


# The most reordered items
reordered_items = df[df['reordered'] == 1]

reorder_counts = reordered_items.groupby('product_name')['reordered'].count().reset_index()

reorder_counts = reorder_counts.sort_values(by='reordered', ascending=False)

top_reordered_items = reorder_counts.head(10)

plt.figure(figsize=(12, 8))
plt.barh(top_reordered_items['product_name'], top_reordered_items['reordered'], color='skyblue')
plt.xlabel('Number of Reorders')
plt.ylabel('Product Name')
plt.title('Top 10 Most Reordered Items')
plt.gca().invert_yaxis()  # To display the highest count at the top
plt.show()

# Determine users who reordered at least once
users_reordered = df.groupby('user_id')['reordered'].sum().reset_index()
users_reordered['reordered'] = users_reordered['reordered'] > 0

# Calculate proportions
reorder_counts = users_reordered['reordered'].value_counts()

# Plot the pie chart
labels = ['Reordered', 'Did not reorder']
colors = ['skyblue', 'lightcoral']
plt.figure(figsize=(8, 8))
plt.pie(reorder_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Users Who Reordered')
plt.show()