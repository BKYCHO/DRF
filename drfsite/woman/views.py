from django.shortcuts import render
from .models import Women
from .serialaziers import WomanSerialaizer

# Create your views here.
from rest_framework import generics

class WomanAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomanSerialaizer