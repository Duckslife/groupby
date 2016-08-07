from django.contrib import admin

# Register your models here.
from .models import Board
from .models import Product
from .models import ItemTags

admin.site.register(Board)
admin.site.register(Product)
admin.site.register(ItemTags)