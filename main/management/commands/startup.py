from subprocess import Popen
from sys import stdout, stdin, stderr
import time, os, signal
from django.core.management.base import BaseCommand

# A custom Django command that handles our regular runserver command
# and our custom update_data command at the same time with one command
# >>> python manage.py startup

class Command(BaseCommand):
    help = 'Run all commands'
    commands = [
        'python manage.py update_data',
        'python manage.py runserver'
    ]

    def handle(self, *args, **options):
        proc_list = []

        for command in self.commands:
            print("$ " + command)
            proc = Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)
            proc_list.append(proc)

        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            for proc in proc_list:
                os.kill(proc.pid, signal.SIGKILL)