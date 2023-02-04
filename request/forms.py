from django import forms
from datetime import *
from request.models import Church_request
from request.models import Suggestion
from request.models import Church
from request.models import Announcement


class RequestForm(forms.ModelForm):
    class Meta:
        model = Church_request
        fields = ['customer', 'request', 'type_choices', 'hours', 'start_date', 'end_date']

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['content', 'tags']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'illustration']
