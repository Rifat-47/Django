from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        """super().clean() method can't deal with empty value"""
        cleaned_data= super().clean()
        vname= self.cleaned_data.get('name')
        if len(vname) < 4:
            raise forms.ValidationError('name must have min 4 letter!')
        vemail= self.cleaned_data.get('email')
        if len(vemail) < 10:
            raise forms.ValidationError('email must have 10 letter!')
            