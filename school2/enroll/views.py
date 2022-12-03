from django.shortcuts import render
from .models import Student
from .forms import StudentRegistration

# Create your views here.
def stinfo(request):
    stud = Student.objects.all()
    return render(request, 'enroll/stinfo.html', {'stu': stud})


def showformatdata(request):
    fm= StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})

