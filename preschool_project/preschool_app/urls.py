from django.urls import path
from preschool_app import views
from django.urls import path, register_converter

from . import converts, views

register_converter(converts.FloatUrlParameterConverter, 'float')


urlpatterns = [
   
    path('getall/',views.GetallSchools.as_view()),
    path('getbyid/<int:id>/',views.Getschoolbyid.as_view()),
    path('getallcity/<str:stringa>/',views.GetschoolbyCity.as_view()),
    path('getbyrating/<float:rating>/',views.Getschoolbyratings.as_view())
]