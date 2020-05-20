import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

from numpy import *

def help_info():
    string = """
Funciton_Plotter 3D
-------------------

input function in forms,
y = f(x,z) or f(x) or f(z)
x = f(y,z) or f(y) or f(z)
z = f(x,y) or f(x) or f(y)

Other Commands
exit: quits program
help: opens this page
"""

    print (string)

def run():
    """
    """
    func_string_raw = input('input your function:\n')

    #lims preset fo now
    xfunc_lims = (-100,100)
    yfunc_lims = (-100,100)
    zfunc_lims = (-100,100)

    if func_string_raw == 'exit':
        return 0

    if func_string_raw == 'help':
        help_info()

    if '=' not in func_string_raw:
        print( 'function requires "=", e.g "y=mx+c"')
        run()

    if ('y =' in func_string_raw) or ('y=' in func_string_raw):
            fvar = 'y'
            func_string = func_string_raw.split('=')[1]
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
                    print('invalid input, type "help" or retry:')
                    run()

    if ('x =' in func_string_raw) or ('x=' in func_string_raw):
        fvar = 'x'
        func_string = func_string_raw.split('=')[1]
        ylist = linspace(yfunc_lims[0],yfunc_lims[1],1000)
        zlist = linspace(zfunc_lims[0],zfunc_lims[1],1000)
        xlist = []

        for n in range (0,len(ylist)):
            y = ylist[n]
            z = zlist[n]

            try:
                x = eval(func_string)
                xlist.append(x)
            except:
                print('invalid input, type "help" or retry:')
                run()

    if ('z =' in func_string_raw) or ('z=' in func_string_raw):
        fvar = 'z'
        func_string = func_string_raw.split('=')[1]
        ylist = linspace(yfunc_lims[0],yfunc_lims[1],1000)
        xlist = linspace(xfunc_lims[0],xfunc_lims[1],1000)
        zlist = []

        for n in range (0,len(ylist)):
            x = xlist[n]
            y = ylist[n]

            try:
                z = eval(func_string)
                zlist.append(z)
            except:
                print('invalid input, type "help" or retry:')
                run()

    fig = plt.figure('Function_Plotter')
    ax = fig.add_subplot(111, projection='3d')
    plt.title('$'+func_string_raw+'$')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')

    if 'x' not in func_string_raw:
            xlist = list(zeros(len(xlist)))

    if 'y' not in func_string_raw:
            ylist = list(zeros(len(ylist)))

    if 'z' not in func_string_raw:
            zlist = list(zeros(len(zlist)))

    ax.plot(xlist,ylist,zlist)
    plt.show()

run()