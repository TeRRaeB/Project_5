from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
 

def view_bag(request):
    """a view to return the bag contents page"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag 
    
    return redirect(redirect_url)

def adjust_bag(request, item_id): 

    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))  
 
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id): 

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)

        request.session['bag'] = bag

        return JsonResponse({"success": True})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)