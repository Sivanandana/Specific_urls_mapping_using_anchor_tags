from django.urls import path
from app3.views import *
app_name='siva3'
urlpatterns = [
    path('siva3/',siva3,name='siva3'),
]