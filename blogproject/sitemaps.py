from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from core.models import Category, Blogpost

class BlogpostSitemaps(Sitemap):
    def items(self):
        return Blogpost.objects.filter(status=Blogpost.ACTIVE)

    def lastmod(self, obj):
        return obj.created_at

class CategorySitemaps(Sitemap):
    def items(self):
        return Category.objects.all()