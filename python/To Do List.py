class TodoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")

    def show_tasks(self):
        if self.tasks:
            print("Your to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
