from django.urls import path
from .views import person_form, success

urlpatterns = [
    path('', person_form, name='person_form'),
    path('success/', success, name='success'),  # Add this line
]
