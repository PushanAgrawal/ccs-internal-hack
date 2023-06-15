from django.shortcuts import render
import requests


from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from .models import HOSPITALS, BLOODBANK , DISTANCE, OTP

from .serializers import HospitalSerializer, BloodBankSerializer, OTPSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.views import APIView
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

import random

from api.models import Message



class GetHospitals(APIView):
    def get(self, request, format=None):
        snippets = HOSPITALS.objects.all()
        serializer = HospitalSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GetNearestHospitals(APIView):
    renderer_classes = [JSONRenderer]
    def getcurrentusers(self , lon,lat, id):
        

        
        headers = {
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'Referer': 'https://docs.mapbox.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'proximity': lon+","+lat,
            'access_token': 'pk.eyJ1IjoicGtkb24iLCJhIjoiY2xpd3dnb2RoMDI2cjNmcWZlNmxtYzVxdiJ9.qF7UqnKsXemy5I5oWoHsCA',
            'limit': '10'
        }

        response = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/hospitals.json', params=params, headers=headers)
        ans=response.json()
        hospitals=[]
        for i in ans['features']:
            name=i["text"]
            if re.search('eyes|eye|oral|dental|dentist', name):
                continue
            cordinates=(str(i["geometry"]["coordinates"][0]),str(i["geometry"]["coordinates"][1]))
            # hospitals.append((name,cordinates))  
            
 
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://docs.mapbox.com',
                'Referer': 'https://docs.mapbox.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'alternatives': 'true',
                'geometries': 'geojson',
                'language': 'en',
                'overview': 'full',
                'steps': 'true',
                'access_token': 'pk.eyJ1IjoiZXhhbXBsZXMiLCJhIjoiY2p0MG01MXRqMW45cjQzb2R6b2ptc3J4MSJ9.zA2W0IkI0c6KaAhJfk9bWg',
            }
            url='https://api.mapbox.com/directions/v5/mapbox/driving/'+lat+'%2C'+lon+'%3B'+cordinates[0]+'%2C'+cordinates[1]
            response = requests.get(
                url,
                params=params,
                headers=headers,
            )  
            resu=response.json()
            
            if len(resu["routes"])!=0:
                time=resu["routes"][0]["duration"]
                hospitals.append([name,cordinates,time])
                
        hospitals= sorted(hospitals,key=lambda x:x[2])   
        print(hospitals) 
        avaliable_hospital=[]
        for i in hospitals:
            host= HOSPITALS.objects.get(name=lower(i))       
            id=host['id']
            all_obj=DISTANCE.objects.filter(hid=id)
            no_of_beds=host.beds
            if (no_of_beds>len(all_obj)):
               avaliable_hospital.append(i)
               
        data={
            'hospitals':avaliable_hospital
        }
            
        return data
    
    def get(self , lon,lat, id):
        data=self.getcurrentusers(lon,lat,id)
        return Response(data)
    
class GETOTP(APIView):

    def get(self,request,fromat=None):
        data = JSONParser().parse(request)
        number=str(data['no'])
        otp=str(data["otp"])

        obj=OTP.objects.filter(no=number).values()
        print(obj)
        if str(obj[0]['otp'])==str(otp):
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

  
   
    

    def post(self, request,format=None):
        data = JSONParser().parse(request)
        number=str(data['no'])
        random_number = str(random.randint(100000, 999999))
        data={
            'no':number,
            'otp':random_number
        }
        serializer=OTPSerializer(data=data)
        
        
            
            
        st="The otp for your shayak app is "+random_number+". Do not share this with anyone"
        params = {
        'key': '8b628a604e7afcbb7c3f39fe40698cf916af5668',
        'number': number,
        'message': st,
        'devices': '2',
        'type': 'sms',
        'prioritize': '0',
        }

        response = requests.get('https://goyalinfocom.com/sms_app/services/send.php', params=params) 

        
        if serializer.is_valid():
            serializer.save()
            return Response( status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)

    
            






        
    
                
            
            
            



