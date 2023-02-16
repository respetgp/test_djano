from time import gmtime, strftime
from random import randint
import datetime


def show_day_night() -> list:
    hour = int(strftime("%H", gmtime()))
    if 9 < hour < 22:
        return ['day', 'день',  strftime("%H:%M:%S", gmtime())]
    else:
        return ['night', 'ночь',  strftime("%H:%M:%S", gmtime())]


def min_end_day():
    date_now = datetime.datetime.now()
    new_day = int(date_now.strftime("%d"))+1
    date_tomorrow = datetime.datetime(2023, 2, new_day)
    time_two_days = date_tomorrow - date_now
    time_two_days_minuts = int(date_now.strftime("%H"))* 60 + int(date_now.strftime("%M"))
    return time_two_days_minuts


def days_end_month():
    date_now = datetime.datetime.today()
    new_month = int(date_now.strftime("%m"))+1
    date_new_month = datetime.datetime(2023, new_month, 1)
    time_two_month = date_new_month - date_now
    time_two_month.days
    return time_two_month.days


def days_newyear():
    date_now = datetime.datetime.today()
    date_newyear = datetime.datetime(2024, 1, 1)
    d = date_newyear - date_now  # str(d)  '83 days'
    return format(d.days)
