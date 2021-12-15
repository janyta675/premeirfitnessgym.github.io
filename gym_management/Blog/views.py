from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    return render(request,'blog/index.html')
def blog(request):
    blogs = Blog.objects.all().order_by("-date")
    return render(request,'blog/blog.html',{"blogs":blogs})
def blog_details(request,slug):
    
    identify_blog = Blog.objects.all().get(slug=slug)
    return render(request, 'blog/blog_details.html', {"blog": identify_blog, "tags": identify_blog.tags.all()})