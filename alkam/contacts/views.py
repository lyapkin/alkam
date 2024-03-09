from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .models import *


# Create your views here.
class ContactsApi(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = ContactsSerializer
    
    def list(self, request):
        result = {
           "departaments": Department.objects.all(),
           "addresses": Address.objects.all()
        }
        serializer = self.get_serializer(result)
        
        return Response(serializer.data)