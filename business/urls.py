from django.urls import re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r"^", include("business.product.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
