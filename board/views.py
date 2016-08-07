# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .models import Product
from .models import ItemTags
from .models import Board

def index(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    itemtags = ItemTags.objects.order_by('sort_num')
    return render(request, 'board/index.html', {'products': products,'itemtags':itemtags})

def drops(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    itemtags = ItemTags.objects.order_by('sort_num')
    return render(request, 'board/drops.html', {'products': products,'itemtags':itemtags})

def board(request, id=1):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    boards = Board.objects.filter(reg_date__lte=timezone.now()).order_by("-reg_date")
    itemtags = ItemTags.objects.order_by('sort_num')
    return render(request, 'board/board.html', {'products': products,'itemtags':itemtags,'boards':boards})

def board_new(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    itemtags = ItemTags.objects.order_by('sort_num')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.reg_date = timezone.now()
            board.save()
            return redirect('board.views.board_detail', id=board.pk)
    else:
        form = PostForm()
    return render(request, 'board/board_new.html', {'form': form,'products': products,'itemtags':itemtags,})

def board_edit(request, id):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    itemtags = ItemTags.objects.order_by('sort_num')
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('board.views.board_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/board_edit.html', {'form': form,'products': products,'itemtags':itemtags,})


def board_detail(request, id=1):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    boards = Board.get_object_or_404(Board, id=id)
    itemtags = ItemTags.objects.order_by('sort_num')
    return render(request, 'board/board_detail.html', {'products': products,'itemtags':itemtags,'boards':boards})



def product_detail(request, id=1):
    product = get_object_or_404(Product, id=id)
    try:
        prev_product = get_object_or_404(Product, id=id).get_previous_by_reg_date()
    except:
        prev_product = None
    try:
        next_product = get_object_or_404(Product, id=id).get_next_by_reg_date()
    except:
        next_product = None

    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    itemtags = ItemTags.objects.order_by('sort_num')
    return render(request, 'board/product_detail.html', {'product': product,'products': products
                        ,'itemtags':itemtags,'prev_product':prev_product,'next_product':next_product})

