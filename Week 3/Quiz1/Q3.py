def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while True:

    if n%2 == 0 and n!=0:
      return True
    elif n<2 and n!=0:
      return True
  # If after dividing by two the number is 1, it's a power of two
    else:
      return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False