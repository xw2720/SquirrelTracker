from django.core.management.base import BaseCommand
from squirrel_tracker.models import Squirrel
import csv


class Command(BaseCommand):
    help = 'This command is to export a .csv file of squirrel database'

    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='*')

    def handle(self, *args, **kwargs):
        #path = args[0]
        #fields = Squirrel._meta.fields

        # model = apps.get_model('map','Squirrrel')
        field_names = [f.name for f in Squirrel._meta.fields]
        filename = args[0]

        with open(filename, 'w') as fn:
            writer = csv.writer(fn, delimiter=',')
            writer.writerow(field_names)

            for instance in Squirrel.objects.all():
                writer.writerow([str(getattr(instance, fn)) for fn in field_names])
            fn.close()