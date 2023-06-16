from rest_framework import serializers
from .models import HOSPITALS, BLOODBANK, OTP, DISTANCE

class HospitalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HOSPITALS
        fields = [
            'name',
            'beds',
            'icu',
            'location',
            'no_of_doc',
            'no_of_nurse',
            'a_pve',
            'a_nve',
            'ab_nve',
            'ab_pve',
            'b_pve',
            'b_nve',
            'o_nve',
            'o_pve',
        ]
        ordering = ['name']

class BloodBankSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = BLOODBANK
        fields = [
            'name',
            'location',
            'a_pve',
            'a_nve',
            'ab_nve',
            'ab_pve',
            'b_pve',
            'b_nve',
            'o_nve',
            'o_pve',
        ]
        ordering = ['name']        
class OTPSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = OTP
        fields = [
            'no',
            'otp',
        ]
        ordering = ['no']        
class DISTANCESerializer(serializers.ModelSerializer):
   

    class Meta:
        model = DISTANCE
        fields = [
            'hid',
            'uid',
        ]
        ordering = ['no']        