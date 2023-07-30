from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('update_task/<int:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<int:pk>/', views.deleteTask, name="delete_task")
]