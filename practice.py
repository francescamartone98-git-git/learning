def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for person in contacts:
            file.write(f"{person['name']},{person['city']}\n")

def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    contacts.append({"name": parts[0], "city": parts[1]})
    except FileNotFoundError:
        pass
    return contacts

contacts = load_contacts()

while True:
    print("\n1. Add contact")
    print("2. Show all contacts")
    print("3. Quit")
    print("4. Search contact")
    print("5. Delete contact")

    choice = input("Choose an option: ")
    print(f"You chose: '{choice}'")

    if choice == "3":
        save_contacts(contacts)
        print("Contacts saved. Goodbye!")
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

    if choice == "4":
        search = input("Enter a name to search: ")
        found = False
        for person in contacts:
            if search.lower() in person["name"].lower():
                print(f"Found: {person['name']} - {person['city']}")
                found = True
        if not found:
            print("No contact found with that name.")

    if choice == "5":
        search = input("Enter a name to delete: ")
        found = False
        for person in contacts:
            if search.lower() in person["name"].lower():
                confirm = input(f"Delete {person['name']} from {person['city']}? (yes/no): ")
                if confirm == "yes":
                    contacts.remove(person)
                    print(f"{person['name']} deleted!")
                    found = True
                    break
        if not found:
            print("No contact found with that name.")