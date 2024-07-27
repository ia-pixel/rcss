from django.contrib import admin
from django.urls import path, include
from products import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # Inclure les URLs de votre application
]
