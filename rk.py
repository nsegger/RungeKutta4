import numpy as np 
from numpy.linalg import inv
from matplotlib import pyplot as plt

def F(t, x, y):
    return y + x - (x*(pow(x, 2) + pow(y, 2)))

def G(t, x, y):
    return x + y - (y*(pow(x, 2) + pow(y, 2)))

def RK4(x, y, h, t):
    pX = []
    pY = []

    pX.append(x)
    pY.append(y)

    for i in range(t-1):
        k1x = F(i, x, y)
        k1y = G(i, x, y)

        k2x = F(i + h/2, x + (k1x * h/2), y + (k1y * h/2))
        k2y = G(i + h/2, x + (k1x * h/2), y + (k1y * h/2))

        k3x = F(i + h/2, x + (k2x * h/2), y + (k2y * h/2))
        k3y = G(i + h/2, x + (k2x * h/2), y + (k2y * h/2))

        k4x = F(i + h, x + (k3x * h), y + (k3y * h))
        k4y = G(i + h, x + (k3x * h), y + (k3y * h))

        kx = ((k1x + 2*k2x + 2*k3x + k4x) / 6)
        ky = ((k1y + 2*k2y + 2*k3y + k4y) / 6)

        pX.append(pX[i] + kx)
        pY.append(pY[i] + ky)

    plt.figure(1)
    plt.subplot(111)
    plt.plot(np.array(pX), np.arange(t), 'bo', np.array(pY), np.arange(t), 'ro')
    plt.ylabel("Tempo")
    plt.xlabel("x: azul, y: vermelho")
    plt.axis([-10000, 50000, 0, t])
    plt.grid(True)

    plt.figure(2)
    plt.subplot(121)
    plt.plot(np.array(pX), np.array(pY), 'bo')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    plt.show()


def main():
    t = 30
    x = 1
    y = 2
    h = 1

    RK4(x, y, h, t)




if __name__ == "__main__":
    main()
