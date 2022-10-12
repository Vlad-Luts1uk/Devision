num1 = 0 
num2=int(input('First #: '))
divisor = int(input('First #: '))
while num2>=divisor: 
  num2 -=divisor
  num1 += 1

print (f'Quotient: {num1} & remainder {num2}')