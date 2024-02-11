from django.urls import path
from .views import index, create_menu


urlpatterns = [
    path('', index, name='menu'),
    path('<path:path>/', create_menu, name='create_menu'),
]