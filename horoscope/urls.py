from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('type/', views.type, name='types'),
    path('type/<str:type>/', views.types_page, name='types_page'),
    path('', views.index, name='start_page'),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:month>/<int:day>/', views.get_info_by_day),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
]
