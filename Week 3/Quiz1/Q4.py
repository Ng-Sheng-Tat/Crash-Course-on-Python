def sum_divisors(n):
  divisor = 2
  if n == 0:
    return 0
  output = 1
  while divisor < n:
    if n%divisor==0:
      output = output + divisor
    else:
      pass
    divisor += 1
  return output

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
