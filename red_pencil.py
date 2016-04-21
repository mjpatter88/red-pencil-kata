STABLE_DAYS_LIMIT = 30
MINIMUM_PRICE_REDUCTION = 5
MAXIMUM_PRICE_REDUCTION = 30

def is_red_pencil(prices):
    is_red_pencils = []

    days_stable = 1
    old_price = None
    is_on_sale = False

    for index, price in enumerate(prices):
        if qualifies_for_red_pencil(price, old_price, days_stable) or continue_red_pencil(is_on_sale, price, old_price):
            is_on_sale = True
        else:
            is_on_sale = False
        is_red_pencils.append(is_on_sale)

        if price == old_price:
            days_stable += 1
        else:
            days_stable = 1
            old_price = price

    return is_red_pencils

def continue_red_pencil(is_on_sale, price, old_price):
    return is_on_sale and not price > old_price
    
def qualifies_for_red_pencil(price, old_price, days_stable):
    return is_price_reduced(price, old_price) and is_stable(days_stable)

def is_price_reduced(price, old_price):
    if old_price:
        percent_discount = ((old_price - price) / old_price) * 100
        return percent_discount >= MINIMUM_PRICE_REDUCTION and percent_discount <= MAXIMUM_PRICE_REDUCTION
    else:
        return False

def is_stable(days_stable):
    return days_stable >= STABLE_DAYS_LIMIT

