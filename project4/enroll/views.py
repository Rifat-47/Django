from django.shortcuts import render
from .models import Student
from .forms import StudentRegistration

def formshow(request):
    fm = StudentRegistration(auto_id=True, initial={'name':'rifat', 'email':'rifat@gmail.com'})
    fm.order_fields(field_order=['name', 'first_name'])
    return render(request, 'enroll/userregistration.html', {'form': fm})

# Create your views here.
#def stinfo(request):
 #   stud = Student.objects.all()
  #  return render(request, 'enroll/stinfo.html', {'stu': stud})


#def showformatdata(request):
 #   fm= StudentRegistration()
  #  return render(request, 'enroll/userregistration.html', {'form':fm})

