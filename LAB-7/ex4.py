

def check_budget(budget):
    total_spent = 0

    for purchase in [36.13, 23.87, 183.35, 22.93, 11.62]:
        total_spent += purchase
        if total_spent > budget:
            print(f"This purchase of {purchase} is above budget.")
            continue
        else:
            print(f"This purchase of {purchase} is within budget.")


check_budget(600)