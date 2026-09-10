# Create lists: hairstyles, prices, last_week
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# Create variable: total_price = 0
total_price = 0

# Iterate prices, add price to total_price
for price in prices:
  total_price += price
# Create variable: average_price and print
average_price = total_price / len(prices)
print(f"Average Haricut Price: {average_price}")

# Create list: new_prices and print
new_prices = [price - 5 for price in prices]
print(new_prices)

# Create variable: total_revenue
total_revenue = 0
# Iterate range of lenght of hairstyle, add to total_revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i]
  total_revenue += last_week[i]
# Print total_revnue
print(f"Total Revenue: {total_revenue}")

# Create variable: average_daily_revenue and print
average_daily_revenue = total_revenue / 7
print(f"average_daily_revenue: {average_daily_revenue}")

# Create list comprehension: cuts_under_30 and print
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f"cuts_under_30: {cuts_under_30}")
