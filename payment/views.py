from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

import razorpay

from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart

from django.views.decorators.csrf import csrf_exempt


def checkout(request):
    print("=== CHECKOUT CALLED ===")
    print("RAZORPAY_KEY_ID:", settings.RAZORPAY_KEY_ID)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    cart = Cart(request)

    try:
        total_cost = float(cart.get_total())
        print("Cart total:", total_cost)

        amount_paise = int(total_cost * 100)  # INR in paise
        print("Amount in paise:", amount_paise)

        payment = client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": "1"
        })

    except Exception as e:
        print("Razorpay Order Creation Failed:", e)
        return render(request, 'payment/payment-failed.html')

    context = {
        'key_id': settings.RAZORPAY_KEY_ID,
        'payment': payment,
        'amount': amount_paise
    }

    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context['shipping'] = shipping_address
        except ShippingAddress.DoesNotExist:
            pass

    return render(request, 'payment/checkout.html', context)


@csrf_exempt
def complete_order(request):
    print("=== COMPLETE ORDER CALLED ===")
    print("POST DATA:", request.POST)

    if request.POST.get('action') == 'post':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zipcode = request.POST.get('zipcode')

            razorpay_order_id = request.POST.get('razorpay_order_id')
            razorpay_payment_id = request.POST.get('razorpay_payment_id')

            shipping_address = f"{address1}\n{address2}\n{city}\n{state}\n{zipcode}"

            cart = Cart(request)
            total_cost = float(cart.get_total())

            if request.user.is_authenticated:
                order = Order.objects.create(
                    full_name=name,
                    email=email,
                    shipping_address=shipping_address,
                    amount_paid=total_cost,
                    user=request.user,
                    payment_id=razorpay_payment_id
                )
            else:
                order = Order.objects.create(
                    full_name=name,
                    email=email,
                    shipping_address=shipping_address,
                    amount_paid=total_cost,
                    payment_id=razorpay_payment_id
                )

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['qty'],
                    price=item['price'],
                    user=request.user if request.user.is_authenticated else None
                )

            cart.clear()  # 💡 Make sure you have a clear() method!
            print("Order completed successfully.")
            return JsonResponse({'success': True})

        except Exception as e:
            print("Complete order failed:", e)
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request'})


def payment_success(request):
    print("=== PAYMENT SUCCESS VIEW ===")
    request.session.flush()
    return render(request, 'payment/payment-success.html')


def payment_failed(request):
    print("=== PAYMENT FAILED VIEW ===")
    return render(request, 'payment/payment-failed.html')
