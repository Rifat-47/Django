from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app1/app1 home.html')

def ehome(request):
    return render(request, 'app1/app1 homex.html')