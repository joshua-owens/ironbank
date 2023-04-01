from typing import List

from pydantic import BaseModel, validator
from bank.models import BankItem

class BankItemIn(BaseModel):
    id: int
    quantity: int
    name: str

class BankItemsIn(BaseModel):
    bank_items: List[BankItemIn]


class PlayerBankItemIn(BaseModel):
    bank_item: BankItemIn
    player_name: str