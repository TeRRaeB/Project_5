from django.shortcuts import render, get_object_or_404, redirect, reverse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Coalesce
from django.contrib import messages
from django.db.models import Q, Avg, Value,FloatField
from .models import Product, Rating, Category, SubCategory


def all_products(request):
    """A view to show all products"""

    products = Product.objects.all()
    query = None
    selected_category = None
    selected_subcategory = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "name"
            elif sortkey == "rating":
                products = products.annotate(
                    rating=Coalesce(Avg("ratings__rating"), Value(0), output_field=FloatField())
                    )
                sortkey = "rating"
            elif sortkey == "category":
                sortkey = "category__name"
            elif sortkey == "subcategory":
                sortkey = "subcategory__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            category_name = request.GET["category"].lower()
            products = products.filter(category__name=category_name)
            selected_category = Category.objects.filter(name=category_name).first()

        if "subcategory" in request.GET:
            subcategory_name = request.GET["subcategory"].lower()
            products = products.filter(subcategory__name=subcategory_name)
            selected_subcategory = SubCategory.objects.filter(
                name=subcategory_name
            ).first()

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    selected_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": selected_category,
        "current_subcategories": selected_subcategory,
        "current_sorting": selected_sorting,
    }

    return render(request, "products/products.html", context)


@login_required
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    user_rating = Rating.objects.filter(user=request.user, product=product).first()
    if user_rating:
        user_rating_value = user_rating.rating
    else:
        user_rating_value = 0 
    stars_range = range(1, 6)

    context = {
        "product": product,
        "user_rating_value": user_rating_value,
        "stars_range": stars_range,
    }

    return render(request, "products/product_detail.html", context)

@login_required
def rate_product(request, product_id):
    product = Product.objects.get(id=product_id)
    rating_value = request.POST.get('rating')
    if rating_value is None: 
        return HttpResponse("Rating is required", status=400)
    
    rating_value = int(rating_value) 
    
    rating, created = Rating.objects.get_or_create(
        user=request.user, product=product,
        defaults={'rating': rating_value}   
    )
     
    if not created:
        rating.rating = rating_value
        rating.save()

    return redirect('product_detail', product_id=product_id)