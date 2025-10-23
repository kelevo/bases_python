class BankAccount:
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance
    self.is_active = True

  def deposit(self, amount):
    if self.is_active:
      self.balance += amount
      print(f"Depósito de {amount} realizado. Nuevo saldo: {self.balance}")
    else:
      print("La cuenta está inactiva. No se pueden realizar depósitos.")

  def withdraw(self, amount):
    if self.is_active:
      if amount <= self.balance:
        self.balance -= amount
        print(f"Retiro de {amount} realizado. Nuevo saldo: {self.balance}")
      else:
        print("Fondos insuficientes para el retiro.")
    else:
      print("La cuenta está inactiva. No se pueden realizar retiros.")

  def deactivate_account(self):
    self.is_active = False
    print("La cuenta ha sido desactivada.")

  def activate_account(self):
    self.is_active = True
    print("La cuenta ha sido activada.")

account1 = BankAccount("Carlos", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.deactivate_account()
account1.deposit(300)
account1.activate_account()
account1.withdraw(1500)

account2 = BankAccount("María", 2000)
account2.withdraw(250)
account2.deposit(1000)
account2.deactivate_account()
account2.withdraw(100)