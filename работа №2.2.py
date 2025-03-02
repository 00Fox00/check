class Task:
    def __init__(self, text):
        self.text = text
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "+" if self.completed else "-"
        return f"[{status}] {self.text}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, text):
        if text.strip():  # Проверка на пустой ввод
            task = Task(text)
            self.tasks.append(task)
            print("задача добавлен")
        else:
            print("ошибка был найден  пустой слот ")

    def view_tasks(self):
        if not self.tasks:
            print("список задач пуст")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"удалена задач {removed_task.text}")
        else:
            print("ошибка неверный номер задачи ")

def main():
    task_list = TaskList()
    
    while True:
        print("\nМеню:")
        print("1. Просмотреть  задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("выберите действие ")

        if choice == '1':
            task_list.view_tasks()
        elif choice == '2':
            text = input("введите текст задачи ")
            task_list.add_task(text)
        elif choice == '3':
            task_list.view_tasks()
            if task_list.tasks:  # Проверка, что есть задачи для удаления
                try:
                    index = int(input("Введите номер задачи для уничтожение ")) 
                    task_list.delete_task(index)
                except ValueError:
                    print("ошибка номер задачи не правтльно ")
        elif choice == '4':
            print("выход ")
            break
        else:
            print("ошибка номер задачи не правтльно")

if __name__ == "__main__":
    main()

