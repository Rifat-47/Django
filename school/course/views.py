from datetime import datetime
from django.shortcuts import render

# Create your views here.

def home(request):
    text= {'time':datetime.now(), 'name':'rifat', 
            'art':'in SQL, the TRUNCATE TABLE statement is a Data Definition Language operation that marks the extents of a table for deallocation. The result of this operation quickly removes all data from a table, typically bypassing a number of integrity enforcing mechanisms.',
            'names':['rifat', 'mon', 'tusher', 'sourav']}
    return render(request, 'course/home.html', text)