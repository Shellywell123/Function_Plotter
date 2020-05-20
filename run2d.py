import matplotlib.pyplot as plt
from numpy import *

def help_info():
    string = """
Funciton_Plotter 2D
-------------------

input function in forms,
y = f(x)
x = f(y)

Other Commands
exit: quits program
help: opens this page
"""

    print (string)

def run():
    """
    """
    
    #deafult form y=..
    fvar = 'y'
    func_string_raw = input('input your function:\n')

    #lims preset for now
    xfunc_lims = (-100,100)

    if func_string_raw == 'help':
        help_info()

    if func_string_raw == 'exit':
        return 0

    if 'z' in func_string_raw:
        print ('2D is only in x & y, retry:')
        run()

    if '=' not in func_string_raw:
        print( 'function requires "=", e.g "y=mx+c"')
        run()

    if ('y =' in func_string_raw) or ('y=' in func_string_raw):
        fvar = 'y'
        func_string = func_string_raw.split('=')[1]
        xlist = linspace(xfunc_lims[0],xfunc_lims[1],1000)
        ylist = []

        for n in range (0,len(xlist)):
            x = xlist[n]

            try:
                y = eval(func_string)
                ylist.append(y)
            except:
                print('invalid input, type "help" or retry:')
                run()

    if ('x =' in func_string_raw) or ('x=' in func_string_raw):
        fvar = 'x'
        func_string = func_string_raw.split('=')[1]
        ylist = linspace(xfunc_lims[0],xfunc_lims[1],1000)
        xlist = []

        for n in range (0,len(ylist)):
            y = ylist[n]

            try:
                x = eval(func_string)
                xlist.append(y)
            except:
                print('invalid input, type "help" or retry:')
                run()

    plt.figure('Function_Plotter')
    plt.title('$'+func_string_raw+'$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(xlist,ylist)
    plt.grid()
    plt.show()

run()