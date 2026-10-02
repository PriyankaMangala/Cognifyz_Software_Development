import json
FILE_NAME = "tasks.json"


class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description


tasks = []
next_task_id = 1


def save_tasks():
    try:
        data = []

        for task in tasks:
            data.append({
                "task_id": task.task_id,
                "title": task.title,
                "description": task.description
            })

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    except OSError:
        print("Error: Unable to save tasks.")

def load_tasks():
    global next_task_id

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for item in data:
            task = Task(
                item["task_id"],
                item["title"],
                item["description"]
            )

            tasks.append(task)

            if task.task_id >= next_task_id:
                next_task_id = task.task_id + 1

    except FileNotFoundError:
        pass

    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        print("Error: Unable to load tasks.")


def create_task():
    global next_task_id

    while True:
        title = input("Enter task title: ").strip()

        if not title:
            print("Title cannot be empty. Please try again.")
            continue

        description = input("Enter task description: ").strip()

        if not description:
            print("Description cannot be empty. Please try again.")
            continue

        task = Task(next_task_id, title, description)
        tasks.append(task)

        next_task_id += 1

        save_tasks()

        print("Task created successfully!")
        return


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== Tasks =====")

    for task in tasks:
        print(f"ID: {task.task_id}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print("--------------------")


def update_task():
    if not tasks:
        print("No tasks available to update.")
        return

    while True:
        view_tasks()

        try:
            task_id = int(input("Enter task ID to update: "))

            for task in tasks:
                if task.task_id == task_id:

                    title = input("Enter new title: ").strip()

                    if not title:
                        print("Title cannot be empty. Please try again.")
                        continue

                    description = input("Enter new description: ").strip()

                    if not description:
                        print("Description cannot be empty. Please try again.")
                        continue

                    task.title = title
                    task.description = description

                    save_tasks()

                    print("Task updated successfully!")
                    return

            print("Task not found. Please select an ID from the list.")

        except ValueError:
            print("Please enter a valid task ID.")


def delete_task():
    if not tasks:
        print("No tasks available to delete.")
        return

    while True:
        try:
            task_id = int(input("Enter task ID to delete: "))

            for task in tasks:
                if task.task_id == task_id:
                    print(f"Task found: {task.title}")

                    while True:
                        confirmation = input(
                            "Are you sure you want to delete this task? (y/n): "
                        ).strip().lower()

                        if confirmation == "y":
                            tasks.remove(task)
                            save_tasks()
                            print("Task deleted successfully!")
                            return

                        elif confirmation == "n":
                            print("Deletion cancelled.")
                            return

                        else:
                            print("Please enter only 'y' or 'n'.")

            print(f"\nNo task found with ID {task_id}.")
            print("Available tasks:")
            view_tasks()
            print("Please enter a valid task ID.")

        except ValueError:
            print("Please enter a valid task ID.")
            
def main():
    load_tasks()

    while True:
        print("\n===== Task Manager =====")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()