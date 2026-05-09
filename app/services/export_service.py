import pandas as pd
from app.database import supabase

class ExportService:

    @staticmethod
    def export_company_orders():

        companies_response = (
            supabase
            .table("companies")
            .select("*")
            .execute()
        )

        companies = companies_response.data

        writer = pd.ExcelWriter(
            "coffee_report.xlsx",
            engine="openpyxl"
        )

        for company in companies:

            users_response = (
                supabase
                .table("users")
                .select("*")
                .eq("company_id", company["id"])
                .execute()
            )

            users = users_response.data

            rows = []

            for user in users:

                orders_response = (
                    supabase
                    .table("orders")
                    .select("*")
                    .eq("user_id", user["id"])
                    .execute()
                )

                orders = orders_response.data

                total = 0

                for order in orders:
                    total += order["total"]

                rows.append({
                    "Name": f'{user["first_name"]} {user["last_name"]}',
                    "Email": user["email"],
                    "Total": total
                })

            df = pd.DataFrame(rows)

            df.to_excel(
                writer,
                sheet_name=company["name"],
                index=False
            )

        writer.close()

        return "coffee_report.xlsx"