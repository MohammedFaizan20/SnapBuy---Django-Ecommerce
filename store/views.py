from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404

from django.http import HttpResponse



# Create your views here.




def store(request):

    all_products = Product.objects.all()

    context = {'my_products': all_products}

    return render(request, 'store/store.html', context)


def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html', {'category':category, 'products':products})


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {'product': product}

    return render(request, 'store/product-info.html', context)

from django.http import HttpResponse,Http404
from django.conf import settings
import os

def serve_image_view(request, image_name):
    image_path = os.path.join(settings.MEDIA_ROOT, 'images', image_name)
    
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            return HttpResponse(image_file.read(), content_type='image/jpeg')  # Change content_type based on image format
    else:
        raise Http404("Image not found.")