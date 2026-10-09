
recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 60


total_spent = sum(recent_purchases)


print(f"Total spent: ${total_spent:.2f}")


if total_spent > budget:
   print("Total spending is above budget.")
else:
   print("Total spending is within budget.")
