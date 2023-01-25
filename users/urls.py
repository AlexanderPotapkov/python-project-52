from django.urls import path

from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='users_list'),
    path('create/', RegisterUser.as_view(), name='register'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update'),
]
