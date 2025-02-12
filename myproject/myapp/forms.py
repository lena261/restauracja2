
from django import forms
from .models import GuestName, Reservation, Table, MyModel, DateTime

class GuestNameForm(forms.ModelForm):
    class Meta:
        model = GuestName
        fields = ['firstname', 'lastname', 'email']
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['lastname', 'TableNumber', 'guestNumber', 'dateTime']
        widgets = {
            'dateTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['TableNumber'].queryset = Table.objects.all()  

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['quantity', 'place', 'TableNumber']
