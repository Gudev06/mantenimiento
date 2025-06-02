import os
import json
import uuid
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_name = "tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    self.tasks = json.load(file)
            except:
                print("Error loading task data. Starting with empty task list.")
                self.tasks = []
    
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, title, description):
        if not title.strip():
            print("Error: Title cannot be empty.")
            return
        if not description.strip():
            print("Error: Description cannot be empty.")
            return

        task = {
            "id": str(uuid.uuid4()),
            "title": title.strip(),
            "description": description.strip(),
            "status": "Pending",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n" + "=" * 120)
        print(f"{'ID':<36} {'TITLE':<20} {'STATUS':<10} {'CREATED DATE':<20} {'DESCRIPTION':<30}")
        print("-" * 120)
        
        for task in self.tasks:
            print(f"{task['id']:<36} {task['title'][:18]:<20} {task['status']:<10} {task['created_date']:<20} {task['description'][:28]:<30}")
        
        print("=" * 120 + "\n")
    
    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def mark_complete(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task["status"] = "Completed"
            self.save_tasks()
            print(f"Task '{task['title']}' marked as completed!")
        else:
            print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task '{removed['title']}' deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")


def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        
        elif choice == "2":
            task_manager.list_tasks()
        
        elif choice == "3":
            task_id = input("Enter task ID to mark as complete: ").strip()
            if not task_id:
                print("Error: Task ID cannot be empty.")
                continue
            task_manager.mark_complete(task_id)
        
        elif choice == "4":
            task_id = input("Enter task ID to delete: ").strip()
            if not task_id:
                print("Error: Task ID cannot be empty.")
                continue
            task_manager.delete_task(task_id)
        
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
