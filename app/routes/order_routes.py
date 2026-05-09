from fastapi import APIRouter
from app.schemas.order_schema import OrderCreate
from app.services.order_service import OrderService

router = APIRouter()

@router.post("/")
def create_order(order: OrderCreate):
    return OrderService.create_order(order)