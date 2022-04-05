def sum_to(n):
  sum = 0
  for number in range(1,n+1):
    sum += number
  return sum

print(sum_to(10))