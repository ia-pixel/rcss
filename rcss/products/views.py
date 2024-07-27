from django.shortcuts import render, get_object_or_404
from products.models import Product
import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def cart(request):
    return render(request, 'checkout.html')

def home(request):
    return render(request, 'home.html', {'products': Product.objects.all()})

def product_list(request):
    products = [
    {'id': 1, 'image': 'media/product1.jpg.webp', 'name': 'Product 1', 'description': 'Description of product 1', 'price': 10.99},
    {'id': 2, 'image': 'media/product2.jpg.webp', 'name': 'Product 2', 'description': 'Description of product 2', 'price': 15.99},
    {'id': 3, 'image': 'media/product3.jpg.webp', 'name': 'Product 3', 'description': 'Description of product 3', 'price': 7.99},
    {'id': 4, 'image': 'media/product4.jpg.webp', 'name': 'Product 4', 'description': 'Description of product 4', 'price': 10.99},
    {'id': 5, 'image': 'media/product5.jpg.webp', 'name': 'Product 5', 'description': 'Description of product 5', 'price': 12.99},
    {'id': 6, 'image': 'media/product6.jpg.webp', 'name': 'Product 6', 'description': 'Description of product 6', 'price': 11.99},
    {'id': 7, 'image': 'media/product7.jpg.webp', 'name': 'Product 7', 'description': 'Description of product 7', 'price': 9.32},
    {'id': 8, 'image': 'media/product8.jpg.webp', 'name': 'Product 8', 'description': 'Description of product 8', 'price': 14.99},
    {'id': 9, 'image': 'media/product9.jpg.webp', 'name': 'Product 9', 'description': 'Description of product 9', 'price': 13.99},
    {'id': 10, 'image': 'media/product10.jpg.webp', 'name': 'Product 10', 'description': 'Description of product 10', 'price': 53.54},
    {'id': 11, 'image': 'media/product11.jpg.webp', 'name': 'Product 11', 'description': 'Description of product 11', 'price': 11.29},
    {'id': 12, 'image': 'media/product12.jpg.webp', 'name': 'Product 12', 'description': 'Description of product 12', 'price': 10.99},
    {'id': 13, 'image': 'media/product13.jpg.webp', 'name': 'Product 13', 'description': 'Description of product 13', 'price': 12.99},
    {'id': 14, 'image': 'media/product14.jpg.webp', 'name': 'Product 14', 'description': 'Description of product 14', 'price': 13.99},
    {'id': 15, 'image': 'media/product15.jpg.webp', 'name': 'Product 15', 'description': 'Description of product 15', 'price': 11.99},
    {'id': 16, 'image': 'media/product16.jpg.webp', 'name': 'Product 16', 'description': 'Description of product 16', 'price': 10.99},
    {'id': 17, 'image': 'media/product17.jpg.webp', 'name': 'Product 17', 'description': 'Description of product 17', 'price': 11.99},
    {'id': 18, 'image': 'media/product18.jpg.webp', 'name': 'Product 18', 'description': 'Description of product 18', 'price': 10.99},
    {'id': 19, 'image': 'media/product19.jpg.webp', 'name': 'Product 19', 'description': 'Description of product 19', 'price': 12.99},
    {'id': 20, 'image': 'media/product20.jpg.webp', 'name': 'Product 20', 'description': 'Description of product 20', 'price': 13.99},
    {'id': 21, 'image': 'media/product21.jpg.webp', 'name': 'Product 21', 'description': 'Description of product 21', 'price': 11.99},
    {'id': 22, 'image': 'media/product22.jpg.webp', 'name': 'Product 22', 'description': 'Description of product 22', 'price': 10.99},
    {'id': 23, 'image': 'media/product23.jpg.webp', 'name': 'Product 23', 'description': 'Description of product 23', 'price': 11.99},
]
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def about(request):
    return render(request, 'about.html')



def checkout(request):
    if request.method == 'POST':
        try:
            # Créer une session de paiement
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'T-shirt',
                        },
                        'unit_amount': 2000,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),
                cancel_url=request.build_absolute_uri('/cancel/'),
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'checkout.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')
