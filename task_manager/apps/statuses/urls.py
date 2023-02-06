from django.urls import path

from ..statuses.views import StatusesView, CreateStatus, UpdateStatus, DeleteStatus

urlpatterns = [
    path('', StatusesView.as_view(), name='statuses'),
    path('create/', CreateStatus.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatus.as_view(), name='update_status'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete_status'),
]
