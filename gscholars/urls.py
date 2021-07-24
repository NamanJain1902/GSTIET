from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ginfo/', include("ginfo.urls")),
]

urlpatterns += staticfiles_urlpatterns()