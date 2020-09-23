"""

Author: Brady Trenary

"""

def calculated_price(price, cash_coupon, percent_coupon):
    with_cash_coupon = price - cash_coupon
    with_percent_coupon = with_cash_coupon - (with_cash_coupon * percent_coupon/100)
    subtotal_tax = with_percent_coupon * 1.06
    shipping = 0
    if with_percent_coupon < 10:
        shipping = 5.95
    elif with_percent_coupon < 30:
        shipping = 7.95
    elif with_percent_coupon < 50:
        shipping = 11.95
    else:
        shipping = 0

    return subtotal_tax + shipping


if __name__ == '__main__':
    calculated_price(15.99, 5, 10)
