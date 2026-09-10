# Your code below:
# Create lists: toppings, prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# Create vairable: num_two_dollar_slices and print
num_two_dollar_slices = prices.count(2)
print(f"num_two_dollar_slices: {num_two_dollar_slices}")

# Create variable: num_pizzas and print
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

# Create list of lists: pizza_and_prices and print
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(f"pizza_and_prices: {pizza_and_prices}")

# Sort pizza_and prices and print
pizza_and_prices.sort()
print(f"pizza_and_prices: {pizza_and_prices}")

# Create variables: cheapest_pizza, priciest_pizza
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
# Pop last value from pizza_and_prices
pizza_and_prices.pop()
# Insert 2 and a list to pizza_and_prices
pizza_and_prices.insert(2, [2.5, "peppers"])

# Create variable: three_cheapest and print
three_cheapest = pizza_and_prices[0:2]
print(f"pizza_and_prices: {pizza_and_prices}")
print(f"three_cheapest: {three_cheapest}")
