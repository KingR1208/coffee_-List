from pydantic import BaseModel

class UserCreate(BaseModel):
    company_id: int
    first_name: str
    last_name: str
    email: str
    pin: str