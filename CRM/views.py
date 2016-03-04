# -*- encoding: utf-8 -*-

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
from decorators import *
import settings
import re
import datetime as dt
import calendar as cl

@login_required
def start(request):
    customers = Customer.objects.filter(user = request.user)
    return render(request, 'customer.html', { 'customers':customers })

#@any_permission_required('benzin.benif')
@login_required
def calendar(request, year=None, month=None):
    customer = None
    if request.GET.has_key('customer_id'):
        customer = Customer.objects.get(pk=request.GET['customer_id'])
    if year is None or month is None:
        start_date = dt.datetime.strptime('%s.%s' %(dt.datetime.now().month, dt.datetime.now().year), '%m.%Y')
    else:
        start_date = dt.datetime.strptime('%s.%s' %(month, year), '%m.%Y')
    offset = start_date.weekday()+cl.monthrange(start_date.year, start_date.month)[1]
    if offset == 28:
        weeks = [0,1,2,3]
    elif offset > 28 and offset < 36:
        weeks = [0,1,2,3,4]
    else:
        weeks = [0,1,2,3,4,5]
    return render(request, 'calendar.html', { 'offset':offset, 'customer':customer, 'prev':(start_date+dt.timedelta(days=-1)), 'next':(start_date+dt.timedelta(days=32)), 
        'cal_date':start_date, 'start_date':start_date.strftime('%m.%Y'), 'weeks':weeks, 'days':[0,1,2,3,4,5,6] })

@login_required
def event_edit(request, event_pk=None):
    if request.GET.has_key('customer_id') and not request.GET.has_key('date'):
        return redirect('/?customer_id='+request.GET['customer_id'])
    elif not request.GET.has_key('customer_id') and request.GET.has_key('date'):
        return redirect('/?date='+request.GET['date'])
    elif request.GET.has_key('customer_id') and request.GET.has_key('date'):
        if request.POST:
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('calendar', request.GET['date'][-4:], request.GET['date'].split('.')[1])
        else:
            evdt = dt.datetime.strptime(request.GET['date'], '%d.%m.%Y')
            form = EventForm(initial={ 'dt':evdt, 'customer':Customer.objects.get(pk=request.GET['customer_id'])})
        return render(request, 'event.html', { 'form':form })
    else:
        return redirect('calendar')

@login_required
def customer_edit(request, customer_pk=None):
    if request.POST:
        if customer_pk and Customer.objects.get(pk=customer_pk).user == request.user:
            form = CustomerForm(request.POST, request.FILES, instance=Customer.objects.get(pk=customer_pk))    
        else:
            form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('start')
    elif customer_pk and Customer.objects.get(pk=customer_pk).user == request.user:
        form = CustomerForm(instance=Customer.objects.get(pk=customer_pk))
    else:
        form = CustomerForm(initial={ 'user':request.user })
    return render(request, 'customer_edit.html', { 'form':form })






