class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description


tasks = []
next_task_id = 1


def get_non_empty_input(prompt):
    """Get input that is not empty or only spaces."""
    while True:
        try:
            value = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            return None

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_task_id(prompt):
    """Get a valid positive integer task ID."""
    while True:
        try:
            value = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            return None

        if not value:
            print("Task ID cannot be empty. Please enter a valid ID.")
            continue

        try:
            task_id = int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if task_id <= 0:
            print("Task ID must be greater than 0.")
            continue

        return task_id


def create_task():
    global next_task_id

    print("\n===== Create Task =====")

    title = get_non_empty_input("Enter task title: ")

    if title is None:
        return

    description = get_non_empty_input("Enter task description: ")

    if description is None:
        return

    task = Task(next_task_id, title, description)
    tasks.append(task)

    print(f"Task created successfully! Task ID: {next_task_id}")

    next_task_id += 1


def view_tasks():
    print("\n===== View Tasks =====")

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(f"ID          : {task.task_id}")
        print(f"Title       : {task.title}")
        print(f"Description : {task.description}")
        print("-" * 30)


def update_task():
    print("\n===== Update Task =====")

    if not tasks:
        print("No tasks available to update.")
        return

    while True:
        task_id = get_task_id("Enter task ID to update: ")

        if task_id is None:
            return

        for task in tasks:
            if task.task_id == task_id:

                print(f"\nCurrent title: {task.title}")
                print(f"Current description: {task.description}")

                new_title = get_non_empty_input("Enter new title: ")

                if new_title is None:
                    return

                new_description = get_non_empty_input(
                    "Enter new description: "
                )

                if new_description is None:
                    return

                task.title = new_title
                task.description = new_description

                print("Task updated successfully!")
                return

        print(f"\nNo task found with ID {task_id}.")
        print("Available tasks:")
        view_tasks()
        print("Please enter a valid task ID.")

def delete_task():
    print("\n===== Delete Task =====")

    if not tasks:
        print("No tasks available to delete.")
        return

    while True:
        task_id = get_task_id("Enter task ID to delete: ")

        if task_id is None:
            return

        for task in tasks:
            if task.task_id == task_id:

                print(f"Task found: {task.title}")

                while True:
                    try:
                        confirmation = input(
                            "Are you sure you want to delete this task? (y/n): "
                        ).strip().lower()
                    except (EOFError, KeyboardInterrupt):
                        print("\nDeletion cancelled.")
                        return

                    if confirmation == "y":
                        tasks.remove(task)
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
        
def main():
    print("===== Task Manager =====")

    while True:
        print("\n1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nProgram closed.")
            break

        if choice == "1":
            create_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you for using Task Manager. Goodbye!")
            break

        elif not choice:
            print("Choice cannot be empty. Please enter a number from 1 to 5.")

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()