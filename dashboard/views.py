from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from ginfo.forms import *
from ginfo.models import Scholar, Citation
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
        # "citations" :  
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
        # "citations" :  
    }
    return render(request, "dashboard/dashboard.html", context)


@login_required()
def add_scholar(request):
    # id = ""
    if request.method == 'POST':
        id = request.POST['gscholar_id']
        if id is not None:
            
            if Scholar.objects.filter(id=id):
                print("its working for data already fetched")
                messages.error(request, "error")
            
            else:
                print(id)

                url = f"https://scholar.google.co.in/citations?user={id}&hl=en"
                
                html_content = requests.get(url).text
                soup = BeautifulSoup(html_content, "html.parser")

                scholar = soup.title.text[:-17]
                profile_img_url = f"https://scholar.googleusercontent.com/citations?view_op=view_photo&user={id}&citpid=4"
                scholar_post = soup.find('div', attrs={'class':'gsc_prf_il'}).text
                designation =  scholar_post.split(",")[0].strip()
                department = scholar_post.split(",")[1].strip()

                d = {}
                total_publications = 0

                text = soup.find('div', attrs={'id': 'gsc_prf_pua'})
                print(text)
                pmi = text.find('img', attrs={'id': 'gsc_prf_pup-img'})
                print(pmi)
                pmisrc = pmi.src
                profile_img_url = f"{url}/{soup.findAll('img', attrs={'id', 'gsc_prf_pup-img'})}"
                labels = [] 
                for label in soup.findAll("a", attrs={'class' : 'gsc_prf_inta gs_ibl'}):
                    labels.append(label.text)

                for citation in soup.findAll('tr', attrs={'class': 'gsc_a_tr'}):
                    cite = citation.find('td', attrs={'class': 'gsc_a_t'})
                    title = cite.find('a', attrs={'class': 'gsc_a_at'}).text
                    coauthor = list(cite.find('div', attrs={'class': 'gs_gray'}).text.strip().split(","))
                    yr = int(citation.find('td', attrs={'class': 'gsc_a_y'}).text)

                    val = (title, coauthor)

                    if d.get(yr):
                        d[yr].append(val)
                    else:
                        d[yr] = list([val])

                    total_publications += 1

                context = {
                    "scholar" : scholar,
                    "content" : soup.prettify(),
                    "d" : d,
                    "labels" : labels,
                    "img_url" : pmisrc,
                }

                scholar_data = Scholar(
                    id = id,
                    name = scholar,
                    designation = designation,
                    department = department,
                    image_url = profile_img_url,
                )
                scholar_data.save()

                for year, citations in d.items():

                    for citation in citations:
                        
                        citation_info = Citation(
                            citation_title = citation[0],
                            citation_year = year,
                        )
                        citation_info.save()
                        citation_info.scholar.add(scholar_data)
                
                messages.success(request, "success")

    return render(request, "dashboard/add_scholar.html")


@login_required
def analytics(request):
    return render(request, "dashboard/analytics.html")


@login_required
def favourites(request):
    return render(request, "dashboard/favourites.html")


@login_required
def messages(request):
    return render(request, "dashboard/messages.html")

@login_required
def settings(request):
    return render(request, "dashboard/settings.html")

