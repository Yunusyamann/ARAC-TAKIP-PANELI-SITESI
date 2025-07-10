from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vehicle

# Yeni kullanıcı oluşturmak için kullanılır. Şifreyi otomatik hash'ler.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

# Araç verilerini JSON'a çevirmek için kullanılır.
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'