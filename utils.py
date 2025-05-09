import json
import globals

TASKS_FILEPATH = globals.TASKS_FILEPATH

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

def get_todo_list():
    with open(TASKS_FILEPATH, 'r') as f:
        data_dict = json.loads(f.read())
    return data_dict['todo']