half = int(len(a) / 2)

tes_1 = tes_2 = a[:half] a[half:]

if tes_1 == tes_2[::-1]:

else:

print(a, 'palendwòm') print(a, 'pa palendwòm')
