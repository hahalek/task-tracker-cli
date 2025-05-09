import pytest
from tracker.tracker import *
from time import sleep
import json
from tracker.utils import *

with open('config.json', 'r') as f:
    config = json.loads(f.read())

TASKS_FILEPATH = config['TASKS_FILEPATH']


def test_task_object():
    task = Task('Finish Task Tracker CLI tool')
    result = type(task)
    print(f'FROM DESCRIPTION ID={task.id}, descr={task.description}, status={task.status}, created_at={task.created_at}, updated_at={task.updated_at}')
    assert result == Task

def test_task_has_id():
    task = Task('Zrobic zakupy')
    result = type(task.id)
    assert result == int

def test_create_task_from_dict():
    d = {
        'id': 86,
        'description': 'Zadanie bojowe',
        'status': 'in_progress',
        'created_at': '31-05-1997, 11:41:54',
        'updated_at': '31-05-1997, 17:23:07'
    }
    task = Task(d)
    print(f'FROM DICT ID={task.id}, descr={task.description}, status={task.status}, created_at={task.created_at}, updated_at={task.updated_at}')
    assert type(task) == Task
    

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
    tracker.add('Java')
    tracker.add('LabVIEW')
    tracker.delete(1)
    todo_len = len(get_todo_list())
    task_desc = find_task_by_id(2)['description']
    assert todo_len == 3
    assert task_desc == 'SQL'

