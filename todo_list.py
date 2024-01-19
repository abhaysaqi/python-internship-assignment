class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: {task}')

    def delete_task(self, task_number):
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                deleted_task = self.tasks.pop(task_number - 1)
                print(f'Task deleted: {deleted_task}')
            else:
                print('Invalid task number.')
        except ValueError:
            print('Please enter a valid task number.')

    def mark_as_completed(self, task_number):
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                completed_task = self.tasks[task_number - 1]
                self.tasks[task_number - 1] = f'[Completed] {completed_task}'
                print(f'Task marked as completed: {completed_task}')
            else:
                print('Invalid task number.')
        except ValueError:
            print('Please enter a valid task number.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('\nTasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')


def main():
    todo_list = TodoList()

    while True:
        print("\n*** To-Do List ***")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
            if len(todo_list.tasks)==0:
                continue
            else:
                task_number = input("Enter task number to delete: ")
            todo_list.delete_task(task_number)
        elif choice == '3':
            todo_list.view_tasks()
            task_number = input("Enter task number to mark as completed: ")
            todo_list.mark_as_completed(task_number)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
