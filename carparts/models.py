from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name= models.CharField(max_length=300)
    model_no= models.IntegerField()
    variant= models.CharField(max_length=500)
    company= models.CharField(max_length=400)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    quantity_stock = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name= models.CharField(max_length=400)
    phone_no= models.IntegerField()
    city= models.CharField(max_length=400)
    area_address= models.CharField(max_length=2000)
    email= models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount=models.IntegerField()
    date_of_order= models.DateTimeField('date ordered')



class Order_detail(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    sub_total= models.IntegerField()







