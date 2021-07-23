from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

      #api endpoints
    path('api/v1/category',views.CategoryList.as_view(),name='categoryEndpoint'),
    path('api/v1/flashcards',views.FlashcardList.as_view(),name='flashcardEndpoint'),
    path('api/v1/category/<int:pk>/', views.CategoryDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)