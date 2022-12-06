from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)
    def clean_name(self):
        valname= self.cleaned_data.get('name')
        if len(valname) < 4:
            raise forms.ValidationError('name must have at least 4 letter!')
        return valname
    def clean_email(self):
        valemail= self.cleaned_data.get('email')
        r = ['a', 'b']
        for i in r:
            if i not in valemail:
                raise forms.ValidationError('email must contain r list')
        return valemail
        