import sys
sys.path.append('/usr/lib/python2.7/dist-packages/numpy')

from numpy import sin, linspace
x = linspace(0, 4, 11)
y = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabet('f(x)')
plt.title('funkcija $sin(x)$')
plt.plot(x, y, color = '#FF0000')

y1 = x
plt.plot(x, y1, color = '#00FF00')

#
