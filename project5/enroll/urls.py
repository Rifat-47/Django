from . import views
from django.urls import path

urlpatterns = [
    #path('', views.stinfo, name='stu-home'),
    path('', views.formshow, name='register'),
    
]
