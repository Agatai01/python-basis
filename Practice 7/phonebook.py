from db import *

while True:
    print("\n1. Add contact")
    print("2. Show contacts")
    print("3. Search (name or phone)")
    print("4. Update (name or phone)")
    print("5. Delete (name or phone)")
    print("6. Filter by prefix")
    print("7. Import CSV")
    print("8. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        insert_contact(name, phone)

    elif choice == "2":
        get_contacts()

    elif choice == "3":
        value = input("Enter name or phone: ")
        search_contact(value)

    elif choice == "4":
        update_contact()

    elif choice == "5":
        value = input("Enter name or phone: ")
        delete_contact(value)

    elif choice == "6":
        prefix = input("Enter phone prefix: ")
        filter_by_prefix(prefix)

    elif choice == "7":
        insert_from_csv("contacts.csv")

    elif choice == "8":
        break