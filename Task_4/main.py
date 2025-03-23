from utils.collections_fun import add_contact, change_contact, show_all, show_phone

contacts = {}


def parse_input(inputted_data: str):
    command = inputted_data.split()
    command = [word.lower().strip() for word in command]
    return command


def handler_input(command_list: list[str]):
    try:
        command, *args = command_list
        match command:
            case "add":
                return add_contact(args, contacts)
            case "change":
                return change_contact(args, contacts)
            case "show":
                return show_phone(args, contacts)
            case "all":
                return show_all(args, contacts)
            case _:
                return "Invalid command!"
    except Exception as e:
        return f"An error occurred: {e}"


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command = parse_input(user_input)

        if command in [["exit"], ["close"]]:
            print("Goodbye!")
            break
        elif command == ["hello"]:
            print("How can I help you?")
        else:
            response = handler_input(command)
            print(response)


if __name__ == "__main__":
    main()


"""
Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.



Вимоги до завдання:

Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


Рекомендації для виконання:

В якості прикладу додамо декоратор input_error для обробки помилки ValueError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner



Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."



Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.



Критерії оцінювання:

Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.


Приклад використання:

При запуску скрипту діалог з ботом повинен бути схожим на цей.

Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356 
Enter a command:
"""
