import json

contactDict = {}

def loadContacts():
    try:
        with open("contacts.json", "r") as file:
            global contactDict
            contactDict = json.load(file)
    except FileNotFoundError:
        # If the file is not found, it's okay; contacts will be an empty dictionary.
        pass

def saveContacts():
    with open("contacts.json", "w") as file:
        json.dump(contactDict, file)

def addContact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contactDict[name] = number
    print("Contact added")
    saveContacts()

def viewContact():
    for name in contactDict:
        print(name, ":", contactDict[name])

def deleteContact():
    name = input("Enter name: ")
    if name in contactDict:
        del contactDict[name]
        print("Contact deleted")
        saveContacts()
    else:
        print("Contact not found")

def updateContact():
    name = input("Enter name: ")
    if name in contactDict:
        number = input("Enter new number: ")
        contactDict[name] = number
        print("Contact updated")
        saveContacts()
    else:
        print("Contact not found")

def searchContact():
    name = input("Enter name: ")
    if name in contactDict:
        print(name, ":", contactDict[name])
    else:
        print("Contact not found")

def main():
    loadContacts()

    while True:
        print("1. Add contact")
        print("2. View contact")
        print("3. Delete contact")
        print("4. Update contact")
        print("5. Search contact")
        print("6. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            addContact()
        elif choice == 2:
            viewContact()
        elif choice == 3:
            deleteContact()
        elif choice == 4:
            updateContact()
        elif choice == 5:
            searchContact()
        elif choice == 6:
            saveContacts()
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()
