Contact = []
Deleted_Contacts = []
def add_contact(name, mobile, e_mail, address):
  if mobile.isdigit() and len(mobile) == 10:
    Contact.append({'Name':name, 'Mobile':mobile, 'E_Mail':e_mail, 'Address':address})
    print("Contact is added in the Contact Book")
  else:
    print("Enter a valid mobile number")
def update_contact(name, mobile, e_mail, address):
  if mobile.isdigit() and len(mobile) == 10:
    index = 0
    while index < len(Contact):
      if Contact[index]['Name'] == name:
        Contact[index]['Mobile'] = mobile
        Contact[index]['E_Mail'] = e_mail
        Contact[index]['Address'] = address
        print("Contact is updated in the Contact Book")
        return
      index += 1
  else:
    print("Contact is not in the Contact Book")
def view_contacts():
  if not Contact:
    print("Contact Book is empty")
  else:
    print("Contact Book")
    for contact in Contact:
      print("Name : ", contact['Name'])
      print("Mobile : ", contact['Mobile'])
      print("E_Mail : ", contact['E_Mail'])
      print("Address : ", contact['Address'])
      print("")
def search_contact(query):
  found = False
  for contact in Contact:
    if query in contact['Name'] or query in contact['Mobile']:
      print("Name : ", contact['Name'])
      print("Mobile : ", contact['Mobile'])
      print("E_Mail : ", contact['E_Mail'])
      print("Address : ", contact['Address'])
      print("")
    else:
      print("Contact is not in the Contact book")
def delete_contact(name):
  for contact in Contact:
    if contact['Name'] == name:
      Deleted_Contacts.append(contact)
      Contact.remove(contact)
      print("Contact is Deleted from the Contact Book")
      return
  print("Contact is not found in the Contact Book")
def restore_contact(name):
  for contact in Deleted_Contacts:
    if contact['Name'] == name:
      Contact.append(contact)
      Deleted_Contacts.remove(contact)
      print("Contact is restored")
      return
  print("Contact not found in deleted history")
def main():
  print("CONTACT BOOK")
  while True:
    print("\n Menu")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. View Contacts")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. restore")
    print("7. Quit")
    Choice = input("Enter your choice")
    if Choice == "1":
      name = input("Enter Contact Name : ")
      mobile = input("Enter Mobile Number : ")
      e_mail = input("Enter E_Mail ID : ")
      address = input("Enter Address : ")
      add_contact(name, mobile, e_mail, address)
    elif Choice == "2":
      name = input("Enter Contact Name to update : ")
      mobile = input("Enter new Mobile Number : ")
      e_mail = input("Enter new E_Mail : ")
      address = input("Enter new Address : ")
      update_contact(name, mobile, e_mail, address)
    elif Choice == "3":
      view_contacts()
    elif Choice == "4":
      query = input("Enter Contact Name or Mobile Number : ")
      search_contact(query)
    elif Choice == "5":
      Name = input("Enter Contact Name to Delete : ")
      delete_contact(Name)
    elif Choice == "6":
      name = input("Enter Contact Name to restore : ")
      restore_contact(name)
    elif Choice == "7":
      print("Exiting")
      print(Deleted_Contacts)
      break
    else:
      print("INVALID. Enter number from 1 to 6 : ")
if __name__ == "__main__":
  main()