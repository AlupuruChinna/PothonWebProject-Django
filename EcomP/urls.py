from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from EcomP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('actsuser.urls')),
    path('', views.home, name= 'home'),
    path('product/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
