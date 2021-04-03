from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('matcher/', include('matcher.urls')),
    path('admin/', admin.site.urls),
]