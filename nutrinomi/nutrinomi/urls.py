from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include('nutri.urls', namespace='nutri')),
    path('admin/', admin.site.urls),
]
