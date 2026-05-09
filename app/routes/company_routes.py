from fastapi import APIRouter
from app.schemas.company_schema import CompanyCreate
from app.services.company_service import CompanyService

router = APIRouter()

@router.post("/")
def create_company(company: CompanyCreate):
    return CompanyService.create_company(company)

@router.get("/")
def get_companies():
    return CompanyService.get_all_companies()