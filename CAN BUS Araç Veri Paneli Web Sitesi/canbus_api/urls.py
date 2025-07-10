from django.urls import path
from .views import RegisterView, VehicleListView, VehicleDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/<str:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
]