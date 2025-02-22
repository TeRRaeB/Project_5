from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q, Avg
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
                products = products.annotate(rating=Avg("ratings__rating"))
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


def product_detail(request, product_id):
    """A view to show detail product"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
