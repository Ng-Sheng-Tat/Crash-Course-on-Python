def format_address(address_string):
  # Declare variables

  # Separate the address string into parts
  address_string = address_string.split()
  firststr = address_string[0]
  # print(firststr)
  dummylist = address_string[1:]
  secondstr = " ".join(dummylist )
  # print(secondstr)
  # print(address_string)
  # print(dummylist)
  # Traverse through the address parts
  # for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {0} on street named {1}".format(firststr, secondstr)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
