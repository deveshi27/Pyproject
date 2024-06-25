import csv
import getpass

# Initialize CSV files for user credentials and financial data
users_file = 'users.csv'
finance_file = 'finance.csv'

def initialize_files():
    # Initialize users file
    with open(users_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Password'])
    
    # Initialize finance file
    with open(finance_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Category', 'Amount'])

# Call the function to initialize files
initialize_files()

def create_user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    
    # Check if user already exists
    with open(users_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print("Username already exists. Try another one.")
                return
    
    # Add new user
    with open(users_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("User created successfully!")

    create_user()

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    with open(users_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return True
    print("Login failed!")
    return False
login()
def add_record(record_type):
    category = input(f"Enter the {record_type} category: ")
    amount = float(input(f"Enter the {record_type} amount: "))
    
    with open(finance_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([record_type, category, amount])
    print(f"{record_type.capitalize()} added successfully!")

def view_records():
    with open(finance_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"{row[0].capitalize()}: {row[1]} - ${row[2]}")

def summarize_finances():
    total_income = 0
    total_expenses = 0
    
    with open(finance_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == 'income':
                total_income += float(row[2])
            elif row[0] == 'expense':
                total_expenses += float(row[2])
    
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Net Savings: ${total_income - total_expenses}")

def main():
    if login():
        while True:
            print("\n1. Add Income")
            print("2. Add Expense")
            print("3. View Records")
            print("4. Summarize Finances")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                add_record('income')
            elif choice == '2':
                add_record('expense')
            elif choice == '3':
                view_records()
            elif choice == '4':
                summarize_finances()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
