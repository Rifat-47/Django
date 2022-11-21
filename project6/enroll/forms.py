from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=50, strip=True, 
    error_messages={'required':'enter your name!'})
    email= forms.EmailField()
    agree= forms.BooleanField()
    date= forms.DateField()