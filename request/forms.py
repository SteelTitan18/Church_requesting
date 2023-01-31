from django import forms
from datetime import *
from request.models import Church_request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Church_request
        fields = '__all__'

