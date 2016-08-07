from django.shortcuts import render
from django.utils import timezone
from .models import Board
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Product
from .models import ItemTags

def index(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    itemtags = ItemTags.objects.order_by('sort_num')
    return render(request, 'board/index.html', {'products': products,'itemtags':itemtags})
