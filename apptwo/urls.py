
from django.contrib import admin
from django.urls import path, register_converter
from apptwo import views as apptwo_views
from apptwo import converters

register_converter(converters.TwoDigitConverter, 'dd')

urlpatterns = [
    path('djangorocks/', apptwo_views.djangorocks),
    path('pictures/<str:category>/', apptwo_views.picture_detail),
    path('pictures/<str:category>/<int:year>/<int:month>/', apptwo_views.picture_detail),
    path('pictures/<str:category>/<int:year>/<int:month>/<dd:day>/', apptwo_views.picture_detail),
]
