from django.conf.urls import handler400, handler403, handler404, handler500
from . import views

urlpatterns = []

# handler404 = 'error_handler.views.page_not_found'
# handler400 = 'error_handler.views.bad_request'
# handler403 = 'error_handler.views.permission_denied'
# handler500 = 'error_handler.views.server_error'