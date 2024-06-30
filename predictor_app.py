import csv

def find_product_name(user_id, csv_file):

  try:
    with open(csv_file, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[0] == user_id:  
          return row[2] 
      return "Product not found"
  except FileNotFoundError:
    print(f"Error: CSV file '{csv_file}' not found.")
    return None

def main():

  csv_file = "user_product_predictions4.csv"  

  while True:
    user_id = input("Enter user ID: ")
    if user_id.lower() == 'q':
      break

    product_name = find_product_name(user_id, csv_file)
    if product_name:
        print(f"The User '{user_id}' will purchase '{product_name}' next.")
    else:
        print(f"Product not found for user ID '{user_id}'.")

if __name__ == "__main__":
  main()