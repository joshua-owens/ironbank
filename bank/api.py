from typing import List

from django.core.exceptions import ObjectDoesNotExist
from ninja import NinjaAPI
from ninja.errors import ValidationError

from .models import BankItem, Player, BankItemPlayer
from .schemas import BankItemSchema


api = NinjaAPI()

@api.post("/bank-items/")
def create_bank_items(request, data: BankItemSchema):
    player, _ = Player.objects.get_or_create(name=data.player_name)


    for item_data in data.bank_items:
        bank_item, _ = BankItem.objects.get_or_create(name=item_data.name, item_id=item_data.id)

        # Update the quantity on the intermediate model
        bank_item_player, created = BankItemPlayer.objects.update_or_create(
            player=player,
            bank_item=bank_item,
            defaults={'quantity': item_data.quantity}
        )
    return {"detail": "Bank items saved successfully"}

@api.exception_handler(ValidationError)
def custom_validation_errors(request, exc):
    print(exc.errors)  # <--------------------- !!!!
    return api.create_response(request, {"detail": exc.errors}, status=422)