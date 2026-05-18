from datetime import datetime


class ReturnRequest:
    def __init__(self, return_id, order_id, product_name, quantity, reason):
        self.return_id = return_id
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.reason = reason
        self.status = "Pending"
        self.request_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def approve_return(self):
        self.status = "Approved"

    def reject_return(self):
        self.status = "Rejected"

    def display_return(self):
        print("=" * 40)
        print("Return ID:", self.return_id)
        print("Order ID:", self.order_id)
        print("Product:", self.product_name)
        print("Quantity:", self.quantity)
        print("Reason:", self.reason)
        print("Status:", self.status)
        print("Date:", self.request_date)
        print("=" * 40)


def create_return_request(return_requests, order_id, product_name, quantity, reason):
    new_return = ReturnRequest(
        len(return_requests) + 1,
        order_id,
        product_name,
        quantity,
        reason
    )

    return_requests.append(new_return)

    print("Return request created successfully.")
    return new_return