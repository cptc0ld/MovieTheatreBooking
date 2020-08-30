"""
WSGI config for plazabooking project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import threading
import schedule
import time
import requests


def task():
    url = "http://127.0.0.1:8000/api/expired/"
    r = requests.put(url, data=None)
    r = requests.delete(url, data=None)


class CheckThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        print("Watching for expired Tickets")
        schedule.every(5).minutes.do(task)
        while True:
            schedule.run_pending()
            time.sleep(300)


CheckThread().start()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plazabooking.settings')

application = get_wsgi_application()
