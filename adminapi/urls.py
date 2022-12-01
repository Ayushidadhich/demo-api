from os import name

from django.urls import path
from .views import *
from .views import ProjectAPIView, ProjectDetailAPIView
urlpatterns = [
    path("project",ProjectAPIView.as_view()),
]
