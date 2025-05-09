import json
from datetime import datetime


with open('config.json', 'r') as f:
    config = json.loads(f.read())

TASKS_FILEPATH = config['TASKS_FILEPATH']


def get_id():
    with open('config.json', 'r') as f:
        config = json.loads(f.read())
    return config['id']

def save_id(new_id: int):
    with open('config.json', 'r') as f:
        config = json.loads(f.read())
    config['id'] = new_id
    with open('config.json', 'w') as f:
        f.write(json.dumps(config))

    
def find_task_by_id(id: int):
    with open(TASKS_FILEPATH, 'r') as f:
        data_dict = json.loads(f.read())
    for task in data_dict['todo']:
        if task['id'] == id:
            return task
    for task in data_dict['in_progress']:
        if task['id'] == id:
            return task
    for task in data_dict['done']:
        if task['id'] == id:
            return task

def get_task_list(key: str):
    with open(TASKS_FILEPATH, 'r') as f:
        data_dict = json.loads(f.read())
    return data_dict[key]


def get_updated_time():
    return datetime.now().strftime("%d-%m-%Y, %H:%M:%S")