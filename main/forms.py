from .models import Trade, Enter_Trade, Exit_Trade
from django import forms

class CreateTrade(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    entry_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'})) 
    exit_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'})) 

    class Meta:
        model = Trade
        fields = [
            'ticker', 'long', 'short', 'entry_price', 'average_down', 'reasons_entry', 'profit', 'loss', 'p_and_l', 
            'trim1', 'trim2', 'exit_price', 'reasons_exit', 'picture1', 'picture2', 'date', 'entry_time', 'exit_time'
        ]

class CreateEntry(forms.ModelForm):
    class Meta:
        model = Enter_Trade
        fields = '__all__'

class CreateExit(forms.ModelForm):
    class Meta:
        model = Exit_Trade
        fields = '__all__'