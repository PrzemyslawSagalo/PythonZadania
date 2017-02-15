import circles
import matplotlib.pyplot as plt


C1 = circles.Circle(1,5,2)
C2 = circles.Circle(1,1,1)

C3 = C1.cover(C2)
print C3


circle1 = plt.Circle((C1.pt.x,C1.pt.y), C1.radius, color='g',fill=False)
circle2 = plt.Circle((C2.pt.x,C2.pt.y), C2.radius, color='b',fill=False)
circle3 = plt.Circle((C3.pt.x,C3.pt.y), C3.radius, color='r',fill=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

ax.set_xlim(-3,8)
ax.set_ylim(-3,8)

plt.show()