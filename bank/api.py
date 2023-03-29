from typing import List
from ninja import NinjaAPI
from .models import BankItem
from .schemas import BankItemIn


api = NinjaAPI()

@api.post("/bank-items/")
def create_bank_items(request, player_name: str, bank_items: List[BankItemIn]):
    # player, _ = Player.objects.get_or_create(name=player_name)

    print(player_name)
    print(bank_items)

    for item_data in bank_items:
        # Get or create the BankItem instance based on the item_id
        try:
            bank_item = BankItem.objects.get(item_id=item_data.item_id)
        except ObjectDoesNotExist:
            bank_item = BankItem.objects.create(**item_data.dict())

        # Update the quantity and save the BankItem instance
        bank_item.quantity = item_data.quantity
        bank_item.save()

        # Add the bank item to the player's bank items
        #player.bank_items.add(bank_item)

    return {"detail": "Bank items saved successfully"}
