from django.shortcuts import render
from .models import Student
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

def thankyou(request):
    return render(request, 'enroll/success.html')

def formshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name= fm.cleaned_data['name']
            email= fm.cleaned_data['email']
            agree= fm.cleaned_data['agree']
            return HttpResponseRedirect('/success')
            #return render(request, 'enroll/success.html', {'name': name})
        return render(request, 'enroll/userregistration.html', {'form': fm})
    else:
        fm = StudentRegistration()
        return render(request, 'enroll/userregistration.html', {'form': fm})