from django.urls import path
from api import views
from django.urls import re_path

from . import consumers

urlpatterns = [
    path('snippets/', views.GetHospitals.as_view()),    
    path(r'msg/', consumers.ChatConsumer.as_asgi()),
]