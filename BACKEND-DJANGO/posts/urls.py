from django.urls import path, include
from posts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewset)

urlpatterns = [
    path('', include(router.urls)),
]
