from typing import List

from pydantic import BaseModel, validator
from bank.models import BankItem

class BankItemIn(BaseModel):
    id: int
    quantity: int
    name: str

class BankItemSchema(BaseModel):
    bank_items: List[BankItemIn]
    player_name: str
