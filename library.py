
#LIBRARY OF FUNCTIONS AND INPUT ALIAS

#ALPHABET
A=""
B="x=sqrt((6-((y-3.85)3/2)^2)2/3)+1.25#2.6<y<5,x=sqrt(2/3(6-((y-1.2)3/2)^2))+1.5#0<y<2.6,y=0#0<x<2.82,y=5#0<x<2.65,x=0#0<y<5,x=1#1<y<2,x=1#3<y<4,x=2#1<y<2,x=2#3<y<4,y=4#1<x<2,y=3#1<x<2,y=2#1<x<2,y=1#1<x<2"
C="x=0#0<y<5,x=1#1<y<4,x=4#0<y<1,x=4#4<y<5,y=5#0<x<4,y=4#1<x<4,y=1#<1x<4,y=0#0<x<4"
D=""
E="y=5#0<x<4,y=4#1<x<4,y=3#1<x<3,y=2#1<x<3,y=1#1<x<4,y=0#0<x<4,x=0#0<y<5,x=1#3<y<4,x=1#1<y<2,x=3#2<y<3,x=4#4<y<5,x=4#0<y<1"
F="y=5#0<x<4,y=4#1<x<4,y=3#1<x<3,y=2#1<x<3,y=0#0<x<1,x=0#0<y<5,x=1#03<y<4,x=1#0<y<2,x=3#2<y<3,x=4#4<y<5"
G=""
H="y=5#0<x<1,y=5#3<x<4,y=3#1<x<3,y=2#1<x<3,y=0#0<x<1,y=0#3<x<4,x=0#0<y<5,x=1#3<y<5,x=1#0<y<2,x=3#3<y<5,x=3#0<y<2,x=4#0<y<5"
I=""
J=""
K=""
L="y=0#0<x<4,y=1#1<x<4,x=0#0<y<5,y=5#0<x<1,x=4#0<y<1,x=1#1<y<5"
M=""
N="y=5#0<x<1,y=5#3<x<4,y=0#3<x<4,y=0#0<x<1,x=0#0<y<5,x=4#0<y<5,x=1#0<y<4,x=3#1<y<5,y=-(2)x+7#1<x<3,y=-(2)x+6#1<x<3"
O=""
P=""
Q=""
R=""
S=""
T="y=5#0<x<4,y=4#0<x<1.5,y=4#2.5<x<4,x=1.5#0<y<4,x=2.5#0<y<4,y=0#1.5<x<2.5,x=0#4<y<5,x=4#4<y<5"
V=""
W=""
X=""
Y=""
Z="y=0#0<x<4,y=5#0<x<4,y=1#1<x<4,y=4#0<x<3,x=0#0<y<1,x=0#4<y<5,x=4#0<y<1,x=4#4<y<5,y=x+1#0<x<3,y=x#1<x<4"

letters = ['B','C','E','F','H','L','N','T','Z']

# # # # # # # # # # #

#LOGOS
batman="y=1.5sqrt((-abs(abs(x)-1))abs(3-abs(x))/((abs(x)-1)(3-abs(x))))(1+abs(abs(x)-3)/(abs(x)-3))sqrt(1-(x/7)^2)+(4.5+0.75(abs(x-0.5)+abs(x+0.5))-2.75(abs(x-0.75)+abs(x+0.75)))(1+abs(1-abs(x))/(1-abs(x))),y=(-3)sqrt(1-(x/7)^2)sqrt(abs(abs(x)-4)/(abs(x)-4)),y=abs(x/2)-0.0913722x^2-3+sqrt(1-(abs(abs(x)-2)-1)^2),y=(2.71052+1.5-0.5abs(x)-1.35526sqrt(4-(abs(x)-1)^2))sqrt(abs(abs(x)-1)/(abs(x)-1))"
heart="y=sqrt(1-(abs(x)-1)^2)#-2<x<2,y=-3sqrt(1-(sqrt(abs(x)/2)))#-2<x<2"

logos = ['batman','heart']

# # # # # # # # # # #

def md_lib_updater(letters,logos):
    """ auto update for markdown"""
    letterstr = '`' + "`, `".join(letters) + '`'
    logostr   = '`' + "`, `".join(logos) + '`'

    file = 'README.md'

    with open(file, 'r') as f:
       cont = f.read()
      # print(cont)

    newcont = ''
    for line in cont.split('\n'):
        if "    - Letters: " in line:
            line =  "    - Letters: {}".format(letterstr)
        if "    - Logos:   " in line:
            line = "    - Logos:   {}".format(logostr)
       # print(line)
        newcont = newcont+line+'\n'

    with open(file, 'w') as f:
        f.write(newcont)

md_lib_updater(letters,logos)

library_contents = letters + logos

def alias_check(func_string):
    """allows user to put alias command, can defo smarten"""

    #################################
    mult_checks = [')(',
                    '0(','1(','2(','3(','4(','5(','6(','7(','8(','9(',
                    ')0',')1',')2',')3',')4',')5',')6',')7',')8',')9',
                    ')a',')c',')s']

    import string
    for letter in list(string.ascii_lowercase):
        mult_checks.append('0'+letter)
        mult_checks.append('1'+letter)
        mult_checks.append('2'+letter)
        mult_checks.append('3'+letter)
        mult_checks.append('4'+letter)
        mult_checks.append('5'+letter)
        mult_checks.append('6'+letter)
        mult_checks.append('7'+letter)
        mult_checks.append('8'+letter)
        mult_checks.append('9'+letter)
        mult_checks.append(')'+letter)

    for check in mult_checks:
        if check in func_string:
            func_string = func_string.replace(check,check[0]+'*'+check[1])

    #################################
    # currently breaks batman funciton?
   # neg_checks = []
   # for letter in list(string.ascii_lowercase):
   #     neg_checks.append('-'+letter)

  #  for check in neg_checks:
  #      if check in func_string:
  #          func_string = func_string.replace(check,check[0]+'-1*'+check[1])

    #################################
    power_checks = ['^']
    for check in power_checks:
        if check in func_string:
            func_string = func_string.replace(check,'**')

    #################################
    comp_checks = [' i','i ','+i','i+','*i','i*','/i','i/','-i','i-']
    for check in comp_checks:
        if check in func_string:
            func_string = func_string.replace(check,'1j')

    return func_string