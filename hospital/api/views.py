from django.shortcuts import render
import requests
import re

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

def getcurrentusers( lon, lat):
    
        

        
    url = "https://api.geoapify.com/v2/places?categories=healthcare.hospital&filter=circle:"+lon+","+lat+",5000&bias=proximity:"+lon+","+lat+"&limit=20&apiKey=7e6937c7b9a74890be81ba8fd55c79bf"
          
    response = requests.get(url)
    ans=response.json()
    hospitals=[]
    hospitals1=[]
    for i in ans['features']:
        name=i["properties"]["name"]
        if re.search('eyes|eye|oral|dental|dentist|Eye|Eyes|Oral|Dental', name):
            continue
        cordinates=(str(i["properties"]["lon"]),str(i["properties"]["lat"]))
        hospitals.append((name,cordinates))  

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
        url='https://api.mapbox.com/directions/v5/mapbox/driving/'+lon+'%2C'+lat+'%3B'+cordinates[0]+'%2C'+cordinates[1]
        response = requests.get(
            url,
            params=params,
            headers=headers,
        )  
        resu=response.json()

        
        if len(resu["routes"])!=0:
            time=resu["routes"][0]["duration"]
            hospitals1.append([name,cordinates,time])
 

    avaliable_hospital=[]
    for i in hospitals1:
        print(i[0].lower())
        host= HOSPITALS.objects.filter(name=i[0].lower()) .values()
        if(len(host)==0):
            continue
        
         
        id=int(host[0]['id'])
        all_obj=DISTANCE.objects.filter(hid=id)
        no_of_beds=host[0]["beds"]
        if (no_of_beds>len(all_obj)):
            i.append(id)
            avaliable_hospital.append(i)
            
            
    data={
        'hospitals':avaliable_hospital
    }
        
    return data
    

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
  
    
    
    def get(self,request, format=None):
        data = JSONParser().parse(request)
        print(data)
        lon=str(data['lon'])
        lat=str(data["lat"])
        id=str(data["id"])
        
        data=getcurrentusers(lon,lat)
        return Response(data,status=status.HTTP_200_OK)
    def put(elf, request, format=None):
        data = JSONParser().parse(request)
        lon=str(data['lon'])
        lat=str(data["lat"])
        id=str(data["id"])
        idu=str(data["idu"])
        obj=DISTANCE(data={'hid':id,
            'uid':idu
        })
        obj
    
class GETOTP(APIView):

    def get(self,request,fromat=None):
        data = JSONParser().parse(request)
        number=str(data['no'])
        otp=str(data["otp"])

        obj=OTP.objects.filter(no=number).values()
        data={
            "id":obj[0]["id"]
        }

        if str(obj[0]['otp'])==str(otp):
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data=data,status=status.HTTP_401_UNAUTHORIZED)

  
   
    

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

    
            






        
    
                
            
            
            



