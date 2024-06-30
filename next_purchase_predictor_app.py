def get_product_name(user_id):
    try:
        user_id = int(user_id)
        user_data = df[df['user_id'] == user_id]
        product_name = user_data['product_name'].values[0]
        return f"User {user_id} will purchase {product_name} next"
    except (ValueError, IndexError):
        return "Invalid User ID"

def main():
    while True:
        user_id = input("Enter User ID (or 'exit' to quit): ")
        if user_id.lower() == 'exit':
            break
        result = get_product_name(user_id)
        print(result)

if __name__ == "__main__":
    main()
    