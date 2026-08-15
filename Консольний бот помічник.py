"""
hw04.py — Консольний бот-помічник для зберігання контактів.

Команди:
    hello
    add <ім'я> <телефон>
    change <ім'я> <новий_телефон>
    phone <ім'я>
    all
    close / exit
"""


def parse_input(user_input):
    """
    Розбиває введений рядок на команду та аргументи.
    Перше слово — команда (у нижньому регістрі), решта — аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """Додає новий контакт до словника. Приймає [ім'я, телефон]."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер телефону для вже існуючого контакту."""
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    """Виводить номер телефону для вказаного контакту."""
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


def show_all(contacts):
    """Повертає рядок з усіма збереженими контактами."""
    if not contacts:
        return "No contacts saved."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()