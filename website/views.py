from django.shortcuts import render
from .models import About_SWLP
# Create your views here.
def index(request):

    return render(request, 'index.html')
