from .views import update
from .views import NewsViewSet, AgencyViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'feed', NewsViewSet, basename='news')
router.register(r'agency', AgencyViewSet, basename='news')
urlpatterns = [
    path("update/", update),
]
urlpatterns = urlpatterns + router.urls
