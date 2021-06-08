from django.db.models import Q
from django.shortcuts import render
from .models import Product, CategoryProd
from django.core.paginator import Paginator # import Paginator

# Create your views here.


def store(request):
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    searched = request.GET.get('search')
    if searched:
        products = Product.objects.filter(
            Q(name__icontains=searched) |
            Q(category__name__icontains=searched)
        ).distinct()
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "store/store.html", {'products': page_obj})

    return render(request, "store/store.html", {'products': page_obj})


def cart(request):

    return render(request, "store/cart.html")


def product(request, product_id):
    products = Product.objects.get(id=product_id)

    return render(request, "store/product.html", {'products': products})
