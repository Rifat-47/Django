from . import views
from django.urls import path

urlpatterns = [
    path('reg', views.formshow, name='register'),
    path('success', views.thankyou, name='success'),
    
]
