from django import forms
from . models import Hostels

class HostelForm(forms.ModelForm):
    class meta():
        model = Hostels
        fields = ['hostel_name', 'hostel_logo']
