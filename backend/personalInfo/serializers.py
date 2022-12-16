from .models import PersonalInfo, Job , Education , certificate 
from rest_framework.serializers import ModelSerializer

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class PersonalInfoSerializer(ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
class eduSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class certSerializer(ModelSerializer):
    class Meta:
        model = certificate
        fields = '__all__'