import time
class Task:
    ids = list()
    def __init__(self, title: str, description: str, task_id: str):
        
        self.title = title
        self.desc = description
        self.is_valied(task_id)
        self.task_id = task_id
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.end_time = None
        self.status = False

    @staticmethod
    def is_valied(task_id):
        if not task_id.isnumeric():
            raise ValueError("ID must be numeric")
        
    def __str__(self):
        return f"Title: {self.title}, Description: {self.desc}, ID: {self.task_id}, ST: {self.start_time}, ET: {self.end_time}, status: {self.status}"




