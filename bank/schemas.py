from pydantic import BaseModel, validator
from bank.models import BankItem

class BankItemIn(BaseModel):
    item: list

    @validator('item')
    def validate_bank_item(cls, value):
        # Implement your validation logic here, for example:
        if not isinstance(value, BankItem):
            raise ValueError("Invalid BankItem")
        return value
