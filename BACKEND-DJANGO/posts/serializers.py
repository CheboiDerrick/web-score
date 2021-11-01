from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ['pk', 'title', 'image','description','link']
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
