import json
contacts = []
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        for i, contact in enumerate(contacts):
            print(f"Contact {i+1}:")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print()
def edit_contact():
    view_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("Editing contact:")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print()
            name = input("Enter new name (or press Enter to keep existing): ")
            phone = input("Enter new phone number (or press Enter to keep existing): ")
            email = input("Enter new email address (or press Enter to keep existing): ")
            if name:
                contact['Name'] = name
            if phone:
                contact['Phone'] = phone
            if email:
                contact['Email'] = email
            print("Contact updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
def delete_contact():
    view_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact {deleted_contact['Name']} deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
def save_to_file():
    filename = input("Enter the filename to save contacts: ")
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print("Contacts saved to file successfully!")
def load_from_file():
    global contacts
    filename = input("Enter the filename to load contacts from: ")
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
        print("Contacts loaded from file successfully!")
    except FileNotFoundError:
        print("File not found.")
    except json.decoder.JSONDecodeError:
        print("Invalid JSON format in the file.")
while True:
    print("\nContact Manager Menu:")
    print("1. Add a Contact")
    print("2. View Contacts")
    print("3. Edit a Contact")
    print("4. Delete a Contact")
    print("5. Save Contacts to File")
    print("6. Load Contacts from File")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        save_to_file()
    elif choice == '6':
        load_from_file()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
