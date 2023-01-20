import requests


# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080

    inWork = True
    print("Варианты действий: \n"
          "1 - Создать заметку\n"
          "2 - Прочитать заметку\n"
          "3 - Получать информацию о заметке\n"
          "4 - Удалить заметку\n"
          "5 - Обновить заметку\n"
          "6 - Получить список заметок\n"
          "7 - Прервать программу\n")
    while inWork:
        choice = int(input("Введите номер действия: "))
        if choice == 1:
                text = input("Введите текст заметки: ")
                token = input("Введите токен: ")
                response = requests.post(f"http://{HOST}:{PORT}" + "/createNote", params={"text": text, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 2:
                note_id = int(input("Введите id заметки: "))
                token = input("Введите токен: ")
                response = requests.get(f"http://{HOST}:{PORT}" + "/getNoteText", params={"id": note_id, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 3:
                note_id = int(input("Введите id заметки: "))
                token = input("Введите токен: ")
                response = requests.get(f"http://{HOST}:{PORT}" + "/getNoteInfo", params={"note_id": note_id, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 4:
                note_id = int(input("Введите id заметки: "))
                token = input("Введите токен: ")
                response = requests.delete(f"http://{HOST}:{PORT}" + "/removeNote", params={"note_id": note_id, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 5:
                note_id = int(input("Введите id заметки: "))
                text = input("Введите текст заметки: ")
                token = input("Введите токен: ")
                response = requests.patch(f"http://{HOST}:{PORT}" + "/updateNote", params={"note_id": note_id, "text": text, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 6:
                token = input("Введите токен: ")
                response = requests.get(f"http://{HOST}:{PORT}" + "/getNotesList", params={"token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 7:
                inWork = False
        else:
            print("Wrong choice")