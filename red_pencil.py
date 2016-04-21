STABLE_DAYS_LIMIT = 30
MIN_PRICE_REDUCTION = 5
MAX_PRICE_REDUCTION = 30

def is_red_pencil(prices):
    is_red_pencils = []

    days_stable = 1
    old_price = None
    is_on_sale = False

    for price in prices:
        is_on_sale = new_red_pencil(price, old_price, days_stable) or continue_red_pencil(is_on_sale, price, old_price)
        is_red_pencils.append(is_on_sale)

        if price == old_price:
            days_stable += 1
        else:
            days_stable = 1
            old_price = price

    return is_red_pencils

def continue_red_pencil(is_on_sale, price, old_price):
    return is_on_sale and not price > old_price
    
def new_red_pencil(price, old_price, days_stable):
    return is_price_reduced(price, old_price) and is_stable(days_stable)

def is_price_reduced(price, old_price):
    if old_price:
        percent_off = ((old_price - price) / old_price) * 100
        return percent_off >= MIN_PRICE_REDUCTION and percent_off <= MAX_PRICE_REDUCTION
    else:
        return False

def is_stable(days_stable):
    return days_stable >= STABLE_DAYS_LIMIT

