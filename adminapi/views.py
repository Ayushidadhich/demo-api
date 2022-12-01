from cgitb import reset
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from adminapp.models import Project
from .serializers import ProjectSerializer


class ProjectAPIview(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,*args,**kwargs):
        projects = Project.objects.all()
        print(projects,'gggggggggggggggggg')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)