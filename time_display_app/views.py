from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
    context = {
        'time': strftime('%d/%m/%Y %H:%M %S', gmtime())
    }
    print(request.method)
    return render(request, 'index.html', context)

#def registrationpage(request):
   ## return render(request,"registration.html")

#def process(request):
    print(request.method)
    print(request.POST
    )
    return HttpResponse("just submitted a post request")


# Create your views here.
