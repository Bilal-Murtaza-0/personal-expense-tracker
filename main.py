
class Transaction:
    def __init__(self, transaction_id, amount, category, date, description, transaction_type):
        self.transaction_id = transaction_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.transaction_type = transaction_type

    def display(self):
        print(f"""
Transaction ID: {self.transaction_id}
Amount: {self.amount}
Category: {self.category}
Date: {self.date}
Description: {self.description}
Transaction Type: {self.transaction_type}""")


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_all_transactions(self):
        if len(self.transactions) >= 1:
            for trans in self.transactions:
                trans.display()
        else:
            print("No transactions found!")

    def search_transaction(self):
        transaction_id = input("Enter Transaction ID: ")

        transaction = next(
            (t for t in self.transactions
             if t.transaction_id == transaction_id),
            None
        )

        if transaction is not None:
            return transaction
        else:
            print("Transaction not found!")
            return None
            
    def delete_transaction(self):
        transaction = self.search_transaction()

        if transaction is not None:
            self.transactions.remove(transaction)
            print("Transaction removed successfully!")
            
    def calculate_totals(self):
        self.total_income = 0
        self.total_expense = 0

        if self.transactions:
            for trans in self.transactions:
                if trans.transaction_type == "income":
                   self.total_income += trans.amount  
                elif trans.transaction_type == "expense":
                    self.total_expense += trans.amount
                    
            net_balance = self.total_income - self.total_expense
            
            print(f"Total Income: {self.total_income}")
            print(f"Total Expense: {self.total_expense}")
            print(f"Net Balance: {net_balance}")
            
        else:
            print("No transactions found!")
        
    def filter_by_type(self):
        transaction_type = input("Enter the transaction type: ").strip().lower()

        for trans in self.transactions: 
            if transaction_type == trans.type:
                trans.display()
            else:
                print("No matching transactions were foun!")
            
                

    
    def update_transaction(self):
        user_input = input("""Enter your choice below:
1. Update amount
2. Update category
3. Update date
4. Update description
5. Update transaction type
6. Delete the transaction
""")

        if user_input == "1":
            transaction = self.search_transaction()

            if transaction is not None:
                try:
                    amount = int(input("Enter the new amount: "))
                except ValueError:
                    print("Please enter a valid number!")
                    return

                if amount > 0:
                    transaction.amount = amount
                    print("Amount updated successfully!")
                else:
                    print("Amount must be greater than zero!")

        elif user_input == "2":
            transaction = self.search_transaction()

            if transaction is not None:
                category = input("Enter the new category: ").strip()

                if category != "":
                    transaction.category = category
                    print("Category updated successfully!")
                else:
                    print("Category cannot be empty!")

        elif user_input == "3":
            transaction = self.search_transaction()

            if transaction is not None:
                date = input("Enter the new date: ").strip()

                if date != "":
                    transaction.date = date
                    print("Date updated successfully!")
                else:
                    print("Date cannot be empty!")

        elif user_input == "4":
            transaction = self.search_transaction()

            if transaction is not None:
                description = input("Enter the new description: ").strip()

                if description != "":
                    transaction.description = description
                    print("Description updated successfully!")
                else:
                    print("Description cannot be empty!")

        elif user_input == "5":
            transaction = self.search_transaction()

            if transaction is not None:
                transaction_type = input(
                    "Enter the transaction type (income/expense): "
                ).strip().lower()

                if transaction_type == "":
                    print("Transaction type cannot be empty!")
                elif transaction_type not in ["income", "expense"]:
                    print("Invalid transaction type! Enter income or expense.")
                else:
                    transaction.transaction_type = transaction_type
                    print("Transaction type updated successfully!")

        elif user_input == "6":
            self.delete_transaction()
            
        else:
            print("Invalid choice!")

manager = TransactionManager()

t1 = Transaction("T101", 5000, "Salary", "2026-10-01", "Monthly salary", "income")
t2 = Transaction("T102", 1200, "Food", "2026-10-02", "Grocery shopping", "expense")
t3 = Transaction("T103", 800, "Transport", "2026-10-03", "Bus fare", "expense")

manager.add_transaction(t1)
manager.add_transaction(t2)
manager.add_transaction(t3)

print("All transactions before deletion:")
manager.display_all_transactions()

print("\nDelete an existing transaction:")
manager.delete_transaction()

print("\nTransactions after deletion:")
manager.display_all_transactions()
