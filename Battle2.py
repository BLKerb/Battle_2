a='level'
half = int(len(a) / 2)

tes_1 = a[:half]
tes_2 = a[half:]

if tes_1 == tes_2[::-1]:
  print(a, 'pa palendwòm')

else:
  print(a, 'palendwòm')
