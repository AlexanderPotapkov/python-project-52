from django.urls import path

from .views import TasksView

urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    # path('<int:pk>', )
    # path('create/', CreateTask.as_view(), name='create_task'),
    # path('<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    # path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
]