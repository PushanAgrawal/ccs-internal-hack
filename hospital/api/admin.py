from django.contrib import admin
from .models import HOSPITALS , BLOODBANK, DISTANCE,USER,OTP

admin.site.register(HOSPITALS)
admin.site.register(BLOODBANK)
admin.site.register(DISTANCE)
admin.site.register(USER)
admin.site.register(OTP)