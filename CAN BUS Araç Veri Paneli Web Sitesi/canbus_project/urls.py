from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API URL'leri (/api/register/, /api/vehicles/, vb.)
    path('api/', include('canbus_api.urls')),

    # JWT Token URL'leri
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Frontend Sayfa URL'leri
    path('register/', TemplateView.as_view(template_name='register.html'), name='register-page'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login-page'),
    path('vehicle/<str:pk>/', TemplateView.as_view(template_name='vehicle_detail.html'), name='vehicle-detail-page'),
    path('', TemplateView.as_view(template_name='index.html'), name='index-page'),
]