from django import forms
from .models import Clients
class ClientsForms(forms.ModelForm):
    class Meta:
        model = Clients
        fields= ['name','phone_number','notes']