def divisors(n):
  if n == 1:
    return [1]

  ret = []
  for i in range(1, n):
    if n % i == 0:
      ret.append(i)

  return ret

divisors(11)
divisors(10)
divisors(12)

def divisor_sum(n):
  '''
  aka the 'd' function
  '''
  return sum(divisors(n))

divisor_sum(220) == 284

def is_amicable(n):
  if divisor_sum(n) == n:
    # perfect numbers are not amicable
    return False
  return divisor_sum(divisor_sum(n)) == n

is_amicable(220) == True
is_amicable(1)
is_amicable(2)

divisors(28)

the_sum = 0
for i in range(1,10000):
  if is_amicable(i):
    print(i)
    the_sum+=i

print()
print(the_sum)
