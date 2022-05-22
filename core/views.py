from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_list_or_404,get_object_or_404, render,redirect
from .models import Blogpost,Category
from .forms import CommentForm
# Create your views here.
def homepage(request,):
    posts=Blogpost.objects.filter(status=Blogpost.ACTIVE)
    return render(request,'homepage.html',{'posts':posts,})

def detail(request, slug):
    post=get_object_or_404(Blogpost,slug=slug, status=Blogpost.ACTIVE) 
    form = CommentForm()

    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('.',slug=slug)
    return render(request,'detail.html',{'post':post,'form':form})
 
def category(request,slug):
    category =get_object_or_404(Category,slug=slug)
    posts= category.categories.filter(status=Blogpost.ACTIVE)
    return render(request,'category.html',{'category':category,'posts':posts}) 

def search(request):
    query=request.GET.get('query','')
    
    posts =Blogpost.objects.filter(status=Blogpost.ACTIVE).filter(Q(title__icontains=query)| Q(intro__icontains=query) |Q(body__icontains=query))
    return render(request,'search.html',{'query':query,'posts':posts})

def about(request):
    return render (request, 'about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow:/admin/"
    ]
    return HttpResponse("\n".join(text), content_type= 'text/plain')