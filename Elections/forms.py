from django import forms
from Accounts.models import Participant
from .models import ElectoralProcess



class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name','last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control'})
        }
class ElectoralProcessForm:
    class Meta:
        model = ElectoralProcess
        fields = ['no_of_voters','start_date', 'end_date','name','email']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control'})
        }