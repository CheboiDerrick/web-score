from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from django.http import HttpResponse
import json
# Create your views here.



class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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


