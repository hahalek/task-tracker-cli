import json
from os.path import exists
from os import makedirs
from .environment import *


def check_if_data_files_exist():
    if not exists(id_filepath):
        makedirs(user_dir, exist_ok=True)
        with open(id_filepath, 'w') as f:
            data = 0
            f.write(str(data))
    if not exists(tasks_filepath):
        makedirs(user_dir, exist_ok=True)
        with open(tasks_filepath, 'w') as f:
            data = '{"todo": [], "in_progress": [], "done": []}'
            f.write(data)


def get_id():
    with open(id_filepath, 'r') as f:
        id = int(f.read())
    return id

def save_id(new_id: int):
    with open(id_filepath, 'w') as f:
        f.write(str(new_id))

    
def find_task_by_id(id: int):
    with open(tasks_filepath, 'r') as f:
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
    with open(tasks_filepath, 'r') as f:
        data_dict = json.loads(f.read())
    return data_dict[key]

