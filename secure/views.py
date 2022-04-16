from django.shortcuts import render
from .models import security
# Create your views here.
def home(request):
    secs = security.objects.all()

    return render(request,'index.html',{"secs":secs})
