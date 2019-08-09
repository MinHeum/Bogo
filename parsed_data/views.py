from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator

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


from django.shortcuts import render
from .models import Product
from .models import Product2
from .models import Product3
from .models import Product4
from .models import Product5
from django.core.paginator import Paginator
from django.utils import timezone


def intro(request):
    return render(request, 'intro.html')


def home(request):
    return render(request, 'home.html')


def gs25(request):
    items = Product5.objects
    item_list = Product5.objects.all()
    paginator = Paginator(item_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'gs25.html', {'items': items, 'posts': posts})


def seven(request):
    items = Product4.objects
    item_list = Product4.objects.all()
    paginator = Paginator(item_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'seven.html', {'items': items, 'posts': posts})


def emart(request):
    items = Product2.objects
    item_list = Product2.objects.all()
    paginator = Paginator(item_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'emart.html', {'items': items, 'posts': posts})


def ministop(request):
    items = Product3.objects
    item_list = Product3.objects.all()
    paginator = Paginator(item_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'ministop.html', {'items': items, 'posts': posts})


def cu(request):
    items = Product.objects
    item_list = Product.objects.all()
    paginator = Paginator(item_list,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'cu.html', {'items': items, 'posts': posts})

@login_required
def addGoods(request):
    return render(request,'bogo/add.html')