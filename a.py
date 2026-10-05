import numpy as np
import matplotlib.pyplot as plot

x = np.linspace(-np.pi, np.pi, 1000)
f = x**2
n1 = np.pi**2/3 + 4*((-1)**1/1**2)*np.cos(x)
n2 = np.pi**2/3 + 4* (((-1)**1/1**2)*np.cos(x)+ ((-1)**2/2**2)*np.cos(2*x))
n3 = np.pi**2/3
for k in range(1, 4):
    n3 += 4*((-1)**k/k**2)*np.cos(k*x)
n7 = np.pi**2/3
for k in range(1, 8):
    n7 += 4*((-1)**k/k**2)*np.cos(k*x)
plot.plot(x, f, label="x^2")
plot.plot(x, n1, label="n=1")
plot.plot(x, n2, label="n=2")
plot.plot(x, n3, label="n=3")
plot.plot(x, n7, label="n=7")
plot.legend()
plot.show()
