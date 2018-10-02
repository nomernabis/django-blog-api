from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^signin/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
