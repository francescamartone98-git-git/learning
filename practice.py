contacts = []

while True:
    print("\n1. Add contact")
    print("2. Show all contacts")
    print("3. Quit")
    
    choice = input("Choose an option: ")
    
    if choice == "3":
        print("Goodbye!")
        break

    if choice == "1":
        adding = True
        while adding:
            name = input("Name: ")
            city = input("City: ")
            contacts.append({"name": name, "city": city})
            print(f"{name} added!")
            another = input("Add another? (yes/no): ")
            if another != "yes":
                adding = False
    
    if choice == "2":
        if len(contacts) == 0:
            print("No contacts yet!")
        else:
            for person in contacts:
                print(f"{person['name']} - {person['city']}")  