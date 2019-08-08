from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'bogo/home.html')

def login(request):
    return render(request, 'bogo/login.html')

@login_required
def post(request):
    posts = Post.objects
    return render(request, 'post/post.html',{'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'post/detail.html', {'post':post_detail})

def new(request):
    return render(request, 'post/new.html')

def create(request):
    post = Post()
    post.user_name = request.user.username
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/' + str(post.id))

@login_required
def addGoods(request):
    return render(request,'bogo/add.html')