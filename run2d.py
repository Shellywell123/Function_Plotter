import matplotlib.pyplot as plt
from numpy import *
from library import *

def help_info():
    string = """
Function_Plotter 2D
-------------------

input function in forms,
y = f(x)
x = f(y)

limit input example
y = x**2 #0<x<1 (can only set lim on x atm)
Other Commands
exit: quits program
help: opens this page
"""

    print (string)


def run():
    """
    """
    
    fig=plt.figure('Function_Plotter')
        
    ax = fig.add_subplot(111)

    #deafult form y=..
    fvar = 'y'
    func_string_multi = input('input your function:\n')
   
    xfunc_lims = (-25,25)
    yfunc_lims = (-25,25)

    

    colours = ['red','yellow','white','blue','cyan','pink','purple','red','yellow','white','blue','cyan','pink','purple','red','yellow','white','blue','cyan','pink','purple']
    
    if func_string_multi == 'batman':
            colours = ['yellow','yellow','yellow','yellow']

    if func_string_multi == 'heart':
        colours = ['red','red']


    if func_string_multi in library_contents:
        func_string_multi = eval(func_string_multi)

    for func_string_raw in func_string_multi.split(','):
        
        color = colours[func_string_multi.split(',').index(func_string_raw)]

        if '#' in func_string_multi:
            limits = func_string_raw.split('#')[1:]  
            #print (limits)
            for lim in limits:
              #  print(lim.split('<'))

              #  if (len(lim.split('<')) != 3) or (len(lim.split('>')) != 3):
              #      print('invalid limits, retry:8')
              #      run()

                if ('<' in lim) and ( '>' in lim):
                    print('invalid limits, retry:')
                    run()

                if '<' in lim:
                    lo,var,up = lim.split('<')
                    

                if '>' in lim:
                    up,var,lo= lim.split('>')
                   # print(a)

                if var == 'x':
                    #print ('xhigh ={}, xlow={}'.format(up,lo))
                    xfunc_lims = (float(lo),float(up))

                if var == 'y':
                    yfunc_lims = (float(lo),float(up))
        #         func_string = func_string_raw.split('=')[1]
          #          x=float(up)
          #          upy = eval(func_string)
          #          x=float(lo)
          #          loy = eval(func_string)
          #          print ('yhigh ={}, ylow={}'.format(up,lo))
          #          yfunc_lims = (float(loy),float(upy))

        if func_string_raw == 'help':
            help_info()

        if func_string_raw == 'exit':
            exit(0)

        if 'z' in func_string_raw:
            print ('2D is only in x & y, retry:')
            run()

        if '=' not in func_string_raw:
            print( 'function requires "=", e.g "y=mx+c"')
            run()

        if ('y =' in func_string_raw) or ('y=' in func_string_raw):
            fvar = 'y'
            func_string = func_string_raw.split('=')[1]
            if 'i' in func_string:
                func_string = func_string.replace('i','1j')
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
            if 'i' in func_string:
                func_string = func_string.replace('i','1j')
            
            ylist = linspace(yfunc_lims[0],yfunc_lims[1],1000)
            xlist = []

            for n in range (0,len(ylist)):
                y = ylist[n]

                try:
                    x = eval(func_string)
                    xlist.append(x)
                except:
                    print('invalid input, type "help" or retry:')
                    run()

       # title_obj = plt.title('$'+func_string_raw+'$')

        plt.plot(xlist,ylist,label='$'+func_string_raw+'$',c=color)


    from MPLP import MPL_Prefs
    MPL_Prefs(fig,ax,'','grid')

    plt.show()

run()