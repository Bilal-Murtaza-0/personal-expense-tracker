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
