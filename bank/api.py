from typing import List

from django.core.exceptions import ObjectDoesNotExist
from ninja import NinjaAPI
from ninja.errors import ValidationError

from .models import BankItem
from .schemas import PlayerBankItemIn, BankItemsIn


api = NinjaAPI()

@api.post("/bank-items/")
def create_bank_items(request, data: BankItemsIn):
    # player, _ = Player.objects.get_or_create(name=player_name)


    for item_data in data.bank_items:
        print(item_data)
        # Get or create the BankItem instance based on the item_id
        try:
            bank_item = BankItem.objects.get(item_id=item_data.id)
        except ObjectDoesNotExist:
            bank_item = BankItem.objects.create(name=item_data.name, item_id=item_data.id, quantity=item_data.quantity)

        # Update the quantity and save the BankItem instance
        bank_item.quantity = item_data.quantity
        bank_item.save()

        # Add the bank item to the player's bank items
        #player.bank_items.add(bank_item)

    return {"detail": "Bank items saved successfully"}

@api.exception_handler(ValidationError)
def custom_validation_errors(request, exc):
    print(exc.errors)  # <--------------------- !!!!
    return api.create_response(request, {"detail": exc.errors}, status=422)