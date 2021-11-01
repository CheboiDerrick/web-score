from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Profile
from .serializers import ProjectSerializer, ProfileSerializer
from django.http import HttpResponse
import json
from rest_framework.permissions import AllowAny
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        file = request.FILES['image']
        description = request.data['description']
        link = request.data['link']
        Project.objects.create(title=title,image=file, description=description, link=link)
        return HttpResponse(({'message': "Uploaded"}), status=200)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Project.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


# @csrf_exempt
# def project_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         project = Project.objects.get(pk=pk)
#     except Project.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ProjectSerializer(project)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ProjectSerializer(project, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         project.delete()
#         return HttpResponse(status=204)
