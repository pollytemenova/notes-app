import json
import datetime

FILENAME = "notes.json"


def load_notes():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open(FILENAME, 'w') as file:
        json.dump(notes, file, indent=4)


def add_note(notes):
    title = input("Введите заголовок: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "date": datetime.datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)


def edit_note(notes):
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок: ")
            note["body"] = input("Введите новый текст заметки: ")
            note["date"] = datetime.datetime.now().isoformat()
            save_notes(notes)
            break


def delete_note(notes):
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)


def list_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['date']}")
        print(f"Текст: {note['body']}\n")


def find_note_by_date(notes):
    search_date = input("Введите дату для поиска (YYYY-MM-DD): ")
    for note in notes:
        if note["date"].startswith(search_date):
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['date']}")
            print(f"Текст: {note['body']}\n")


def main():
    notes = load_notes()

    while True:
        print("\nКоманды: add, edit, delete, list, find, exit")
        command = input("Введите команду: ")

        if command == "exit":
            break
        elif command == "add":
            add_note(notes)
        elif command == "edit":
            edit_note(notes)
        elif command == "delete":
            delete_note(notes)
            notes = load_notes()
        elif command == "list":
            list_notes(notes)
        elif command == "find":
            find_note_by_date(notes)
        else:
            print("Неизвестная команда")


if __name__ == '__main__':
    main()