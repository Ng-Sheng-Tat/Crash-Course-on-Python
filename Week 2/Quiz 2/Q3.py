def lucky_number(name):
  number = len(name) * 9
  output = "Hello " + name + ". Your lucky number is " + str(number)
  return output
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))