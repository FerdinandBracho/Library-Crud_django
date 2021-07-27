from django import forms
from django.forms.widgets import Textarea 
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=25)
    message = forms.CharField(widget=Textarea)

    def load_in_db(self):
        # !Instancioamos el modelo
        contact = Contact()

        # !Cargamos los datos a cada campo
        contact.name = self.cleaned_data['name']
        contact.email = self.cleaned_data['email']
        contact.phone = self.cleaned_data['phone']
        contact.message = self.cleaned_data['message']

        # !Guardamos en base de datos 
        contact.save()

