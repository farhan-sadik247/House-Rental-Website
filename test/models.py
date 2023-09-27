from django.db import models
from django.contrib.auth.models import AbstractUser

# Defining database schema

class Manush(AbstractUser):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    occupation = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    dob = models.DateField(null = True)
    pic = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.username

class House(models.Model):
    details = models.TextField()
    price = models.DecimalField(max_digits= 10, decimal_places = 2, blank = False, null = False)
    pic = models.ImageField(upload_to='images/')
    location = models.TextField()
    manush = models.ForeignKey(Manush, on_delete = models.CASCADE)
    rent_date = models.DateField(blank = False, null = False)
    bedroom_no = models.IntegerField(blank = False, null = False)
    bathroom_no = models.IntegerField(blank = False, null = False)
    flat_size = models.IntegerField(blank = False, null = False)
    gender = models.TextField(blank=False,null=False,default='Both')
    
    
    FAMILY = 'family'
    BACHELOR = 'bachelor'
    SUBLET = 'sublet'
    TYPE_CHOICES = [
        (FAMILY, 'Family'),
        (BACHELOR, 'Bachelor'),
        (SUBLET, 'Sublet'),
    ]

    type = models.CharField(max_length = 10, choices = TYPE_CHOICES, default = FAMILY)   
    
    

    def __str__(self) -> str:
        return self.location

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    manush = models.ForeignKey(Manush, on_delete = models.CASCADE)

    @property
    def num_items(self):
        return len(self.cart_item_set.all())

    def __str__(self) -> str:
        return 'Cart of: ' + self.manush.username

class Cart_item(models.Model):
    # quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    house = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'Item: {self.house.location} for {self.cart.manush.username}'
    
class Search(models.Model):
    price1 = models.DecimalField(max_digits= 100, decimal_places = 2, blank = True, null = True)
    price2 = models.DecimalField(max_digits= 100, decimal_places = 2, blank = True, null = True)
    location = models.TextField(blank = True, null = True, default="")
    gender = models.TextField(blank=True,null=True,default='')
    
    
    FAMILY = 'family'
    BACHELOR = 'bachelor'
    SUBLET = 'sublet'
    TYPE_CHOICES = [
        (FAMILY, 'Family'),
        (BACHELOR, 'Bachelor'),
        (SUBLET, 'Sublet'),
    ]

    type = models.CharField(max_length = 10, choices = TYPE_CHOICES, default = None, blank = True, null = True)
