from django import forms
from .models import Book
from django.core import validators

class Add_Book_Informations(forms.ModelForm):
    class Meta:
        model=Book
        fields=['Author','Title']

        widgets={
            'Author':forms.TextInput( attrs={'class':'form-control','placeholder':"Enter your Name",}),
            'Title':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your Book's Title"}),
        }