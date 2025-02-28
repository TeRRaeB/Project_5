from django.shortcuts import render, get_object_or_404, redirect, reverse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q, Avg, Value,FloatField
from .models import Product, Rating, Category, SubCategory, Review
from .forms import ReviewForm,ProductForm

def all_products(request):

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
    
    if request.GET.get('show_all'):
        reviews = product.reviews.all()
    else:
        reviews = product.reviews.all()[:3]
        
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
        "reviews": reviews
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
    
    messages.info(request, "Your rating has been sent!")
    return redirect('product_detail', product_id=product_id)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data.get("rating")
            comment = form.cleaned_data.get("comment")

            review, created = Review.objects.update_or_create(
                user=request.user,
                product=product,
                defaults={"rating": rating_value, "comment": comment},
            )

            rating, created = Rating.objects.update_or_create(
                user=request.user,
                product=product,
                defaults={"rating": rating_value},
            )

            messages.info(request, "Your review has been submitted!", extra_tags="review")
            return redirect("product_detail", product_id=product.id)
        else:
            messages.error(request, "There was an issue with your review.", extra_tags="review")
            return redirect("product_detail", product_id=product.id)

    else:
        form = ReviewForm()

    return render(request, "products/add_review.html", {"form": form, "product": product})

@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context) 

def get_subcategories(request, category_id):
    subcategories = SubCategory.objects.filter(category_id=category_id)
    data = {
        'subcategories': list(subcategories.values('id', 'name'))
    }
    return JsonResponse(data)

@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))