from django.shortcuts import render

# Create your views here.
def jinjaconditions(request):
    d={'name':'varsha','age':10,'marks':95,'a':50,'b':100,'c':25}
    return render(request,'jinjaconditions.html',context=d)