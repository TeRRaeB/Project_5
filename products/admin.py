from django.contrib import admin
from .models import Product, Category, SubCategory, Rating, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price', 'average_rating', 'total_votes')
    search_fields = ('name', 'description')
    list_filter = ('category', 'subcategory')

    def average_rating(self, obj):
        return obj.average_rating()
    average_rating.short_description = "Avr. rating"

    def total_votes(self, obj):
        return obj.total_votes()
    total_votes.short_description = "votes"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('rating',)
    ordering = ('-created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at', 'short_comment')
    search_fields = ('user__username', 'product__name', 'comment')
    list_filter = ('rating',)
    ordering = ('-created_at',)

    def short_comment(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    short_comment.short_description = "Comment"

admin.site.register(Category)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')