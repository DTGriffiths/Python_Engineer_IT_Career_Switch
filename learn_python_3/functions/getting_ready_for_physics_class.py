# Uncomment this when you reach the "Use the Force" section
# Create variables: train_mass, train_acceleration, train_distance, bomb_mass
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
def f_to_c(f_temp):
  '''Convert farenheit to celsius.'''
  # Return (farenheit - 32) * 5 / 9
  c_temp = (f_temp - 32) * 5/9
  return c_temp
# Create variable: f100_in_celsius = f_to_c(100)
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  '''Convert celsius to farenheit.'''
  # Return celsius * (9 / 5 + 32)
  f_temp = c_temp * (9/5 + 32)
  return f_temp
# Create variable: c0_in_fahrenheit = c_to_f(0)
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  '''Calculate force'''
  # Return mass * acceleration
  return mass * acceleration
# Create variable: train_force = get_force(train_mass, train_acceleration) and print
train_force = get_force(train_mass, train_acceleration)
print(f"Train force: {train_force}")
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3 * 10 ** 8):
  '''Calculate energy'''
  # Return mass * (c ** 2)
  return mass * (c ** 2)
# Create variable: bomb_energy = get_energy(bomb_mass) and print
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  '''Calculate work'''
  # Return force * distance
  force = get_force(mass, acceleration)
  return force * distance
# Create variable: train_work = get_work(train_mass, train_acceleration, train_distance) and print
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
