from django.contrib import admin
from django.urls import include, path  # make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicapp.urls')),  # include the app urls
]
