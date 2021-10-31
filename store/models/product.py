from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default=' ')
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return f"{self.name}  {self.price}  {self.category}"

    @staticmethod
    def get_all_products():
       return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()


    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids) #id__in will take the list

