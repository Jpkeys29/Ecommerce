from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta: 
        verbose_name_plural = 'categories'  #to rename the model to 'categories' in the admin page

    def __str__(self):
        return self.name
    
    #creating a dynamic url for each category(dropdown menu on the nav bar)
    def get_absolute_url(self):
        return reverse('list-category',args=[self.slug])



class Product(models.Model):
    # Create a foreign key in order to link the product model to a specific category model:
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250) #so that our products are unique!
    price = models.DecimalField(max_digits=4, decimal_places=2)
    SIZE_CHOICES = (('S','Small'),('M','Medium'),('L','Large'),('XL','Extra Large'))
    size = models.CharField(null=True, max_length=2, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='images/')

    class Meta: 
        verbose_name_plural = 'products'  

    def __str__(self):
        return self.title
    
    #creating a dynamic url for each product(redirects to every specific product page)
    def get_absolute_url(self):
        return reverse('product-info',args=[self.slug])





    
