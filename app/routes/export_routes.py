from fastapi import APIRouter
from app.services.export_service import ExportService

router = APIRouter()

@router.get("/")
def export_report():

    file_name = ExportService.export_company_orders()

    return {
        "message": "Export completed",
        "file": file_name
    }