Project idea from: https://roadmap.sh/projects/task-tracker  
  
## Install  

```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Clone the repository
pip install git+https://github.com/hahalek/task-tracker-cli

```
  
## Uninstal  
Uninstall on Windows with "py -m pip uninstall tracker". On Unix/macOS with "python -m pip uninstall tracker".  
  
## Description  
This is a simple Command Line Interface tool for task tracking. You can view your tasks in easly readible table, add new tasks, mark thier status as in-progress or done, update task description, delete a single task or reset whole todo list.  
  
## Usage  
tracker [command] [argument]  

| Syntax      | Description |
| ----------- | ----------- |
| list [(optional) status]      | Lists all tasks in a table. Adding optional argument [todo/in-progress/done] lists those specific tasks. |
| add [description] [(optional) status]      | Adds a task with specified description. By default task is added to todo list. Adding optional status [in-progress/done] adds tasks to specified list. |
| mark-in-progress [id]      | Changes status of a task with id 'id' to in-progress and moves it to in-progress list. Id od a task can be check with 'list' command. |
| mark-done [id]      | Changes status of a task with id 'id' to done and moves it to doen list. Id of a task can be checked with 'list' command. |
| update [id] [new description]      | Changes description of a task with id 'id' to new description. Id of a task can be checked with 'list' command. |
| delete [id]      | Deletes task with specified id. Id of a task can be checked by 'list' command. |
| reset      | Deletes all tasks. Sets id counter back to 0. |
