import cmd
from datetime import datetime

class Task():
    def __init__(self, description: str):
        with open('id.txt', 'r') as f:
            id = int(f.read())
            new_id = id + 1
        
        timestamp = datetime.now()

        self.id = new_id
        self.description = description
        self.status = 'todo'
        self.created_at = timestamp
        self.updated_at = timestamp

        with open('id.txt', 'w') as f:
            f.write(str(new_id))

class Tracker(cmd.Cmd):
    prompt = '--> '
    intro = 'Welcome in Task Tracker CLI.'
    def add(self, description: str):
        # Create new task with todo status and ID, add createdAt and updatedAt timestamps
        pass

    def update(self, description: str = None, id: int = None,):
        #if description or id of the task is given
        pass
    
