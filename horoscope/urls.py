from django.urls import path
from . import views

urlpatterns = [
    path('type/', views.type),
    # path('type/<str: type>/', views.types_page, name='types_page'),
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),


]
