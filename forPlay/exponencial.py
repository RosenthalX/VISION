import numpy as np
import matplotlib.pyplot as plt


X = np.arange(-10,10,0.1)

_,(plt1,plt2,plt3) = plt.subplots(3)

y = 1/(1+np.exp(-X))
plt1.plot(X,y,c="b",label="exponencial",linewidth=3)

X = np.arange(-10,10,0.1)
y1 = np.exp(-X)
plt2.plot(X,y1,c="g",label="exponencial2",linewidth=3)

X = np.arange(-10,10,0.1)
y2 = np.log(1+np.exp(X))
plt3.plot(X,y2,c="r",label="exponencial3",linewidth=3)
plt.yticks(np.arange(-5,25,1))
plt.xticks(np.arange(-15,15,1))

plt.yticks(np.arange(-5,25,1))
plt.xticks(np.arange(-15,15,1))

plt.yticks(np.arange(-5,25,1))
plt.xticks(np.arange(-15,15,1))

plt1.grid()
plt2.grid()
plt3.grid()


plt.plot(X,y2,c="r",label="exponencial",linewidth=3)
#plt.grid()
plt.show()  