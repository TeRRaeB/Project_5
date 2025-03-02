from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Product
from django.utils import timezone
from django.conf import settings

class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all().order_by('name')

    def lastmod(self, obj):
        return timezone.now() 

    def location(self, obj):
        return f"{settings.SITE_URL}{reverse('product_detail', args=[obj.id])}"