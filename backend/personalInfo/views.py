from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonalInfoSerializer, JobSerializer , eduSerializer , certSerializer 
from .models import PersonalInfo, Job, Education, certificate

# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    def get_queryset(self):
        return Job.objects.all()

class eduViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = eduSerializer
    def get_queryset(self):
        return Education.objects.all()

class certViewSet(viewsets.ModelViewSet):
    queryset = certificate.objects.all()
    serializer_class = certSerializer