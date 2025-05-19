import argparse
from .model import *

def main(command_line=None):

    parser = argparse.ArgumentParser(
        prog="tracker",
        description="Tracker is a task manager CLI tool")

    subparsers = parser.add_subparsers(dest='command',
                                       help="Usage: tracker <command> [argument]")

    list_tasks = subparsers.add_parser('list', help="list [(optional) status] \t\t\t Lists all tasks in a table. Adding optional argument [todo/in-progress/done] lists those specific tasks.")
    list_tasks.add_argument('mode', nargs='?', default='all', type=str)

    add = subparsers.add_parser('add', help="add [description] [(optional) status] \t\t\t Adds a task with specified description. By default task is added to todo list. Adding optional status [in-progress/done] adds tasks to specified list.")
    add.add_argument('description', type=str, help='add help')
    add.add_argument('status', nargs='?', default='todo', type=str)

    mark_in_progress = subparsers.add_parser('mark-in-progress', help="mark-in-progress [id] \t\t\t Changes status of a task with id 'id' to in-progress and moves it to in-progress list. Id od a task can be check with 'list' command.")
    mark_in_progress.add_argument('id', type=int)

    mark_done = subparsers.add_parser('mark-done', help="mark-done [id] \t\t\t Changes status of a task with id 'id' to done and moves it to doen list. Id of a task can be checked with 'list' command.")
    mark_done.add_argument('id', type=int)

    update = subparsers.add_parser('update', help="update [id] [new description] \t\t\t Changes description of a task with id 'id' to new description. Id of a task can be checked with 'list' command.")
    update.add_argument('label')
    update.add_argument('new_description', type=str)

    delete = subparsers.add_parser('delete', help="delete [id] \t\t\t Deletes task with specified id. Id of a task can be checked by 'list' command.")
    delete.add_argument('id', type=int)

    reset = subparsers.add_parser('reset', help="\t reset \t\t\t Delete all tasks. Sets id counter back to 0.")


    args = parser.parse_args(command_line)

    tracker = Tracker()

    if args.command == 'add':
        tracker.add(args.description, args.status)
    elif args.command == 'update':
        if args.label.isdigit():
            args.label = int(args.label)
        tracker.update(args.label, args.new_description)
    elif args.command == 'delete':
        tracker.delete(args.id)
    elif args.command == 'mark-in-progress':
        tracker.mark(args.id, 'in-progress')
    elif args.command == 'mark-done':
        tracker.mark(args.id, 'done')
    elif args.command == 'list':
        tracker.list(args.mode)
    elif args.command == 'reset':
        tracker.reset()


if __name__ == '__main__':
    main()