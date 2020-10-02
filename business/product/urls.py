from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter
from business.product.product.views import ProductViewSet

router = SimpleRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [re_path(r"^", include(router.urls))]
