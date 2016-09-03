# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from users.models import User
from  board.models import Board
from  board.models import Product
from  board.models import ItemTags


def index(request):
    return render(request, 'login_page.html')


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

