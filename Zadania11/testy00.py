from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import copy

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
line, = ax.plot([], [], 'ro')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

def bubbleSort(alist):
    y_list = []

    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        y_list.append(copy.copy(alist))

    return y_list

y_list = [9,8,7,6,5,4,3,2,1]
y_list = bubbleSort(y_list)

x_list = range(1, len(y_list)+2)


def animate(i):
    y = np.array(y_list[i])
    line.set_data(x_list, y_list[i])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x_list)-1, interval=500, blit=True)

anim.save('basic_animation.gif')

plt.show()