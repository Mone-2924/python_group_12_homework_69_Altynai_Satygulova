from django.shortcuts import render
from django.template.context_processors import request

def index_view(request):
    return render(request, 'index.html')