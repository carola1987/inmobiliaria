from django.urls import path
from . import views

app_name = 'gestion_inmuebles'

urlpatterns = [
    path('inmuebles/', views.InmuebleListView.as_view(), name='inmueble_list'),
    path('inmueble/<int:inmueble_id>/', views.InmuebleDetailView.as_view(), name='inmueble_detail'),
    path('inmueble/nuevo/', views.InmuebleCreateView.as_view(), name='inmueble_create')
    
]