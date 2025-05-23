from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from products.models import Product
 

def view_bag(request):
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag 
    
    return redirect(redirect_url)

def adjust_bag(request, item_id): 
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))  
 
    if quantity > 0:
        bag[item_id] = quantity
        
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}',extra_tags="bag")
    else:
        bag.pop(item_id)        
        messages.success(request, f'Remove {product.name} from your bag',extra_tags="bag")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id): 
    try:        
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag',{})
        bag.pop(item_id)
        
        messages.success(request, f'Remove {product.name} from your bag',extra_tags="bag")
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        
        messages.error(request, f'Error removing item: {e}',extra_tags="bag")
        return HttpResponse(status=500)