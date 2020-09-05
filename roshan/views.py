from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Contact,Portfolio,Blogpost
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    myposts = Blogpost.objects.all()
    return render(request,'blog.html',{'myposts':myposts})

def blogpost(request,pk):
    post = get_object_or_404(Blogpost, pk=pk)
    return render(request,'blog-post.html',{'post': post})

def portfolio(request):
    datas = Portfolio.objects.all()
    return render(request,'portfolio.html',{'datas':datas})

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        yourmessage = request.POST.get('message','')
        contact = Contact(name = name,email=email,subject=subject,yourmessage=yourmessage)
        print(contact,thank)
        contact.save()
        thank = True
        print(thank)

    return render(request,'contact.html',{'thank':thank})