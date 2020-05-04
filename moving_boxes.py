'''
moving boxes problem presented by... numberfile? 3blue1brown?
Derek Jacobsen
2/28/20
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as rect
from matplotlib import animation

plt.close('all')

class box:
    def __init__(self, v0, mass, locX):
        self.velocity = v0
        self.mass = mass
        engy = self.energyFN()
        self.energy = engy
        self.loc = locX
        self.startLoc = locX
        self.shape = rect.Rectangle((self.loc,0),1,1,color = 'k')
        self.locList = []

    def energyFN(self):
        engy = 0.5*self.mass*self.velocity**2

        return engy

box1 = box(0, 1, 3)
box2 = box(-2, 10, 9)

axX = [-1,10]
axY = [0,0]

ax2Y = [-1,10]
ax2X = [0,0]

fig = plt.figure()
ax = plt.axes(xlim=(-1, 10), ylim=(-1, 5))


plt.plot(axX,axY)
plt.plot(ax2X,ax2Y)

dt = 0.01 #s
index = 0

while box2.loc <= 10:
    box1.locList.append(box1.loc)
    box2.locList.append(box2.loc)

    if box1.loc <= 0:
        box1.velocity = -1*box1.velocity
        box1.loc = box1.velocity * dt + box1.loc
        box2.loc = box2.velocity * dt + box2.loc
        index+=1

    elif box2.loc < box1.loc + 1:
        # collision 
        v1 = (box1.mass - box2.mass)/(box1.mass + box2.mass)*box1.velocity + (2*box2.mass)/(box1.mass +
                                                                                            box2.mass)*box2.velocity
        v2 = (box2.mass - box1.mass)/(box1.mass + box2.mass)*box2.velocity + (2*box1.mass)/(box1.mass +
                                                                                            box2.mass)*box1.velocity
        box1.velocity = v1
        box2.velocity = v2
        box1.loc = box1.velocity * dt + box1.loc
        box2.loc = box2.velocity * dt + box2.loc
        index += 1

    else:
        box1.loc = box1.velocity * dt + box1.loc
        box2.loc = box2.velocity * dt + box2.loc


print(str(index))

def init():
    # something that says the boxes moving needs to be updated each frame... and only the boxes... only two box objects?
    ax.add_patch(box1.shape)
    ax.add_patch(box2.shape)
    
    return box2.shape, box1.shape
    


def animate(i):
    
    box2.shape.set_xy([box2.locList[i],0])
    box1.shape.set_xy([box1.locList[i],0])
    
    return box2.shape, box1.shape,


anim = animation.FuncAnimation(fig, animate, init_func = init, frames = len(box1.locList), interval = 20, blit = True)



plt.show()
