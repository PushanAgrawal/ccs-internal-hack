from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('apis', views.GetNearestHospitals.as_view()),
    path('otp', (views.GETOTP.as_view())),
   
    
]