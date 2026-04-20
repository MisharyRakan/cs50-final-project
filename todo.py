def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()

    print("Simple To‑Do List")
    print("1) Add task")
    print("2) Show tasks")
    print("3) Delete task")
    print("4) Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Added.")

    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        num = int(input("Delete number: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Deleted.")

    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
