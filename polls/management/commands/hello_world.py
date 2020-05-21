from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('params1', nargs='?', type=str)
        
    def handle(self, *args, **options):
        param1 = options['params1']
        self.stdout.write('[#] Begin execute...')
        try:
            self.stdout.write('[#] Hello ' + str(param1))
        except Exception as e:
            print('Error:', e)
        self.stdout.write('[#] DONE!')