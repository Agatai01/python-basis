from db import *

while True:
    print("\n1. Add contact")
    print("2. Show contacts")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Import CSV")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        insert_contact(name, phone)

    elif choice == "2":
        get_contacts()

    elif choice == "3":
        name = input("Search name: ")
        search_by_name(name)

    elif choice == "4":
        name = input("Name: ")
        phone = input("New phone: ")
        update_phone(name, phone)

    elif choice == "5":
        name = input("Delete name: ")
        delete_contact(name)

    elif choice == "6":
        insert_from_csv("contacts.csv")

    elif choice == "7":
        break