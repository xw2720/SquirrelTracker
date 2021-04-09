from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from squirrel_tracker.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    help = 'this command is for importing data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        # do sqlite3 create table + insert into
        # run migrating first!
        # python manage.py makemigrations
        # python manage.py migrate --run-syncdb

        path = kwargs['path']
        try:
            with open(path, encoding='utf-8') as fn: #fn = file name
                reader = csv.DictReader(fn)
                for i in reader:
                    s = Squirrel(
                        Longitude=i['X'],
                        Latitude=i['Y'],
                        Unique_squirrel_id=i['Unique Squirrel ID'],
                        Shift=i['Shift'],
                        Date=datetime.date(
                            int(i['Date'][-4:]), int(i['Date'][:2]), int(i['Date'][2:4])),
                        Age=i['Age'],
                        Primary_fur_color=i['Primary Fur Color'],
                        Location=i['Location'],
                        Specific_location=i['Specific Location'],
                        Running=i['Running'].capitalize(),
                        Chasing=i['Chasing'].capitalize(),
                        Climbing=i['Climbing'].capitalize(),
                        Eating=i['Eating'].capitalize(),
                        Foraging=i['Foraging'].capitalize(),
                        Other_activities=i['Other Activities'],
                        Kuks=i['Kuks'].capitalize(),
                        Quaas=i['Quaas'].capitalize(),
                        Moans=i['Moans'].capitalize(),
                        Tail_flags=i['Tail flags'].capitalize(),
                        Tail_twitches=i['Tail twitches'].capitalize(),
                        Approaches=i['Approaches'].capitalize(),
                        Indifferent=i['Indifferent'].capitalize(),
                        Runs_from=i['Runs from'].capitalize(),
                    )
                    s.save()
        except csv.Error as e:
            print(f'there is error with {reader.line_num}')
        self.stdout.write(self.style.SUCCESS('Successfully'))