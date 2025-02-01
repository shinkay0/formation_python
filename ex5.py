
class NegativeAmountError(Exception):
  pass

class InsufficientBalanceError(Exception):
  pass
 
class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    try:
      if amount < 0:
        raise NegativeAmountError("Le montant ne peut pas être négatif")
      else:
        self.balance += amount
    except NegativeAmountError as e:
      print(e)


  def draw(self , amount):
    try:
      if amount > self.balance:
        raise InsufficientBalanceError("Solde insuffisant")
      
      if amount < 0:
        raise NegativeAmountError("Le montant ne peut pas être négatif")
      else:
        self.balance -= amount

    except (NegativeAmountError, InsufficientBalanceError) as e:
      print(e)

        
  def show(self):
    print(f"\nVotre solde est de {self.balance}€")

account = BankAccount("User1")

AGAIN = True

menu = """
1. Déposer de l'argent
2. Retirer de l'argent
3. Voir le solde
4. Quitter
"""

while AGAIN:
  print(menu)

  USER = int(input("Choisir une action : "))

  if USER == 1:
    amount = int(input("Entrer le montant du dépot : "))
    account.deposit(amount)

  if USER == 2:
    amount = int(input("Entrer le montant du retrait : "))
    account.draw(amount)

  if USER == 3:
    account.show()

  if USER == 4:
    AGAIN = False