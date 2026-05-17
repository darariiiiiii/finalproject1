class Discount:
    def apply_discount(self, price):
        return price


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, price):
        discount_amount = price * self.percent / 100
        return price - discount_amount


class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        final_price = price - self.amount

        if final_price < 0:
            return 0
        else:
            return final_price


def apply_promo_code(price, promo_code):
    promo_code = promo_code.upper()

    if promo_code == "SALE10":
        discount = PercentageDiscount(10)
        return discount.apply_discount(price)

    elif promo_code == "WELCOME5000":
        discount = FixedDiscount(5000)
        return discount.apply_discount(price)

    else:
        return price