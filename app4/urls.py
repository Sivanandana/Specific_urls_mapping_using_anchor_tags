from django.urls import path
from app4.views import *
app_name='siva4'
urlpatterns = [
    path('siva4/',siva4,name='siva4'),
]