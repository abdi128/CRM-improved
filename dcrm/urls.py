"""
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(website.urls)),
]
"""
from django.contrib import admin
from django.urls import path, include
from website import urls as website_urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(website_urls)),
]