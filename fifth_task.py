import json

# файлдан алу операциясы tasks.json
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# файлга сактау операциясы tasks.json
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# задача косу операциясы
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Задача добавлена: ", task)

# задачаны кору/оку операциясы
def view_tasks(tasks):
    if not tasks:
        print("Нет задач для отображения.")
    else:
        print("\nЗадачи:")
        for index, task in enumerate(tasks, start=1):
            status = "Завершена" if task["completed"] else "В процессе"
            print(f"{index}. {task['task']} ({status})")

# задачаны орындалды деп озгерту функциясы
def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f'Задача "{tasks[index]["task"]}" отмечена как завершенная.')
    else:
        print("Неверный номер задачи.")

# задачаны озгерту функциясы
def edit_task(tasks, index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        save_tasks(tasks)
        print(f'Задача отредактирована: "{new_task}"')

# задачаны оширу функциясы
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f'Задача "{deleted_task["task"]}" удалена.')
    else:
        print("Неверный номер задачи.")

# файлдан задачаларды алу
tasks = load_tasks()

while True:
    print("\nМенеджер списка дел")
    print("1. Добавить задачу")
    print("2. Просмотр задач")
    print("3. Отметить задачу как завершенную")
    print("4. Редактировать задачу")
    print("5. Удалить задачу")
    print("6. Выход")

    choice = input("Введите ваш выбор (1/2/3/4/5/6): ")

    if choice == '1':
        task = input("Введите задачу: ")
        add_task(tasks, task)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        if not tasks:
            print("Нет задач для отметки как завершенных.")
        else:
            view_choice = input("Введите номер задачи для отметки как завершенной: ")
            try:
                index = int(view_choice) - 1
                mark_task_completed(tasks, index)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите верный номер задачи.")
    elif choice == '4':
        view_tasks(tasks)
        edit_choice = input("Введите номер задачи для редактирования: ")
        try:
            index = int(edit_choice) - 1
            new_task = input("Введите новую задачу: ")
            edit_task(tasks, index, new_task)
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите верный номер задачи.")
    elif choice == '5':
        view_tasks(tasks)
        delete_choice = input("Введите номер задачи для удаления: ")
        try:
            index = int(delete_choice) - 1
            delete_task(tasks, index)
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите верный номер задачи.")
    elif choice == '6':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите верный вариант.")
