
#LIBRARY OF FUNCTIONS AND INPUT ALIAS

#ALPHABET
A=""
B="x=sqrt((6-((y-3.85)3/2)^2)2/3)+1.25#2.6<y<5,x=sqrt(2/3(6-((y-1.2)3/2)^2))+1.5#0<y<2.6,y=0#0<x<2.82,y=5#0<x<2.65,x=0#0<y<5,x=1#1<y<2,x=1#3<y<4,x=2#1<y<2,x=2#3<y<4,y=4#1<x<2,y=3#1<x<2,y=2#1<x<2,y=1#1<x<2"
C=""
D=""
E="y=5#0<x<4,y=4#1<x<4,y=3#1<x<3,y=2#1<x<3,y=1#1<x<4,y=0#0<x<4,x=0#0<y<5,x=1#3<y<4,x=1#1<y<2,x=3#2<y<3,x=4#4<y<5,x=4#0<y<1"
F=""
G=""
H=""
I=""
J=""
K=""
L=""
M=""
N=""
O=""
P=""
Q=""
R=""
S=""
T=""
V=""
W=""
X=""
Y=""
Z=""

letters = ['B','E']

#LOGOS
batman="y=1.5sqrt((-abs(abs(x)-1))abs(3-abs(x))/((abs(x)-1)(3-abs(x))))(1+abs(abs(x)-3)/(abs(x)-3))sqrt(1-(x/7)^2)+(4.5+0.75(abs(x-0.5)+abs(x+0.5))-2.75(abs(x-0.75)+abs(x+0.75)))(1+abs(1-abs(x))/(1-abs(x))),y=(-3)sqrt(1-(x/7)^2)sqrt(abs(abs(x)-4)/(abs(x)-4)),y=abs(x/2)-0.0913722x^2-3+sqrt(1-(abs(abs(x)-2)-1)^2),y=(2.71052+1.5-0.5abs(x)-1.35526sqrt(4-(abs(x)-1)^2))sqrt(abs(abs(x)-1)/(abs(x)-1))"
heart="y=sqrt(1-(abs(x)-1)^2)#-2<x<2,y=-3sqrt(1-(sqrt(abs(x)/2)))#-2<x<2"

logos = ['batman','heart']

library_contents = letters + logos

def alias_check(func_string):
    """allows user to put alias command, can defo smarten"""

    mult_checks = [')(',
                    '0(','1(','2(','3(','4(','5(','6(','7(','8(','9(',
                    ')0',')1',')2',')3',')4',')5',')6',')7',')8',')9',
                    ')a',')c',')s',
                    '0a','1a','2a','3a','4a','5a','6a','7a','8a','9a'
                    '0c','1c','2c','3c','4c','5c','6c','7c','8c','9c',
                    '0e','1e','2e','3e','4e','5e','6e','7e','8e','9e',
                    '0i','1i','2i','3i','4i','5i','6i','7i','8i','9i',
                    '0s','1s','2s','3s','4s','5s','6s','7s','8s','9s',
                    '0x','1x','2x','3x','4x','5x','6x','7x','8x','9x',
                    '0y','1y','2y','3y','4y','5y','6y','7y','8y','9y',
                    '0z','1z','2z','3z','4z','5z','6z','7z','8z','9z']
    for check in mult_checks:
        if check in func_string:
            func_string = func_string.replace(check,check[0]+'*'+check[1])

    power_checks = ['^']
    for check in power_checks:
        if check in func_string:
            func_string = func_string.replace(check,'**')

    comp_checks = [' i','i ','+i','i+','*i','i*','/i','i/','-i','i-']
    for check in comp_checks:
        if check in func_string:
            func_string = func_string.replace(check,'1j')

    



    return func_string