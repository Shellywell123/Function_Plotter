import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

def run():
    func_string = input('input your function:\n')

    #lims preset fo now
    xfunc_lims = (-100,100)
    zfunc_lims = (-100,100)

    xlist = linspace(xfunc_lims[0],xfunc_lims[1],1000)
    zlist = linspace(zfunc_lims[0],zfunc_lims[1],1000)
    ylist = []


    for n in range (0,len(xlist)):
        x = xlist[n]
        z = zlist[n]

        try:
            y = eval(func_string)
            ylist.append(y)
        except:
            print('invalid input retry:')
            run()
        



    fig = plt.figure('Function_Plotter')
    ax = fig.add_subplot(111, projection='3d')
    plt.title('$y = '+func_string+'$')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    if 'z' in func_string:
        ax.plot(xlist,ylist,zlist)
    else:
        ax.plot(xlist,ylist)
    plt.show()

run()