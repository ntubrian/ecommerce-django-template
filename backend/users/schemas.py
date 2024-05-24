from pydantic import BaseModel, EmailStr, StringConstraints
from typing_extensions import Annotated
from typing import Literal

class BusinessUserSchema(BaseModel):
    username: Annotated[str, StringConstraints(min_length=3, max_length=255)]
    email: EmailStr
    role: Literal[
        'admin',
        'store_manager',
        'product_manager',
        'order_manager',
        'customer_support',
        'finance_manager',
        'marketing_specialist'
    ]

    class Config:
        orm_mode = True
