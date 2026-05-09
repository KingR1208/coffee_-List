from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService

router = APIRouter()

@router.post("/")
def create_user(user: UserCreate):
    return UserService.create_user(user)

@router.get("/company/{company_id}")
def get_users(company_id: int):
    return UserService.get_users_by_company(company_id)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return UserService.delete_user(user_id)