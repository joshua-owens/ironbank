from django.contrib import admin
from .models import Player, BankItem, BankItemPlayer

admin.site.register(Player)
admin.site.register(BankItem)
admin.site.register(BankItemPlayer)