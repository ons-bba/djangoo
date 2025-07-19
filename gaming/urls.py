from django.urls import path
from .views import (SéanceListView, SéanceCreateView, 
                    SéanceUpdateView, SéanceDeleteView, SéanceDetailView)

urlpatterns = [
    path('', SéanceListView.as_view(), name='séance-list'),
    path('ajouter/', SéanceCreateView.as_view(), name='séance-create'),
    path('modifier/<int:pk>/', SéanceUpdateView.as_view(), name='séance-update'),
    path('supprimer/<int:pk>/', SéanceDeleteView.as_view(), name='séance-delete'),
    path('detail/<int:code>/', SéanceDetailView.as_view(), name='séance-detail'),
]