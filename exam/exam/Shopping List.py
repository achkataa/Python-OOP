def shopping_list(budget, **kwargs):
    result = []
    if budget < 100:
        return "You do not have enough budget."

    for key, value in kwargs.items():
        price = value[0] * value[1]
        if price <= budget:
            budget -= price
            result.append(f"You bought {key} for {price:.2f} leva.")
            if len(result) == 5:
                break
    return '\n'.join(result)




print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


