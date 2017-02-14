from matplotlib import pyplot as plt
from matplotlib import animation
from copy import copy

data = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubbleSort(alist):
    y_list = []
    y_list.append(copy(alist))

    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        y_list.append(copy(alist))

    return y_list


y_list = data
y_list = bubbleSort(y_list)

x_list = range(1, len(y_list) + 1)

fig = plt.figure()
ax = plt.axes(xlim=(x_list[0] - 1, x_list[-1] + 1), ylim=(y_list[-1][0] - 1, y_list[-1][-1] + 1))
line, = ax.plot([], [], 'ro')


def init():
    line.set_data([], [])
    return line,


def animate(i):
    line.set_data(x_list, y_list[i])
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x_list) - 1, interval=500, blit=True)

# anim.save('bubbleSort_animation.gif')

plt.show()
