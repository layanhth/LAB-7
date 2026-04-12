from django.urls import path
from . import views

urlpatterns = [
    path('task7', views.students_by_city),
]
