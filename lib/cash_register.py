class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.transaction_history = []

    def add_item(self, item_price, item_quantity=1):
        self.total += item_price * item_quantity
        self.transaction_history.append((item_price, item_quantity))

    def apply_discount(self, discount):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            raise ValueError("Discount must be an integer between 0 and 100")
        discount_amount = self.total * discount // 100
        self.total -= discount_amount
        return discount_amount

    def void_last_transaction(self):
        if not self.transaction_history:
            raise ValueError("No transactions to void")
        last_transaction = self.transaction_history.pop()
        self.total -= sum(last_transaction)