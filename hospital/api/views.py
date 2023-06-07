from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from .models import HOSPITALS, BLOODBANK , DISTANCE
from .serializers import HospitalSerializer, BloodBankSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.views import APIView
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


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
    def getcurrentusers(self , loc, id):
        all_obj=DISTANCE.objects.filter(dist__lte=loc)
        host= HOSPITALS.objects.get(pk=id)
        no_of_beds=host.beds
        if (no_of_beds>len(all_obj)):
            return True
        
     
class MessageSendAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "general", {"type": "send_info_to_user_group",
                        "text": {"status": "done"}}
        )

        return Response({"status": True}, status=status.HTTP_200_OK)

    def post(self, request):
        msg = Message.objects.create(user=request.user, message={
                                     "message": request.data["message"]})
        socket_message = f"Message with id {msg.id} was created!"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"{request.user.id}-message", {"type": "send_last_message",
                                           "text": socket_message}
        )

        return Response({"status": True}, status=status.HTTP_201_CREATED)