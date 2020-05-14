from random import randrange

num_items = 100

max_value = randrange(1, num_items + 1)
print(max_value)

num_updates = 0 
for i in range(1, num_items):
  current = randrange(1, num_items + 1)

  if current > max_value:
    max_value = current
    num_updates = num_updates + 1 
    print(current, "<= Update")
  else:
    print(current)
print(f"The maximum value found was {max_value}")
print(f"The maximum value was updated {num_updates} times")