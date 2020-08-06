###### to calculate the linear velocity of my robot ######
############## Zahra Ghasemi - 955367022 #################

import math
import numpy as np
import matplotlib.pyplot as plt

time = []
Vee = []
for i in range(60):
    l1 = 40+i
    l2 = 100
    l3 = 100
    l4 = 40+i
    
    th1 = math.radians(i)
    th2 = math.radians(i)
    
    # Jacobian matrix
    Jv = ([l4*math.cos(th1+th2)-l3*math.sin(th1)+l2, l4*math.cos(th1+th2), 0, math.sin(th1+th2)],
          [0, 0, 0, 0],
          [l4*math.sin(th1+th2)+l3*math.cos(th1), l4*math.sin(th1+th2), 1, math.cos(th1+th2)])
    
    # the velocities
    thetai = ([math.radians(1)],
              [math.radians(1)],
              [1],
              [1])
    
    # Jacobian*velocities
    Vv = np.dot(Jv,thetai)
    Vee.append(math.sqrt(Vv[0]**2+Vv[1]**2+Vv[2]**2))
    time.append(i)
    
#print(Vee)
#print(time)

x = time
y = Vee

plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('Vee')
plt.show()