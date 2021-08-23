from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required()
def index(request):
    return render(request, "loginout/index.html", {"context": "Hello World"})


def register_user(request):
    
    form = UserCreationForm()
    print(form)
    