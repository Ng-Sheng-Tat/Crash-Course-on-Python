def is_palindrome(input_string):
	# We'll create two strings, to compare them
	input_string = input_string.replace(" ", "")


	input_string = input_string.lower()

	if input_string[-1::-1]==input_string:
		return True
	return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
