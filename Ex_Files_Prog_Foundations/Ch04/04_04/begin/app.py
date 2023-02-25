miles = input('Enter a distance in miles: ')
miles_value = float(miles)
exchange = 1.609344
kilometers_value = miles_value * exchange

print("")
if kilometers_value > 1 :
  print(f'{miles} miles is equal to {kilometers_value} kilometers')
else :
  print(f'{miles} miles is equal to {kilometers_value} kilometer')

print("")


print('meow' * 5)
