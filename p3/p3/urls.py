from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from p3 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

urlpatterns += staticfiles_urlpatterns()
