from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(label='your name', label_suffix=":-", initial='rifat',
        help_text='put your name', widget=forms.TextInput(attrs={'class':'css1', 'id':'uniqueid'}))
    email= forms.EmailField()
    first_name= forms.CharField()
    keyz= forms.CharField(widget=forms.HiddenInput())