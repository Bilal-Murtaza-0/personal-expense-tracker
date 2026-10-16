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
  
  






