def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)

sum(map(int, list(str(factorial(100)))))
