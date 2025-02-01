def add_contact(contacts):
    contact = input("Entrer le nom du contact : ")
    phone = input("Entrer le numéro de téléphone : ")
    email = input("Entrer l'adresse email : ")

    contacts.update({contact:{
      "phone": phone,
      "email": email,
    }})

def list_contacts(contacts):
  for key, value in contacts.items():
    print(f"{key} {value}")

def search_contact(contacts):
  search = input("Entrer le nom d'un contact : ")

  print(search)
  print(10*"-")
  print(f"Phone: {contacts[search]["phone"]}\nEmail {contacts[search]["email"]}")

contacts = {}

menu = f"""
1. Ajouter un contact
2. Lister tous les contacts
3. Rechercher un contact par nom
4. Quitter
"""

AGAIN = True

while AGAIN:
  print(menu)
  USER = -1
  while USER < 1 or USER > 4:
    USER = int(input("Choisir une action : "))
  if USER == 1:
    add_contact(contacts)
  if USER == 2:
    list_contacts(contacts)
  if USER == 3:
    search_contact(contacts)
  if USER == 4:
    AGAIN = False

