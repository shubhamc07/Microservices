from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default="pending")
