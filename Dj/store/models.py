from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


######################################## Variables ########################################


User = settings.AUTH_USER_MODEL


######################################## Product section ########################################


class Category(models.Model):
    title       = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    thumbnail   = models.ImageField(upload_to='category/')
    active      = models.BooleanField(default=True)
    created_at  = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = True
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    numbers         = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    title           = models.CharField(max_length=255, unique=True, primary_key=True)
    description     = models.TextField()
    digital         = models.BooleanField(default=False, null=True, blank=True)
    thumbnail       = models.ImageField(upload_to='product/')
    price           = models.DecimalField(max_digits=12, decimal_places=2)
    old_price       = models.DecimalField(max_digits=12, decimal_places=2)
    barcode         = models.CharField(max_length=15, validators=[numbers])
    active          = models.BooleanField(default=True)
    created_at      = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    def gallery(self):
        return Gallery.objects.filter(product=self)
    
    def feature(self):
        return Feature.objects.filter(product=self)
    
    class Meta:
        managed = True
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title   = models.CharField(max_length = 256)
    img     = models.ImageField(upload_to='gallery/')
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        ordering = ['title']
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class Feature(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    title       = models.CharField(max_length = 256)
    description = models.TextField()
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        ordering = ['title']
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


######################################## Cart section ########################################


class Order(models.Model):
    customer       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_order     = models.DateTimeField(auto_now_add=True)
    complete       = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.pk)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product    = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order      = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity   = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order      = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address    = models.CharField(max_length=200, null=True)
    city       = models.CharField(max_length=200, null=True)
    state      = models.CharField(max_length=200, null=True)
    zipcode    = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
