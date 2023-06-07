from rest_framework import serializers
from .models import HOSPITALS, BLOODBANK

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