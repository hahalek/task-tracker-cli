import cmd
from datetime import datetime
import json

data_filepath = r'tasks_database.json'
id_filepath = r'id.txt'

class Task():
    def __init__(self, description: str):
        with open('id.txt', 'r') as f:
            id = int(f.read())
            new_id = id + 1
        
        timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

        self.id = new_id
        self.description = description
        self.status = 'todo'
        self.created_at = timestamp
        self.updated_at = timestamp

        with open('id.txt', 'w') as f:
            f.write(str(new_id))

    def task_to_dict(self):
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
        init_dict = {
            'todo': [],
            'in_progress': [],
            'done': []
        }
        with open(data_filepath, 'w') as f:
            f.write(json.dumps(init_dict))
        with open(id_filepath, 'w') as f:
            f.write('0')

    def add(self, description: str):
        # Create new task with todo status and ID, add createdAt and updatedAt timestamps
        new_task = Task(description)
        with open(data_filepath, 'r') as f:
            data_json = f.read()
        
        data_dict = json.loads(data_json)
        todo_list = data_dict['todo']
        new_task_dict = new_task.task_to_dict()
        todo_list.append(new_task_dict)
        with open(data_filepath, 'w') as f:
            f.write(json.dumps(data_dict))
        

    def update(self, id: int, new_description: str):
        #if description or id of the task is given
        update_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        with open(data_filepath, 'r') as f:
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
        with open(data_filepath, 'w') as f:
            f.write(json.dumps(data_dict))

    def delete(self, id: int):
        with open(data_filepath, 'r') as f:
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
        with open(data_filepath, 'w') as f:
            f.write(json.dumps(data_dict))
        


tracker = Tracker()
tracker.add('Pocwiczyc')


# {
#     "todo": [],
#     "in_progress": [],
#     "done": []
# }