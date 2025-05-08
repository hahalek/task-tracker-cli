import pytest
from tracker import *
from time import sleep
import json


json_filepath = r'tasks_database.json'

def find_task_by_id(id: int):
    with open(json_filepath, 'r') as f:
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
    with open(json_filepath, 'r') as f:
        data_dict = json.loads(f.read())
    return data_dict['todo']



def test_task_object():
    task = Task('Finish Task Tracker CLI tool')
    result = type(task)
    print(f'ID={task.id}, descr={task.description}, status={task.status}, created_at={task.created_at}, updated_at={task.updated_at}')
    assert result == Task

def test_task_has_id():
    task = Task('Zrobic zakupy')
    result = type(task.id)
    assert result == int

def test_new_task_has_id_increased_by_one():
    task1 = Task('Zadanie 1')
    task2 = Task('Zadanie 2')
    result = task2.id - task1.id
    assert result == 1

def test_add_new_task():
    tracker = Tracker()
    desc = 'Zrobic pranie'
    tracker.add(desc)
    result = find_task_by_id(1)['description']
    assert result == desc

def test_update_task():
    tracker = Tracker()
    desc = 'Rower'
    tracker.add('Spacer')
    sleep(2)
    tracker.update(1, desc)
    task_desc = find_task_by_id(1)['description']
    task_created_time = find_task_by_id(1)['created_at']
    task_updated_at = find_task_by_id(1)['updated_at']
    assert task_desc == desc
    assert task_created_time != task_updated_at


def test_delete_task():
    tracker = Tracker()
    tracker.add('Python')
    tracker.add('SQL')
    tracker.delete(1)
    todo_len = len(get_todo_list())
    task_desc = find_task_by_id(2)['description']
    assert todo_len == 1
    assert task_desc == 'SQL'
