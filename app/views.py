from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Dash:

    def home(request):
        return render(request, "dash/home.html")

# def other(request):
#     return render(request, "app/other.html")

