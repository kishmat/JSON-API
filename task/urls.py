from django.urls import include, path
from rest_framework import routers
from task import views

router = routers.DefaultRouter()
router.register(r'members', views.MemberViewSet)
router.register(r'activity', views.Activity_periodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
