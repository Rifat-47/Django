import django
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration

# Create your views here.
def thankyou(request):
    return render(request, 'enroll/success.html')

def showformatdata(request):
    if request.method == 'POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            name= fm.cleaned_data['name']
            email= fm.cleaned_data['email']
            #return render(request, 'enroll/success.html', context= {'nm':name})
            return HttpResponseRedirect('/success/')
    else:    
        fm= StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})

