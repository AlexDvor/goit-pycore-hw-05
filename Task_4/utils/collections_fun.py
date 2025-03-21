def add_contact(name: str, phone: str, contacts: dict):
    contacts[name] = phone
    print(f"Contact {name} added!")


def change_contact(name: str, phone: str, contacts: dict):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} updated!")
    else:
        print("Contact not found!")


def show_phone(name: str, contacts: dict):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found!")


def show_all(contacts: dict):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")
