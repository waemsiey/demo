from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ='home'),
    path("todos/", views.todos , name='Todos'),
    path('upload/', views.upload_csv_file, name='uploadcsv')
    #path('display/')
]