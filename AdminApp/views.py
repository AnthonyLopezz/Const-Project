from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from AdminApp.forms.forms import FormProduct, FormService
from StoreApp.models import Product
from ServicesApp.models import Service
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required()
def admon(request):
    return render(request, "admon/admin.html")


@login_required()
def add_Product(request):
    data = {
        'form': FormProduct()
    }
    if request.method == 'POST':
        formulario = FormProduct(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["message"] = "Aggregate correctly"
        else:
            data["form"] = formulario
    return render(request, "admon/AddProduct.html", data)


@login_required()
def list(request):

    search = request.GET.get('search')
    products = Product.objects.all()

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'products': page_obj
    }
    if search:
        products = Product.objects.filter(
            Q(name__icontains=search) |
            Q(category__name__icontains=search)
        ).distinct()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'products': page_obj
        }
        return render(request, "admon/listProduct.html", data)

    return render(request, "admon/listProduct.html", data)


@login_required()
def modify_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    data = {
        'form': FormProduct(instance=product)
    }
    if request.method == 'POST':
        form = FormProduct(data=request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="list")
        data["form"] = form

    return render(request, "admon/EditProduct.html", data)


@login_required()
def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect(to="list")


@login_required()
def list_users(request):

    users = User.objects.all()
    searched = request.GET.get('search')
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'users': page_obj
    }

    if searched:
        users = User.objects.filter(
            Q(username__icontains=searched) |
            Q(first_name__icontains=searched) |
            Q(last_name__icontains=searched) |
            Q(email__icontains=searched)
        ).distinct()
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            'users': page_obj
        }

        return render(request, "admon/listUsers.html", data)

    return render(request, "admon/listUsers.html", data)


@login_required()
def list_service(request):

    services = Service.objects.all()
    searched = request.GET.get('search')
    paginator = Paginator(services, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'services': page_obj
    }

    if searched:
        services = Service.objects.filter(
            Q(title__icontains=searched)
        ).distinct()
        paginator = Paginator(services, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            'services': page_obj
        }

        return render(request, "admon/listService.html", data)

    return render(request, "admon/listService.html", data)


@login_required()
def modify_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    data = {
        'form': FormService(instance=service)
    }
    if request.method == 'POST':
        form = FormService(data=request.POST, instance=service, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="listService")
        data["form"] = form

    return render(request, "admon/EditService.html", data)


@login_required()
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect(to="listService")


@login_required()
def add_service(request):
    data = {
        'form': FormService()
    }
    if request.method == 'POST':
        formulario = FormService(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["message"] = "Aggregate correctly"
        else:
            data["message"] = "Service cannot be added"
    return render(request, "admon/addService.html", data)


