from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

def blog(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request, 'blog.html', {'blogs' : blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id)) #url은 항상 str로 써야한다. int 정수형으로 정의했을 지라도!

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog')
    else:
        form =BlogPost()
        return render(request, 'new.html', {'form':form})