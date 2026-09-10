# Create variable: weight
weight = 41.5
# Ground Shipping
# If/elif weight, print weights multiplied and added
if weight <= 2:
  print((weight * 1.50) + 20)
elif 2 < weight <= 6:
  print((weight * 3.00) + 20)
elif 6 < weight <= 10:
  print((weight * 4.00) + 20)
elif weight > 10:
  print((weight * 4.75) + 20)

# Premium Shipping
# Create variable: cost_ground_premium and print
cost_ground_premium = 125.00
print(f"Cost of the ground shipping premium: ${cost_ground_premium}")

# Drone Shipping
# If/elif weight, print weight multiplied
if weight <= 2:
  print(weight * 4.50)
elif 2 < weight <= 6:
  print(weight * 9.00)
elif 6 < weight <= 10:
  print(weight * 12.00)
elif weight > 10:
  print(weight * 14.25)
