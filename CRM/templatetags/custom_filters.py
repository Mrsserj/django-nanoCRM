# -*- encoding: utf-8 -*-

from django import template
from CRM.models import Customer, Calendar 
import datetime as dt
import calendar as cl
#import locale
#locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from CRM.settings import MEDIA_URL

register = template.Library()

monthNames = [
    u'Января',
    u'Февраля',
    u'Марта',
    u'Апреля',
    u'Мая',
    u'Июня',
    u'Июля',
    u'Августа',
    u'Сентября',
    u'Октября',
    u'Ноября',
    u'Декабря',
]

def get_events(user, sd, customer=None):
    ed = sd+dt.timedelta(days=1)
    result = '<ul class="events">'
    if customer:
        cal = Calendar.objects.filter(customer__user=user, dt__gte=sd, dt__lt=ed, customer=customer)
    else:
        cal = Calendar.objects.filter(customer__user=user, dt__gte=sd, dt__lt=ed)
    for ev in cal:
        rendered = render_to_string('tooltip.html', { 'MEDIA_URL':MEDIA_URL, 'cal': ev })
        result += '<li><a href="#" rel="tooltip" title="' + rendered + '">%s %s</a></li>' %((dt.timedelta(hours=8)+ev.dt).strftime('%H:%M'), ev.name)
    result += '</ul>'
    return result

@register.simple_tag(takes_context=True)
def get_day(context):
    user = context['user']
    week = context['week']
    day = context['day']
    customer = context['customer']
    start_date = dt.datetime.strptime(context['start_date'], '%m.%Y')
    #end_date = dt.datetime.strptime(cl.monthrange(start_date.year, start_date.month)[1]+'.'+context['start_date'], '%d.%m.%Y')
    offset = start_date.weekday()
    days = week*7+day-offset
    rez = start_date+dt.timedelta(days=days)
    result = "<td " 
    if rez.strftime('%d.%m.%Y') == dt.datetime.now().strftime('%d.%m.%Y'):
        result += ' class="current">'
    elif (week+day) % 2 == 0:
        result += ' class="light">'
    else:
        result += ' class="dark">'
    if not start_date.month == rez.month and not rez.day == 1:
        result += '<span style="color:#d0d0d0;">%s</span>' %rez.day
    elif not start_date.month == rez.month and rez.day == 1:
        result += '<span style="color:#d0d0d0;">%s %s</span>' %(rez.day, monthNames[rez.month-1])
    elif start_date.month == rez.month and rez.day == 1:
        result += '<span>%s %s</span>' %(rez.day, monthNames[rez.month-1])
    else:
        result += str(rez.day)
    if customer:
        result += get_events(user, rez, customer) + '<a href=\'' + reverse('event') + '?customer_id=' + str(customer.id) + '&date=' + rez.strftime('%d.%m.%Y')+'\'><i class="glyphicon glyphicon-tag"></i></a></td>'
    else:
        result += get_events(user, rez, customer) + '</td>'    
    return result


