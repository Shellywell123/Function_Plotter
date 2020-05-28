import matplotlib.pyplot as plt
from numpy import *

xfunc_lims = (-10,10)
yfunc_lims = (-5,5)
zfunc_lims = (-5,5)

x1list = linspace(xfunc_lims[0],xfunc_lims[1],1000)
y1list = list(zeros(len(x1list)))
z1list = []

x2list = linspace(xfunc_lims[0],xfunc_lims[1],1000)
y2list = list(zeros(len(x2list)))
z2list = []

x3list = linspace(xfunc_lims[0],xfunc_lims[1],1000)
y3list = list(zeros(len(x3list)))
z3list = []

x4list = linspace(xfunc_lims[0],xfunc_lims[1],1000)
y4list = list(zeros(len(x4list)))
z4list = []

for n in range(0,len(x1list)):
    x=x1list[n]
    z1 = 1.5*sqrt((-abs(abs(x) - 1)) * abs(3 - abs(x))/((abs(x) - 1)*(3 - abs(x)))) * (1+abs(abs(x) - 3)/(abs(x)- 3)) * sqrt(1 - (x/7)**2)+(4.5+0.75 * (abs(x - 0.5)+abs(x+0.5)) - 2.75 * (abs(x-0.75)+abs(x+0.75))) * (1+abs(1 - abs(x))/(1 - abs(x)))
    z1list.append(z1)

for n in range(0,len(x2list)):
    x=x2list[n]
    z2 = (-3)*sqrt(1 -(x/7)**2) * sqrt(abs(abs(x) - 4)/(abs(x)-4))
    z2list.append(z2)

for n in range(0,len(x3list)):
    x=x3list[n]
    z3 = abs(x/2) - 0.0913722 * x**2-3+sqrt(1 - (abs(abs(x) - 2) - 1)**2)
    z3list.append(z3)

for n in range(0,len(x4list)):
    x=x4list[n]
    z4 = (2.71052+1.5 - 0.5 * abs(x) - 1.35526 * sqrt(4 - (abs(x) - 1)**2)) * sqrt(abs(abs(x) - 1)/(abs(x) - 1))
    z4list.append(z4)

fig = plt.figure('Batman_Plotter')
ax = fig.add_subplot(111, projection='3d')
title_obj = plt.title('$Batman$')
ax.plot(x1list,y1list,z1list,label='$Batman$',c='yellow')
#ax.plot(x2list,y2list,z2list,c='yellow')
#ax.plot(x3list,y3list,z3list,c='yellow')
#ax.plot(x4list,y4list,z4list,c='yellow')
#from MPLP import MPL_Prefs
#MPL_Prefs(fig,ax,title_obj,'grid')

plt.show()