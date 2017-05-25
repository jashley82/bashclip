import os

from django.core.management.base import BaseCommand
from app_bashclip.models import Command as Command_Model


class Command(BaseCommand):
    help = 'Parses bash_history and populates database'

    def handle(self, *args, **options):
        filename = '{}/.bash_history'.format(os.environ.get('HOME'))
        with open(filename, 'r') as bash_history:
            cmds = bash_history.read().split('\n')
            line_no = 0
            for cmd in cmds:
                line_no += 1
                Command_Model.objects.create(cmd_text=cmd, line_no=line_no)
                self.stdout.write(self.style.SUCCESS(cmd))
