# variasjon_app/urls.py (hovedprosjekt)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # 👈 inkluderer våre ruter
]