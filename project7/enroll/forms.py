from django import forms
from .models import User

"""'__all__' shows all model fields in form """
"""shows all model fields exclude, it can be list or tuples"""
class StudentRegistration(forms.ModelForm):
    class Meta:
        model= User
        # __all__' shows all model fields in form 
        fields = '__all__'
        #fields= ['name', 'email', 'password']
        error_messages= {'name':{'required':'enter name'}}
        #shows all model fields exclude, it can be list or tuples
        #exclude = ['name']

        #fields= ['name', 'email', 'password']
