contacts = dict()  

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add/Edit Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number (10 digits): ")
        
        if phone.isdigit() and len(phone) == 10:
            contacts[name] = phone  # add or update the contact in the dictionary
            print(f"Contact '{name}' added/updated successfully")
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")
        
    elif choice == "2":
        name = input("Enter the name of the contact to delete: ")
        
        if name in contacts:  # check if the contact exists in the dictionary
            del contacts[name]  # delete the contact from the dictionary
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found")
            
    elif choice == "3":
        if contacts:  # check if there are any contacts in the dictionary
            print("\n--- Contact List ---")
            for name, phone in contacts.items():  # iterate through the dictionary to display contacts
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts to display.")
    
    elif choice == "4":
        print("Exiting Contact Book. Goodbye")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
