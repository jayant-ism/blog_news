from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'landing.html' )


def campgroundsindex(request) : 
    sd = { 'id' :  'sdaads' ,
            'name' : 'dassda' ,
            'image' :  'asads' }
    return render(request , 'campgrounds/index.html' , {'campgrounds' : [sd] } )
def campgroundopen(request):

    if request.method == 'GET' : 
        print("ok")
        print(request.GET.get('nam')  )



    return  render(request , 'campgrounds/index.html' , {'campgrounds' :  [] } )