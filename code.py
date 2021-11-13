x = 1
pi = 1
tPi = 0
for i in range(999999999):
  pi =tPi + 1/x - 1/(x+2)
  x += 4
  tPi = pi
  print(pi*4)
  