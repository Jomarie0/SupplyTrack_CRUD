from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('dashboard:home')),  # 👈 root redirects to dashboard
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('orders/', include('orders.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('users/', include('users.urls')),
]

