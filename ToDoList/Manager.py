from Task import *

class Manager:
    def __init__(self):
        self.tasks = {}

    def creat_task(self, title, description, t_id):
        new_task = Task(title, description, t_id)
        return new_task

    def add_task(self, task):
        if task.task_id not in self.tasks:
            self.tasks[task.task_id] = task
            print("Added")
        else:
            print("ID already exist")

    def mark_done(self, task_id):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if task.status == False:
                task.status = True
                task.end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print("Done")
        else:
            print("ID not found")

    def display_tasks(self):
        if not self.tasks:
            print("Empty")
        for task in self.tasks.values():
            print(task)

    def summary(self):
        all_tasks = len(self.tasks)
        done_tasks = 0
        for task in self.tasks.values():
            if task.status :
                done_tasks += 1
        not_finished = all_tasks - done_tasks
        print(f"Done Tasks: {done_tasks}, Undone Tasks: {not_finished}")

if __name__ == "__main__":
    maneger1 = Manager()
    task1 = maneger1.creat_task("AS", "kgkhyf", "67")
    task2 = Task("AS", "kgkhyf", "8")
    maneger1.add_task(task1)
    maneger1.add_task(task2)
    maneger1.mark_done("67")
    maneger1.display_tasks()
    maneger1.summary()
    