from django.urls import path
from .views import YourModelNameListCreateView, YourModelNameRetrieveUpdateDestroyView

app_name = 'video'
urlpatterns = [
    path('', YourModelNameListCreateView.as_view(), name='your-model-list-create'),
    path('<int:pk>/', YourModelNameRetrieveUpdateDestroyView.as_view(), name='your-model-retrieve-update-destroy'),
]
