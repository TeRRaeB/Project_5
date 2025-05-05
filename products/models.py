from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    image_url = models.URLField(max_length=1024, null= True, blank=True)
    image = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def rating(self):
        ratings = list(self.ratings.values_list('rating', flat=True)) + list(self.reviews.values_list('rating', flat=True))
        if not ratings: 
            return 0
        return round(sum(ratings) / len(ratings), 1) if ratings else 0

    def total_votes(self): 
        return self.ratings.count() + self.reviews.count()
 
 
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        existing_review = Review.objects.filter(user=self.user, product=self.product).first()
        if existing_review:
            existing_review.rating = self.rating
            existing_review.save()
            return
        existing_rating = Rating.objects.filter(user=self.user, product=self.product).exclude(pk=self.pk).first()
        if existing_rating:
            existing_rating.rating = self.rating
            existing_rating.save()
            return

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'product')
        
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        existing_rating = Rating.objects.filter(user=self.user, product=self.product).first()
        if existing_rating:
            existing_rating.rating = self.rating
            existing_rating.save()

        existing_review = Review.objects.filter(user=self.user, product=self.product).exclude(pk=self.pk).first()
        if existing_review:
            existing_review.rating = self.rating
            existing_review.comment = self.comment
            existing_review.save()
        else:
            super().save(*args, **kwargs) 

    class Meta:
        unique_together = ('user', 'product')