from django.shortcuts import render
from polls.models import pracTable

# Create your views here.


def index(request):
    return render(request, "polls/html/index.html")
