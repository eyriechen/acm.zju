import math

line  = raw_input()
num = int(line)
for i in range(1, num + 1):
    line = raw_input()
    xy = line.split()
    x = float(xy[0])
    y = float(xy[1])
    length = (x**2 + y**2) ** 0.5
    year = int((math.pi*length**2)/2/50) + 1
    print 'Property ' + str(i) + ': This property will begin eroding in year ' + str(year) + '.'

print 'END OF OUTPUT.'
