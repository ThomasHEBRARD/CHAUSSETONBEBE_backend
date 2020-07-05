from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import HomePageSerializer
from .models import HomePageModel


class HomePageViewSet(generics.ListCreateAPIView):
    queryset = HomePageModel.objects.all()
    serializer_class = HomePageSerializer

class HomePageViewSetDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomePageModel.objects.all()
    serializer_class = HomePageSerializer
