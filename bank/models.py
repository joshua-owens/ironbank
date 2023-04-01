from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)

class BankItem(models.Model):
    item_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Player, related_name="bank_items")


class BankItemPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bank_item = models.ForeignKey(BankItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

