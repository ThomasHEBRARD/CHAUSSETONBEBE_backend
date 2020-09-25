from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import BusinessSerializer
from .models import BusinessModel


class BusinessViewSet(generics.ListCreateAPIView):
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessSerializer

    def get_queryset(self):
        return self.queryset

class BusinessViewSetDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessSerializer
