from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'this command is for importing data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        # TODO sqlite3 create table + insert into

        self.stdout.write(self.style.SUCCESS('Successfully'))