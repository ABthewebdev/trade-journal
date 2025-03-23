from .models import Trade
from django import forms

class CreateTrade(forms.ModelForm):
    model = Trade
    fields = '__all__'