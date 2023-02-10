from django.urls import path

from .views import TasksView, CreateTask, UpdateTask, DeleteTask, ShowTask

urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('<int:pk>', ShowTask.as_view(), name='show_task'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
]
