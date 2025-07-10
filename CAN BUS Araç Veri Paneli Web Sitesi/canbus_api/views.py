from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Vehicle
from .serializers import UserSerializer, VehicleSerializer

# Herkesin erişebileceği Kullanıcı Kayıt View'ı
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny] # Kimlik doğrulaması gerektirmez
    serializer_class = UserSerializer

# Sadece giriş yapmış kullanıcıların erişebileceği Araç Listesi View'ı
class VehicleListView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

# Sadece giriş yapmış kullanıcıların erişebileceği Araç Detay View'ı
class VehicleDetailView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'