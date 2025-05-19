Install
Open terminal in directory with pyproject.toml and install with pip (pip install --user .).

Uninstal
Uninstall on Windows with "py -m pip uninstall tracker". On Unix/macOS with "python -m pip uninstall tracker".

Description
This is a simple Command Line Interface tool for task tracking. From command line you can track your doto, in progress and done task list and view them in table.

Usage
tracker <command> [argument]

list [(optional) status]                       Lists all tasks in a table. Adding optional argument [todo/in-progress/done] lists those specific tasks.
add [description] [(optional) status]          Adds a task with specified description. By default task is added to todo list. Adding optional status [in-progress/done] adds tasks to specified list.
mark-in-progress [id]                          Changes status of a task with id 'id' to in-progress and moves it to in-progress list. Id od a task can be check with 'list' command.
mark-done [id]                                 Changes status of a task with id 'id' to done and moves it to doen list. Id of a task can be checked with 'list' command.
update [id] [new description]                  Changes description of a task with id 'id' to new description. Id of a task can be checked with 'list' command.
delete [id]                                    Deletes task with specified id. Id of a task can be checked by 'list' command.
reset                                          Delete all tasks. Sets id counter back to 0.