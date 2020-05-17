import matplotlib.pyplot as plt
from numpy import *

def run():
    func_string = input('input your function:\n')

    #lims preset fo now
    xfunc_lims = (-100,100)

    xlist = linspace(xfunc_lims[0],xfunc_lims[1],1000)
    ylist = []

    for n in range (0,len(xlist)):
        x = xlist[n]

        try:
            y = eval(func_string)
            ylist.append(y)
        except:
            print('invalid input retry:')
            run()

    plt.figure('Function_Plotter')
    plt.title('$y = '+func_string+'$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(xlist,ylist)
    plt.grid()
    plt.show()

run()