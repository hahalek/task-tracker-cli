import cmd
from datetime import datetime
import json
from utils import get_id, save_id, get_updated_time

with open('config.json', 'r') as f:
    config = json.loads(f.read())

TASKS_FILEPATH = config['TASKS_FILEPATH']

class Task():
    def __init__(self, data: str | dict, status: str = 'todo'):
        if type(data) == str:
            timestamp = get_updated_time()
            new_id = get_id() + 1

            self.id = new_id
            self.description = data
            self.status = status
            self.created_at = timestamp
            self.updated_at = timestamp

            save_id(new_id)
            
        elif type(data) == dict:
            self.id = data['id']
            self.description = data['description']
            self.status = data['status']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']


    def to_dict(self):
        task_dict = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return task_dict




class Tracker():
    def __init__(self, reset: bool = False):
        if reset:
            '''Initialize json with all tasks to default skelethon, and set ID to 0'''
            init_dict = {
                'todo': [],
                'in_progress': [],
                'done': []
            }
            with open(TASKS_FILEPATH, 'w') as f:
                f.write(json.dumps(init_dict))
            save_id(0)


    def get_tasks(self):
        with open(TASKS_FILEPATH, 'r') as f:
            data = json.loads(f.read())
        for key in data.keys():
            data[key] = [Task(x) for x in data[key]]
        return data


    def save_tasks(self, tasks):
        for key in tasks.keys():
            tasks[key] = [task.to_dict() for task in tasks[key]]
        with open(TASKS_FILEPATH, 'w') as f:
            f.write(json.dumps(tasks))
    

    def find_task(self, tasks, by: str, value):
        if by == 'id':
            for key in tasks.keys():
                for task in tasks[key]:
                    if task.id == value:
                        return task
        elif by == 'description':
            for key in tasks.keys():
                for task in tasks[key]:
                    if task.description == value:
                        return task



    def add(self, description: str, status: str = 'todo'):
        # Create new task with todo status and ID, add createdAt and updatedAt timestamps
        new_task = Task(description, status)
        tasks = self.get_tasks()
        tasks[status].append(new_task)
        self.save_tasks(tasks)
        #TODO tasks: dict[str, list[Task]] = TaskDB(**data_dict)
        

    def update(self, id: int, new_description: str):
        #if description or id of the task is given
        tasks = self.get_tasks()
        for key in tasks.keys():
                for task in tasks[key]:
                    if task.id == id:
                        task.description = new_description
                        task.updated_at = get_updated_time()
        self.save_tasks(tasks)


    def delete(self, id: int):
        tasks = self.get_tasks()
        for key in tasks.keys():
            for task in tasks[key]:
                if task.id == id:
                    tasks[key].remove(task)
        self.save_tasks(tasks)
    

    def mark(self, id: int, new_status: str):
        tasks = self.get_tasks()
        for key in tasks.keys():
            for task in tasks[key]:
                if task.id == id:
                    target_task = task
                    tasks[key].remove(task)
                    break
        target_task.status = new_status
        target_task.updated_at = get_updated_time()
        tasks[new_status].append(target_task)
        self.save_tasks(tasks)
    
    def list(self, status: str):
        tasks = self.get_tasks()
        print(f'{status} list:')
        for task in tasks[status]:
            print(f'   {task.id:<5} {task.description:<40} ({task.created_at})')
    




# {
#     "__id": 4
#     "todo": [],
#     "in_progress": [],
#     "done": []
# }