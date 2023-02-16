from django.http import HttpResponse
from django.shortcuts import render
from page.logic import show_day_night, min_end_day, days_newyear, days_end_month
# Create your views here.


def show_page_day_night(request):

    lst = show_day_night()
    minuts_ed = min_end_day()
    days_ny = days_newyear()
    days_em = days_end_month()

    mycontext = {
        'day': lst[0],
        'day_russian': lst[1],
        'time': lst[2],
        'minuts_end_day': minuts_ed,
        'days_ny': days_ny,
        'days_to_end_month': days_em
    }

    return render(request, template_name='days_template.html', context=mycontext)
