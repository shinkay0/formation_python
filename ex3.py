class Contact:
  def __init__(self, name, phone, mail):
    self.name=name
    self.phone=phone
    self.mail=mail

  def __str__(self):
    return f"{'-'*20}\nName = {self.name}\nPhone = {self.phone}\nMail = {self.mail}"

class ContactBook:
  def __init__(self):
    self.contacts = {}
    default_contact = Contact("default", "000-000-0000", "default@mail.com")
    self.contacts[default_contact.name] = default_contact

  def add_contact(self, contacts):
    self.contacts[contacts.name]=contact

  def list_contacts(self):
    for contact in self.contacts.values():
      print(contact)

  def search_contact(self, name):
    return self.contacts.get(name, "pas de contact trouvé")
  
  def delete_contact(self, name):
    return self.contacts.pop(name)


contacts = ContactBook()

menu = """
1. Ajouter un contact
2. Lister tous les contacts
3. Rechercher un contact par nom
4. Supprimer un contact par nom
5. Quitter
"""

AGAIN = True

while AGAIN:
  print(menu)
  USER = -1
  while USER < 1 or USER > 5:
    try:
      USER = int(input("Choisir une option : "))
    except ValueError:
      print("Veuillez entrer un nombre valide")
      
  if USER == 1:
    name = input("Entrer le nom : ")
    phone = input("Entrer le numéro de téléphone : ")
    mail = input("Entrer le mail : ")
    contact = Contact(name, phone, mail)
    contacts.add_contact(contact)
  if USER == 2:
    contacts.list_contacts()
  if USER == 3:
    name = input("Entrer le nom du contact : ")
    print(contacts.search_contact(name))
  if USER == 4:
    name = input("Entrer le nom du contact : ")
    contacts.delete_contact(name)
  if USER == 5:
    AGAIN = False


