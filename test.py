import pytest
from tracker import *
from time import sleep

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
    tracker.add('Zrobic pranie')

def test_update_task():
    tracker = Tracker()
    tracker.add('Spacer')
    sleep(2)
    tracker.update(7, 'Rower')