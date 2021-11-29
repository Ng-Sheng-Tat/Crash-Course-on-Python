# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)def lucky_number(name):
  number = len(name) * 9
  output = "Hello " + name + ". Your lucky number is " + str(number)
  return output
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))