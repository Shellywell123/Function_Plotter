import matplotlib.pyplot as plt
from numpy import *

def run():
    """
    """
    #deafult form y=..
    fvar = 'y'
    func_string = input('input your function:\n')

    #lims preset for now
    xfunc_lims = (-100,100)

    if '=' not in func_string:
        print( 'function requires "=", e.g "y=mx+c"')
        run()

    if ('y =' in func_string) or ('y=' in func_string):
        fvar = 'y'
        func_string = func_string.split('=')[1]
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

    if ('x =' in func_string) or ('x=' in func_string):
        fvar = 'x'
        func_string = func_string.split('=')[1]
        ylist = linspace(xfunc_lims[0],xfunc_lims[1],1000)
        xlist = []

        for n in range (0,len(ylist)):
            y = ylist[n]

            try:
                x = eval(func_string)
                xlist.append(y)
            except:
                print('invalid input retry:')
                run()

    plt.figure('Function_Plotter')
    plt.title('$'+fvar+' = '+func_string+'$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(xlist,ylist)
    plt.grid()
    plt.show()

run()