from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tasks/', views.task_list_view, name='tasks'),
    path('rot/', views.brain_dump_view, name='brain_dump'),
    path('list/<int:list_id>/', views.tasklist_view, name='tasklist'),
]