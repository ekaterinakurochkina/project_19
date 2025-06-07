from celery import shared_task
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule
import json



