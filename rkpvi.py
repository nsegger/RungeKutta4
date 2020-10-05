import numpy as np
from matplotlib import pyplot as plt

def F(x, y):
  return x - y + 2

def RK4(x, y, h, t):
  data = []
  pX = []
  pY = []

  x0 = x

  for i in range(t):
    x = x0 + (h * i)

    k1 = F(x, y)

    k2 = F(x + h/2, y + (k1 * h/2))
    
    k3 = F(x + h/2, y + (k2 * h/2))
  
    k4 = F(x + h, y + (k3 * h))
    
    data.append([i, x, y, k1, k2, k3, k4])
    pX.append(x)
    pY.append(y)
    
    y = y + ((k1 + 2*k2 + 2*k3 + k4) * (h/6))

  return data, pX, pY


def main():
  t = 6
  x = 0
  y = 2
  h = 0.2

  columns = ('i', 'xi', 'yi', 'k1', 'k2', 'k3', 'k4')

  data, pX, pY = RK4(x, y, h, t)

  cellText = []
  for item in data:
    cellText.append(['%.2f' % x for x in item])

  fig, axs = plt.subplots(2, 1)
    
  table = axs[0].table(cellText=cellText, colLabels=columns, loc='center')
  axs[0].axis('off')
  axs[0].axis('tight')

  axs[1].plot(np.array(pX), np.array(pY), 'b')
  plt.xlabel("x")
  plt.ylabel("y")
  plt.grid(True)

  plt.show()

if __name__ == "__main__":
  main()
