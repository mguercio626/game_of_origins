import numpy as np
import matplotlib.pyplot as plt


def electric_force(dist):
    multiplier = 1
    charge1 = 1
    charge2 = 1
    return (multiplier * charge1 * charge2) / (dist**2)


def collision_force(dist):
    multiplier = 1
    return  -1 * multiplier / ((dist*10)**3)


ef = np.vectorize(electric_force)
cf = np.vectorize(collision_force)
x = np.arange(0.000001,1,0.000001)
yef = ef(x)
ycf = cf(x)


plt.axis([0, 0.1, -1000000, 1000000])
plt.plot(x, yef)
plt.plot(x, ycf)
plt.plot(x, yef + ycf)
plt.xlabel("distance")
plt.ylabel("force")
plt.show()
