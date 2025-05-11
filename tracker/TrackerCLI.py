import argparse
from model import *

def main(command_line=None):

    parser = argparse.ArgumentParser(
        prog="tracker",
        description="Tracker is a task manager CLI tool")

    subparsers = parser.add_subparsers(dest='command')

    add = subparsers.add_parser('add', help='add help')
    add.add_argument('description', type=str, help='add help')
    add.add_argument('status', nargs='?', default='todo', type=str)

    update = subparsers.add_parser('update')
    update.add_argument('label')
    update.add_argument('new_description', type=str)

    delete = subparsers.add_parser('delete')
    delete.add_argument('id', type=int)

    mark_in_progress = subparsers.add_parser('mark-in-progress')
    mark_in_progress.add_argument('id', type=int)

    mark_done = subparsers.add_parser('mark-done')
    mark_done.add_argument('id', type=int)

    list_tasks = subparsers.add_parser('list')
    list_tasks.add_argument('mode', nargs='?', default='all', type=str)

    reset = subparsers.add_parser('reset')


    args = parser.parse_args(command_line)

    tracker = Tracker()

    if args.command == 'add':
        tracker.add(args.description, args.status)
    elif args.command == 'update':
        if args.label.isdigit():
            args.label = int(args.label)
        tracker.update(args.label, args.new_description)
        print(f'Running: tracker update {args.label} {args.new_description}')
    elif args.command == 'delete':
        tracker.delete(args.id)
        print(f'Running: tracker delete {args.id}')
    elif args.command == 'mark-in-progress':
        tracker.mark(args.id, 'in-progress')
        print(f'Running: tracker mark-in-progress {args.id}')
    elif args.command == 'mark-done':
        tracker.mark(args.id, 'done')
        print(f'Running: tracker mark-done {args.id}')
    elif args.command == 'list':
        tracker.list(args.mode)
    elif args.command == 'reset':
        tracker.reset()


if __name__ == '__main__':
    main()