from django.shortcuts import render
from django.http import HttpResponse
from request.models import Church_request
from request.models import Church
from request.forms import RequestForm
from django.shortcuts import redirect
from datetime import *

def church_main(request, church_id):
    church = Church.objects.get(id=church_id)
    return render(request, 'request/church_main.html', {'church': church})

def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            _request = form.save(commit=False)
            if (_request.type_choices == "solo"):
                _request.end_date = _request.start_date
                #_request = form.save()
            _request = form.save(commit=False)
            return redirect('request-confirm', _request.customer, _request.request, _request.type_choices, _request.hours, _request.start_date, _request.end_date)
    else:
        form = RequestForm()
    return render(request, 'request/request_create.html', {'form':form})

def request_detail(request, request_id):
    request = Church_request.objects.get(id=request_id)
    return render(request, 'request/request_detail.html', {'request': request})

def request_confirm(request, _customer, requet, _type_choices, _hours, _start_date, _end_date):
    #_request = Church_request.objects.get(id=request_id)
    #_request = Church_request()
    form = RequestForm(request.POST)
    form.fields['customer'].value = _customer
    form.fields['request'].value = requet
    form.fields['type_choices'].value = _type_choices
    form.fields['hours'].value = _hours
    form.fields['start_date'].value = _start_date
    form.fields['end_date'].value = _end_date
    if form.is_valid():
        _request = form.save()
        return redirect('request-detail', _request.id)
    return render(request, 'request/myTemplate.html', {'forms': form})

def request_list(request):
    list = Church_request.objects.all()
    return render(request, 'request/request_list.html', {'lists' : list})

def acceuil(request):
    church_list = Church.objects.all()
    return render(request, 'request/acceuil.html', {'list' : church_list})

def confirmation(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            _request = form.save()
            #return render(request, 'request/acceuil.html')
    else:
        form = RequestForm()
    #requests = Church_request.objects.get(id=request_id)
    return render(request, 'request/request_detail.html', {'requests':_request})
