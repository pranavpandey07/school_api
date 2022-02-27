from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated,AllowAny
from preschool_app import models
from preschool_app.serializers import PreschoolSerializer

# Create your views here.
class GetallSchools(APIView):
    
    permission_classes = [AllowAny]
    def get(self,request):
        school_data=models.preschool.objects.all()
        school_serialized_data=PreschoolSerializer(school_data,many=True)
        return Response(data={'data':school_serialized_data.data})


class Getschoolbyid(APIView):
    
    permission_classes = [AllowAny]
    def get(self,request,id):
        try:
            school_data=models.preschool.objects.get(School_id=id)
            school_serialized_data=PreschoolSerializer(school_data)
            return Response(data={'data':school_serialized_data.data})
        
        except models.preschool.DoesNotExist:
            return Response(data={'data':"Not Found"},status=404) 

class GetschoolbyCity(APIView):
    
    permission_classes = [AllowAny]
    def get(self,request,stringa):
        try:
            school_data=models.preschool.objects.filter(City=stringa)
            school_serialized_data=PreschoolSerializer(school_data,many=True)
            return Response(data={'data':school_serialized_data.data})
        
        except models.preschool.DoesNotExist:
            return Response(data={'data':"Not Found"},status=404) 

class Getschoolbyratings(APIView):
    
    permission_classes = [AllowAny]
    def get(self,request,rating):
        try:
            school_data=models.preschool.objects.filter(Ratings=rating)
            school_serialized_data=PreschoolSerializer(school_data,many=True)
            return Response(data={'data':school_serialized_data.data})
        
        except models.preschool.DoesNotExist:
            return Response(data={'data':"Not Found"},status=404) 