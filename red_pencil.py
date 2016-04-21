def is_red_pencil(prices):
    is_red_pencils = []

    days_stable = 1
    old_price = None
    on_sale = False

    for index, price in enumerate(prices):
        price_reduction_percent = ((prices[index-1] - price) / prices[index-1]) * 100
        if price_reduction_percent >= 5 and price_reduction_percent <= 30 and days_stable >= 30 or on_sale:
            is_red_pencils.append(True)
            on_sale = True
        else:
            is_red_pencils.append(False)
            on_sale = False
        if price == old_price:
            days_stable += 1
        else:
            days_stable = 1
            old_price = price

    return is_red_pencils
