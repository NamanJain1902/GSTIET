from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def permission_denied(request, exception):
    raise render(request, "error_handler/permission_denied.html", status=403)

def page_not_found(request, exception):
    return render(request, "error_handler/page_not_found.html", status=404)

def bad_request(request, exception):
    return render(request, "error_handler/bad_request.html", status=400)

def server_error(request, exception=None):
    return render(request, "error_handler/server_error.html", status=500)
