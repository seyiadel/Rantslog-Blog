from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField()
    
    def __str__(self):
        return self.title

    class Meta():
        ordering=('title',)
        verbose_name_plural='Categories'

    def get_absolute_url(self):
        return '/%s/' % self.slug



class Blogpost(models.Model):

    ACTIVE='active'
    DRAFTS='drafts'

    CHOICES_STATUS=(
        (ACTIVE,'Active'),
        (DRAFTS, 'Drafts')
    )

    category=models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    image= models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug= models.SlugField()
    title=models.CharField(max_length=250)
    intro =models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=27, choices=CHOICES_STATUS, default=ACTIVE)

    class Meta():
        ordering=('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

class Comment(models.Model):
    post=models.ForeignKey(Blogpost,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=27)
    comment =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)