from django import forms
from django.forms import fields
from django.forms.widgets import Textarea 
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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

class SingUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    class meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    # def authenticate_user(self, request):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password1']
    #     user = authenticate(username=username, password=password)
    #     login(request, user)

