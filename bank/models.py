from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)

class BankItem(models.Model):
    item_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    players = models.ManyToManyField(Player, related_name="bank_items")
