from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI


router = routers.DefaultRouter()
router.register(r'flashcards',views.FlashCardViewSet)

urlpatterns = [
   url(r'^$',views.index, name='index'),
   url(r'^create/', views.create, name="create"),
   path('api/register/', RegisterAPI.as_view(), name='register'),

   path('api/login/', LoginAPI.as_view(), name='login'),
   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
   path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)