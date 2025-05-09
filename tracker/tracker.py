import cmd
from datetime import datetime
import json
from .utils import get_id, save_id

with open('config.json', 'r') as f:
    config = json.loads(f.read())

TASKS_FILEPATH = config['TASKS_FILEPATH']

class Task():
    def __init__(self, data: str | dict):
        if type(data) == str:
            timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            new_id = get_id() + 1

            self.id = new_id
            self.description = data
            self.status = 'todo'
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
    def __init__(self):
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
        print(data)
        return data


    def save_tasks(self, tasks):
        for key in tasks.keys():
            tasks[key] = [task.to_dict() for task in tasks[key]]
        with open(TASKS_FILEPATH, 'w') as f:
            f.write(json.dumps(tasks))



    def add(self, description: str):
        # Create new task with todo status and ID, add createdAt and updatedAt timestamps
        new_task = Task(description)
        tasks = self.get_tasks()
        tasks['todo'].append(new_task)
        self.save_tasks(tasks)
        #TODO tasks: dict[str, list[Task]] = TaskDB(**data_dict)
        

    def update(self, id: int, new_description: str):
        #if description or id of the task is given
        update_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        tasks = self.get_tasks()
        with open(TASKS_FILEPATH, 'r') as f:
            data_json = f.read()
        
        data_dict = json.loads(data_json)
        for task in data_dict['todo']:
            if task['id'] == id:
                task['description'] = new_description
                task['updated_at'] = update_time
        for task in data_dict['in_progress']:
            if task['id'] == id:
                task['description'] = new_description
                task['updated_at'] = update_time
        for task in data_dict['done']:
            if task['id'] == id:
                task['description'] = new_description
                task['updated_at'] = update_time
        with open(TASKS_FILEPATH, 'w') as f:
            f.write(json.dumps(data_dict))

    def delete(self, id: int):
        with open(TASKS_FILEPATH, 'r') as f:
            data_json = f.read()
        
        data_dict = json.loads(data_json)
        for task in data_dict['todo']:
            if task['id'] == id:
                data_dict['todo'].remove(task)
        for task in data_dict['in_progress']:
            if task['id'] == id:
                data_dict['in_progress'].remove(task)
        for task in data_dict['done']:
            if task['id'] == id:
                data_dict['done'].remove(task)
        with open(TASKS_FILEPATH, 'w') as f:
            f.write(json.dumps(data_dict))
        


tracker = Tracker()
tracker.add('One')
tracker.add('Two')
tracker.get_tasks()


# {
#     "__id": 4
#     "todo": [],
#     "in_progress": [],
#     "done": []
# }