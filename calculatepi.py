pi = 3
temporary = 2

while True:
  pi = pi + 4/(temporary*(temporary+1)*(temporary+2)) - 4/((temporary+2)*(temporary+3)*(temporary+4))
  temporary = temporary + 4
  print(pi)
  
