from django.db import models

# Create your models here.
class ShoppingList(models.Model):
    list_id = models.UUIDField()
    list_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    status = models.CharField(default="available", max_length=20)
    buy_day = models.DateField(null=True)


class UserList (models.Model):
    user_id = models.IntegerField()
    list_id = models.UUIDField()


class MallList(models.Model):
    name = models.CharField(max_length=50)
    list_id = models.UUIDField()


class Item(models.Model):
    name = models.CharField(max_length=50)
    shop_id = models.ForeignKey(MallList, on_delete=models.CASCADE)