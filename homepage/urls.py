from django.urls import path, include
from .views import HomePageViewSet, HomePageViewSetDetailed
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('homepage/', HomePageViewSet.as_view()),
    path('homepage/<int:pk>/', HomePageViewSetDetailed.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)