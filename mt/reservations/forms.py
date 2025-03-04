from django import forms
from .models import Reservation, ReservationStatus

class ReservationForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'status']

class ReservationStatusForm(forms.ModelForm):
    class Meta:
        model = ReservationStatus
        fields = ['name']
