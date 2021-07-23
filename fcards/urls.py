from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
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
   path('signup/', views.signup, name='signup'),
   path('login/',auth_views.LoginView.as_view(), name='login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
   
  #api endpoints
   path('api/v1/category',views.CategoryList.as_view(),name='categoryEndpoint'),
   path('api/v1/flashcards',views.FlashcardList.as_view(),name='flashcardEndpoint'),
   path('api/v1/category/<int:pk>/', views.CategoryDetail.as_view()),
   path('api/login/', LoginAPI.as_view(), name='login'),
   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
   path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]