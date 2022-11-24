from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformatdata(request):
    if request.method == 'POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            return render(request, 'enroll/success.html', context= {'name':nm})
    else:    
        fm= StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
    fm= StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})