from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'Anish'})

def goto(request):
    val1 = int(request.POST['n1'])
    val2 = int(request.POST['n2'])
    res = val1 + val2
    return render(request,'output.html',{'result':res,'name':'Anish'})
