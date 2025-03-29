from .models import Trade, Enter_Trade, Exit_Trade, OptionsTrade
from django import forms

class CreateFutures(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    entry_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'})) 
    exit_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'})) 

    class Meta:
        model = Trade
        fields = [
            'user', 'ticker', 'long', 'short', 'entry_price', 'average_down', 'reasons_entry', 'profit', 'loss', 'p_and_l', 
            'trim1', 'trim2', 'exit_price', 'reasons_exit', 'picture1', 'picture2', 'date', 'entry_time', 'exit_time', 'quantity'
        ]
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the form initialization
        super().__init__(*args, **kwargs)

        if user:
            # Filter choices so the user only sees their own reasons
            self.fields['reasons_entry'].queryset = Enter_Trade.objects.filter(user=user)
            self.fields['reasons_exit'].queryset = Exit_Trade.objects.filter(user=user)

class CreateOptions(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    entry_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    exit_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = OptionsTrade
        fields = [
            'user', 'ticker', 'call', 'put', 'stock_price','option_price', 'exit_option_price', 'reasons_entry', 'profit', 'loss', 'p_and_l', 
            'trim1', 'trim2', 'reasons_exit', 'picture1', 'picture2', 'date', 'entry_time', 'exit_time', 'quantity'
        ]
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the form initialization
        super().__init__(*args, **kwargs)

        if user:
            # Filter choices so the user only sees their own reasons
            self.fields['reasons_entry'].queryset = Enter_Trade.objects.filter(user=user)
            self.fields['reasons_exit'].queryset = Exit_Trade.objects.filter(user=user)

class CreateEntry(forms.ModelForm):
    class Meta:
        model = Enter_Trade
        fields = ['reason',]

class CreateExit(forms.ModelForm):
    class Meta:
        model = Exit_Trade
        fields = ['reason',]