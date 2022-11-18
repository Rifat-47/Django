from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(label_suffix='-')
    email= forms.EmailField()
    first_name= forms.CharField()
    key= forms.CharField(widget=forms.HiddenInput())