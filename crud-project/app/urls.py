from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('show/',views.show),
    path('show/delete/<int:id>/',views.delete),
    path('show/edit/<int:id>/',views.edit),
]