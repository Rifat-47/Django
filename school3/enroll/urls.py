from . import views
from django.urls import path

urlpatterns = [
    path('reg/', views.showformatdata, name='register'),
    path('success/', views.thankyou),
    
]
