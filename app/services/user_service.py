from app.database import supabase

class UserService:

    @staticmethod
    def create_user(user_data):

        data = {
            "company_id": user_data.company_id,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name,
            "email": user_data.email,
            "pin": user_data.pin
        }

        response = (
            supabase
            .table("users")
            .insert(data)
            .execute()
        )

        return response.data

    @staticmethod
    def get_users_by_company(company_id):

        response = (
            supabase
            .table("users")
            .select("*")
            .eq("company_id", company_id)
            .execute()
        )

        return response.data

    @staticmethod
    def delete_user(user_id):

        response = (
            supabase
            .table("users")
            .delete()
            .eq("id", user_id)
            .execute()
        )

        return response.data