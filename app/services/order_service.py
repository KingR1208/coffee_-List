from app.database import supabase

class OrderService:

    @staticmethod
    def create_order(order_data):

        total = 0

        order_items = []

        for item in order_data.items:

            product_response = (
                supabase
                .table("products")
                .select("*")
                .eq("id", item.product_id)
                .execute()
            )

            product = product_response.data[0]

            item_total = (
                product["price"] * item.quantity
            )

            total += item_total

            order_items.append({
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": product["price"]
            })

        order_response = (
            supabase
            .table("orders")
            .insert({
                "user_id": order_data.user_id,
                "total": total
            })
            .execute()
        )

        created_order = order_response.data[0]

        for item in order_items:

            supabase.table("order_items").insert({
                "order_id": created_order["id"],
                "product_id": item["product_id"],
                "quantity": item["quantity"],
                "price": item["price"]
            }).execute()

        return {
            "message": "Order created successfully",
            "order_id": created_order["id"],
            "total": total
        }