from django.core.management.base import BaseCommand
from django.utils import timezone
import time, os, schedule, requests


class Command(BaseCommand):
    '''Deletes cache on an interval of 1 hour. This will force an API call 
    only when our fetch_data function will see no data in the cache folder.'''

    help = 'Wipes cached json/txt files'

    def update_data():
        print('deleting cache...')
        dir = 'cache/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

    schedule.every(1).hours.do(update_data)

    while True:
        schedule.run_pending()
        time.sleep(1)