from app.database import supabase

class CompanyService:

    @staticmethod
    def create_company(company_data):

        data = {
            "name": company_data.name,
            "logo_url": company_data.logo_url
        }

        response = (
            supabase
            .table("companies")
            .insert(data)
            .execute()
        )

        return response.data

    @staticmethod
    def get_all_companies():

        response = (
            supabase
            .table("companies")
            .select("*")
            .execute()
        )

        return response.data