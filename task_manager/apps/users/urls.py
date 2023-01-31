from django.urls import path
from .views import UsersView, RegisterUser, UpdateUser

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('create/', RegisterUser.as_view(), name='register'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update'),
    # path('<int:pk>/delete/', #####, name='delete'),
]
