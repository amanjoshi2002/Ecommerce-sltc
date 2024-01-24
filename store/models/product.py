from django.db import models
from .category import Category


class Product(models.Model):
    Product_id = models.AutoField
    name = models.CharField(max_length=50)
    display = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    discount = models.IntegerField(default=15)
    qty = models.IntegerField(default=20)
    image = models.ImageField(upload_to='uploads/products/')
    image1 = models.ImageField(upload_to='uploads/products1/' , default= 'uploads/product/1_01.jpg')
    image2 = models.ImageField(upload_to='uploads/products2/' ,default= 'uploads/product/1_01.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
      return Product.objects.filter(display=True)
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();



from .retailstore import RetailStore

class SalesOrder(models.Model):
    retail = models.ForeignKey(RetailStore, on_delete=models.CASCADE, related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_items = models.ManyToManyField(Product, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=False)
