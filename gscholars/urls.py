from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ginfo/', include('ginfo.urls')),
]

handler404 = 'error_handler.views.page_not_found'
handler400 = 'error_handler.views.bad_request'
handler403 = 'error_handler.views.permission_denied'
handler500 = 'error_handler.views.server_error'

urlpatterns += staticfiles_urlpatterns()