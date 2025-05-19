import os.path
from platformdirs import user_data_dir
appname = 'tracker'
appauthor = 'task-tracker-cli'

user_dir = user_data_dir(appname, appauthor)

id_filepath = os.path.join(user_data_dir(appname, appauthor), 'id.txt')
tasks_filepath = os.path.join(user_data_dir(appname, appauthor), 'tasks.json')
