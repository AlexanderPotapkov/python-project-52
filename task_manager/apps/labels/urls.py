from django.urls import path

from .views import LabelsView, CreateLabel, UpdateLabel

urlpatterns = [
    path('', LabelsView.as_view(), name='labels'),
    path('create/', CreateLabel.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='update_label'),
    # path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete_label'),
]
