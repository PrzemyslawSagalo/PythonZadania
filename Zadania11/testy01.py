import matplotlib.pyplot as plt
import copy

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

alist = [9,8,7,6,5,4,3,2,1]
y_list = bubbleSort(alist)


fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 20))

x_list = range(1,10)

print x_list, y_list

line, = ax.plot(x_list, y_list[0] , 'ro')
plt.axis([0, 10, 0, 10])
plt.show()

