from django.urls import path

from .views import draw_menu, index

urlpatterns = [
    path('', index, name='menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
