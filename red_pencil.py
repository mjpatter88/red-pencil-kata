STABLE_DAYS_LIMIT = 30
MINIMUM_PRICE_REDUCTION = 5
MAXIMUM_PRICE_REDUCTION = 30

def is_red_pencil(prices):
    is_red_pencils = []

    days_stable = 1
    old_price = None
    on_sale = False

    for index, price in enumerate(prices):
        if is_price_reduced(price, old_price) and is_stable(days_stable) or on_sale:
            on_sale = True
        else:
            on_sale = False
        is_red_pencils.append(on_sale)

        if price == old_price:
            days_stable += 1
        else:
            days_stable = 1
            old_price = price

    return is_red_pencils

def is_price_reduced(price, old_price):
    if old_price:
        percent_discount = ((old_price - price) / old_price) * 100
        return percent_discount >= MINIMUM_PRICE_REDUCTION and percent_discount <= MAXIMUM_PRICE_REDUCTION
    else:
        return False

def is_stable(days_stable):
    return days_stable >= STABLE_DAYS_LIMIT

