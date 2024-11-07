from django.urls import path
from .views import get_nodes, create_nodes


urlpatterns = [
    path('nodes/', get_nodes, name='get_nodes'),
    path('nodes/create/', create_nodes, name='create_nodes')
]