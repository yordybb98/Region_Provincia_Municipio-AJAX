from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('region/', views.get_region),
    path('provincias/<int:region_id>', views.get_provincias),
    path('municipios/<int:provincia_id>', views.get_municipios),
]