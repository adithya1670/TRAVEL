from django.http import HttpResponse
from django.shortcuts import render
# from. models import Place
from. models import Team

# Create your views here.
# def demo (request):
#     obj=Place.objects.all()
#     return render(request,"index.html",{'result':obj})

# def demo(request):
#     obj1=Team.objects.all()
#     return render(request, "index.html",{'result1':
def demo (request):
    obj=Team.objects.all()
    return render(request,"index.html",{'result':obj})
# def operation (request):
#        x=int(request.GET.get('num1'))
#        y=int(request.GET.get('num2'))
#
#        return   render(request, "result.html", {'result': x+y,'result1':x-y,'result2':x*y,'result3':x/y})

# def demo(request):
#     return render(request,"index.html")
