import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from MPLP import *
from library import *

def help_info():
    string = """
Function_Plotter 3D
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
    
    func_string_multi = input('input your function:\n')
    
            
    if func_string_multi == 'exit':
        exit(0)
        
    if func_string_multi == 'help':
        help_info()


    fig = plt.figure('Function_Plotter',figsize=[7,5])
    ax = fig.add_subplot(111, projection='3d')

    colours = ['red','yellow','white','blue','cyan','pink','purple','red','yellow','white','blue','cyan','pink','purple','red','yellow','white','blue','cyan','pink','purple']

    if func_string_multi == 'batman':
            colours = ['yellow','yellow','yellow','yellow']

    if func_string_multi == 'heart':
            colours = ['red','red']

    if func_string_multi in library_contents:
        func_string_multi = eval(func_string_multi)


    for func_string_raw in func_string_multi.split(','):
        color = colours[func_string_multi.split(',').index(func_string_raw)]

        #lims preset fo now
        xfunc_lims = (-100,100)
        yfunc_lims = (-100,100)
        zfunc_lims = (-100,100)

        if '=' not in func_string_raw:
            print( 'function requires "=", e.g "y=mx+c"')
            run()

        if ('y =' in func_string_raw) or ('y=' in func_string_raw):
                fvar = 'y'
                func_string = func_string_raw.split('=')[1]
                func_string = alias_check(func_string)
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
            func_string = alias_check(func_string)
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
            func_string = alias_check(func_string)
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

        
       # title_obj = plt.title('$'+func_string_raw+'$')

        if 'x' not in func_string_raw:
                xlist = list(zeros(len(xlist)))

        if 'y' not in func_string_raw:
                ylist = list(zeros(len(ylist)))

        if 'z' not in func_string_raw:
                zlist = list(zeros(len(zlist)))

        legend_label = legend_labeller(func_string_raw)
        ax.plot(xlist,ylist,zlist,label=legend_label,c=color)

    
    MPL_Prefs(fig,ax,'','grid')

    plt.show()

run()