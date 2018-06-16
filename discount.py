unit=int(input('enter total no. of unit to purchase'))
if unit<11:
  cost=unit*100
  print('cost will be:',cost)
else:
  cost=unit*100-unit*10/100
  print('cost will be:',cost)
	  