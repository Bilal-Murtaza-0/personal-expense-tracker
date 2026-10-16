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
    Transaction ID:{self.transaction_id},\n 
    Amount: {self.amount},\n 
    Category: {self.category},\n 
    Date: {self.date},\n
    Description: {self.description},\n
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
    
    transaction = next((t for t in self.transactions if t.transaction_id == transaction_id),None)
    if transaction is not None:
      return transaction
    else:
      print("Transaction not Found!")
      return None
  
  def update_transaction(self):
    user_input = input("""Enter your choice below: 
    1. Update amount
    2. Update category
    3. Update date
    4. Update description
    5. Update transaction type
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
      else:
        print("Transaction not found!")
    elif user_input == "2":
      transaction = self.search_transaction()
      if transaction is not None:
          category = input("Enter the new category: ").strip()
          if category != "":
           transaction.category = category
           print("Category updated successfully!")
          else: 
            print("Category cannot be empty!")
      else:
        print("Transaction not found!")
      
    elif user_input == "3":
      transaction = self.search_transaction().strip()
      if transaction is not None:
        date = input("Enter the date: ")
        if date != "":
          transaction.date = date
          print("Date updated successfully!")
          
      
  
    
  
  






