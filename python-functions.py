def sum_to(n):
  sum = 0
  for number in range(1,n+1):
    sum += number
  return sum

# print(sum_to(10))

def largest(li):
  return max(li)

# print(largest([1,289, 2, 3, 4, 0, 289, 278]))

def occurences(str_1, str_2):
  counter = 0
  if len(str_2) == 1:
    for character in str_1:
      if str_2 in character:
        counter += 1
  else:
    for word in str_1.split():
          if str_2 in word:
            counter += 1
  return counter

# print(occurences('fleep floop', 'ee'))
