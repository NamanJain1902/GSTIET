from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from ginfo.forms import *
from ginfo.models import Scholar, Citation, Authored
# TODO from ginfo.views import add_scholar
# Create your views here.

@login_required
def index(request):
    try:
        scholars_set = Scholar.objects.all()
        citations_set = Citation.objects.all()

        if request.method == 'POST':    
            if request.POST.get('search_field', ''):
                search_field = request.POST.get('search_field', '')
                scholars_set = Scholar.objects.filter(name__icontains=search_field)
            
            if request.POST.get('sort_method', None):
                sort_criteria = request.POST.get('sort_method', None)
                scholars_set = Scholar.objects.order_by(sort_criteria)
        
    except Scholar.DoesNotExist:
        raise Http404("Scholar entry does not exist.")
    
    context = {
        "scholars": scholars_set,
        "publications" :  citations_set,
    }
    return render(request, "dashboard/dashboard.html", context)

@login_required
def dashboard(request):
    try:
        scholars_set = Scholar.objects.all()
        citations_set = Citation.objects.all()


        if request.method == 'POST':    
            if request.POST.get('search_field', ''):
                search_field = request.POST.get('search_field', '')
                scholars_set = Scholar.objects.filter(name__icontains=search_field)
            
            if request.POST.get('sort_method', None):
                sort_criteria = request.POST.get('sort_method', None)
                scholars_set = Scholar.objects.order_by(sort_criteria)
        
    except Scholar.DoesNotExist:
        raise Http404("Scholar entry does not exist.")
    
    context = {
        "scholars": scholars_set,
        "citations" :  citations_set,
    }
    return render(request, "dashboard/dashboard.html", context)

@login_required
def delete_scholar(request, id):
    pass

@login_required
def edit_scholar(request, id):
    pass

@login_required
def analytics(request):
    return render(request, "analytics/index.html")

@login_required
def favourites(request):
    return render(request, "dashboard/favourites.html")


@login_required
def messages(request):
    return render(request, "dashboard/messages.html")

@login_required
def settings(request):
    return render(request, "dashboard/settings.html")

