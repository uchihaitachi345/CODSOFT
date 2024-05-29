class MyTaskList:
    def __init__(self):
        self.my_tasks = []

    def add_new_task(self, description):
        self.my_tasks.append(description)

    def delete_task(self, index):
        if 0 <= index < len(self.my_tasks):
            del self.my_tasks[index]
            print("task deleted")
        else:
            print("task missing")

    def show_my_tasks(self):
        if self.my_tasks:
            print(" list:")
            for idx, task in enumerate(self.my_tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("task list empty")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.my_tasks:
                file.write(task + '\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.my_tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("file not found")


def display_menu():
    print("1. New Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. end")


def get_choice():
    while True:
        choice = input("select a number: ")
        if choice in {"1", "2", "3", "4", "5", "6"}:
            return choice
        else:
            print(" not valid choice.enter again")


def get_task_number(tasks):
    while True:
        try:
            task_number = int(input("Enter the number to the task: ")) - 1
            if 0 <= task_number < len(tasks):
                return task_number
            else:
                print(" Please pick a valid task number.")
        except ValueError:
            print("Sorry, Could you enter a valid number?")


def start_Program():
    my_task_list = MyTaskList()
    while True:
        display_menu()
        choice = get_choice()

        if choice == "1":
            task_description = input("task to add to the list ")
            my_task_list.add_new_task(task_description)
            print("Task successfully added")
        elif choice == "2":
            if my_task_list.my_tasks:
                task_number = get_task_number(my_task_list.my_tasks)
                my_task_list.delete_task(task_number)
            else:
                print("no tasks for to remove.")
        elif choice == "3":
            my_task_list.show_my_tasks()
        elif choice == "4":
            filename = input("file name to save the task")
            my_task_list.save_to_file(filename)
            print("successfully saved!")
        elif choice == "5":
            filename = input("which file to load")
            my_task_list.load_from_file(filename)
            print(" file loaded successfully!")
        elif choice == "6":
            print("bye")
            break

if __name__ == "__main__":
    start_Program()
