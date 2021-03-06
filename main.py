#!/usr/bin/env python3

# main.py
# SENG3011 - Cool Bananas
#
# The main entry point into running the Django server, and starting the program.
# It updates the server when necessary, and allows the server to be accessed via the web.


if __name__ == '__main__':

    import json
    import os
    import sys

    from django.core.management import execute_from_command_line

    with open('config.json') as f:
        config = json.loads(f.read())

    os.environ.setdefault('SECRET_KEY', config['secret_key'])
    os.environ.setdefault('DEBUG', str(config['debug']))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seng.settings")

    if len(sys.argv[1:]):
        execute_from_command_line(['main.py'] + sys.argv[1:])
    else:
        execute_from_command_line(['main.py', 'runserver', '127.0.0.1:5002', '--noreload'])
