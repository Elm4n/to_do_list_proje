import csv

class Task():
    def __init__(self, name, desc, priority):
        self.name = name
        self.desc = desc
        self.priority = int(priority)
        
    def __str__(self):
        return f"{self.priority} ({self.name}): {self.desc}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        """
        add a new task to the list.
        asks user name, description and priority of a task to add to a list of tasks. prevent duplicate task names.

        """
        name = input("Enter task name: ").strip()
        desc = input("Enter description: ").strip()
        while True:
            try:
                priority = int(input("Enter priority number: ").strip())
                break
            except(ValueError):
                print("Priority must be an integer.")
        
        if any(t.name.lower() == name.lower() for t in self.tasks):
            print("Task with this name already exists.")
        else:
            new_task = Task(name, desc, priority)
            self.tasks.append(new_task)
            print(f"Task '{new_task.name}' added successfully!")

    def remove_task(self):
        """
        remove a task from the list.
        asks the  user for task name and delete it from the list if found.

        """
        rt = input("Enter a task you want to delete: ").strip()
        for t in self.tasks:
            if t.name.lower() == rt.lower():
                self.tasks.remove(t)
                print(f"{t.name} deleted")
                return
        print("task not found")

    def show_task(self):
        """
        display all tasks sorted by priority .

        """
        if not self.tasks:
            print("No tasks")
            return
        for i, task in enumerate(sorted(self.tasks, key = lambda x:x.priority), start = 1):
            print(f"{i}: {task.priority} {task.name} {task.desc}")



    def save_csv(self, path="tasks.csv"):
        """
        save task to a CSV file.
        A list of tasks, where each task is a list in the form
        [priority (int), name (str), desc (str)].

            """
        with open(path, "w", newline = "", encoding = "utf-8" ) as file:
            writer = csv.writer(file)
            writer.writerow(["priority", "name", "desc"])
            for task in self.tasks:
                writer.writerow([task.priority, task.name, task.desc])

    def load_csv(self, path = "tasks.csv"):
        """
        Load tasks from a CSV file.
        A list of tasks, where each task is a list in the form
        [priority (int), name (str), desc (str)].
        Returns an empty list if the file does not exist.
        """
        try:
            with open(path, "r", newline = "", encoding = "utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks = [
                    Task(row["name"], row["desc"], int(row["priority"]))
                    for row in reader
                    if row.get("name")
                ]
            
        except FileNotFoundError:
            self.tasks = []
    
if __name__ == "__main__":
    app = TaskManager()
    app.load_csv()

    while True:
        print("\n 1)Add   2)Remove   3)Show   4)Save   5)Exit")
        choice = input("choose : ").strip()
        if choice == "1":
            app.add_task()
        elif choice == "2":
            app.remove_task()
        elif choice == "3":
            app.show_task()
        elif choice == "4":
            app.save_csv(app.tasks)
            print(f"Saved {len(app.tasks)} tasks.")
        elif choice == "5":
            app.save_csv(app.tasks)
            break
        else:
            print("Invalid choice")