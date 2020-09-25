from django.urls import re_path, include
from business.product.product.views import ProductViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r"^<int:pk>/", ProductViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
