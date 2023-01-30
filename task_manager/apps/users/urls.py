from django.urls import path
from .views import UsersView, RegisterUser

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('create/', RegisterUser.as_view(), name='register'),
    # path('<int:pk>/update/', #####, name='update'),
    # path('<int:pk>/delete/', #####, name='delete'),
]