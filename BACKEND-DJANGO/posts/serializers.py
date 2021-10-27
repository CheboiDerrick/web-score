from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ['pk', 'title', 'image','descrption','link']
        fields = '__all__' 