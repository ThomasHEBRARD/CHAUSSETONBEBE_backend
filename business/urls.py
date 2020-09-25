from django.urls import path, include
from .views import BusinessViewSet, BusinessViewSetDetailed
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('business/', BusinessViewSet.as_view()),
    path('busienss/<int:pk>/', BusinessViewSetDetailed.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)