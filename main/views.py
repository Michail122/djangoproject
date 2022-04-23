
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')
   # return HttpResponse("<h4>Wooorks!</h4>")
def about(request):
    return render(request, 'main/about.html')
  #  return HttpResponse("<h4>Aboba!</h4>")
# Create your views here.
