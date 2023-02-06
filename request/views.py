from django.shortcuts import render
from django.http import HttpResponse
from request.models import Church_request
from request.models import Church
from request.forms import RequestForm
from request.models import Suggestion
from request.forms import SuggestionForm
from request.forms import AnnouncementForm
from request.models import Announcement
from django.shortcuts import redirect
from datetime import *

def church_main(request, church_id):
    church = Church.objects.get(id=church_id)
    return render(request, 'request/church_main.html', {'church': church, 'header_title' : church.name})

# def tagsInputTest(request):
#     if request.method == 'POST':
#         suggestion = Suggestion()
#         form = SuggestionForm(request.POST)
#         if form.is_valid():
#             suggestion = form.save()
#     else:
#         form = SuggestionForm()
#
#     return render(request, 'request/test.html', {'form':form})

def suggestion_create(request, church_id):
    church = Church.objects.get(id = church_id)
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            # ajouter l'église concernée
            suggestion.save()
            form.save_m2m()
    else:
        form = SuggestionForm()

    return render(request, 'request/suggestions.html', {'form':form, 'header_title':church.name + " : Boîte à suggestions"})


def request_create(request, church_id):
    church = Church.objects.get(id=church_id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            _request = form.save(commit=False)
            if (_request.type_choices == "solo"):
                _request.end_date = _request.start_date
                #_request = form.save()
            _request.church = church
            _request = form.save()
            return redirect('request-confirm', _request.customer, _request.request, _request.type_choices, _request.hours, _request.start_date, _request.end_date)
    else:
        form = RequestForm()
    return render(request, 'request/request_create.html', {'church': church, 'form':form, 'header_title' : church.name + " : Demande de messe" })

def announcement(request, church_id):
    _church = Church.objects.get(id=church_id)
    announcement_list = list(Announcement.objects.filter(announcement_church_id = _church.id))

    return render(request, 'request/announcement.html', {'announcement_list':announcement_list, 'header_title':_church.name + " : Annonces"})

# def announcement_admin(request, church_id):
#     church = Church.objects.get(id=church_id)
#     if request.method == 'POST':
#         announcement = Announcement()
#         announcement.church = church
#         form = AnnouncementForm(request.POST, instance=announcement)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AnnouncementForm()
#
#     return render(request, 'request/announcement.html', {'church':church, 'form':form, 'header_title':church.name + " : Annonces"})


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
    return render(request, 'request/acceuil.html', {'list' : church_list, 'header_title' : "DEMANDE DE MESSE"})

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
