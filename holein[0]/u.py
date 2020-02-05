j = 200
def r(n):
 if n == 0 or n == 1:
  return True
 for i in [2, 3, 5]:
  if n%i == 0:
   return r(n//i)
 return False
for i in range(2, j):
 if r(i):
  print(i)