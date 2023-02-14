from django import forms
from request.models import Announcement
from request.models import ChurchRequest
from request.models import Suggestion


class RequestForm(forms.ModelForm):
    class Meta:
        model = ChurchRequest
        fields = ['customer', 'request', 'type_choices', 'hours', 'start_date', 'end_date']


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['content']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'illustration']
