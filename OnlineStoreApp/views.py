from django.shortcuts import render
from .models import Cover


# Create your views here.


def home(request):
    covers = Cover.objects.all()
    return render(request, "OnlineStoreApp/home.html", {'covers': covers})
