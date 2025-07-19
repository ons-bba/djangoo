from django.urls import path
from . import views

urlpatterns = [
    path('', views.SeanceListView.as_view(), name='seance_list'),
    path('ajouter/', views.SeanceCreateView.as_view(), name='seance_add'),
    path('modifier/<int:pk>/', views.SeanceUpdateView.as_view(), name='seance_edit'),
    path('supprimer/<int:code>/', views.seance_delete, name='seance_delete'),
    path('detail/<int:code>/', views.seance_detail, name='seance_detail'),
]
