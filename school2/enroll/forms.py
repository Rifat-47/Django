from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(help_text='just put your name')
    email= forms.EmailField()