
#LIBRARY OF FUNCTIONS

#ALPHABET
A = ""
B = "x = sqrt((6-((y-3.85)*3/2)**2)*2/3)+1.25 #2.6<y<5,x = sqrt(2/3*(6-((y-1.2)*3/2)**2))+1.5 #0<y<2.6, y=0 #0<x<2.82, y=5 #0<x<2.65, x=0 #0<y<5, x=1 #1<y<2,x=1 #3<y<4, x=2 #1<y<2,x=2 #3<y<4, y=4 #1<x<2,y=3 #1<x<2   ,y=2 #1<x<2   ,y=1 #1<x<2"
C = ""
D = ""
E = "y=5 #0<x<4, y=4 #1<x<4, y=3 #1<x<3, y=2 #1<x<3, y=1 #1<x<4, y=0 #0<x<4, x=0 #0<y<5, x=1 #3<y<4, x=1 #1<y<2, x=3 #2<y<3, x=4 #4<y<5, x=4 #0<y<1"
F = ""
G = ""
H = ""
I = ""
J = ""
K = ""
L = ""
M = ""
N = ""
O = ""
P = ""
Q = ""
R = ""
S = ""
T = ""
V = ""
W = ""
X = ""
Y = ""
Z = ""

letters = ['B','E']

#LOGOS
batman = "y=1.5*sqrt((-abs(abs(x) - 1)) * abs(3 - abs(x))/((abs(x) - 1)*(3 - abs(x)))) * (1+abs(abs(x) - 3)/(abs(x)- 3)) * sqrt(1 - (x/7)**2)+(4.5+0.75 * (abs(x - 0.5)+abs(x+0.5)) - 2.75 * (abs(x-0.75)+abs(x+0.75))) * (1+abs(1 - abs(x))/(1 - abs(x))),y = (-3)*sqrt(1 -(x/7)**2) * sqrt(abs(abs(x) - 4)/(abs(x)-4)),y = abs(x/2) - 0.0913722 * x**2-3+sqrt(1 - (abs(abs(x) - 2) - 1)**2),y = (2.71052+1.5 - 0.5 * abs(x) - 1.35526 * sqrt(4 - (abs(x) - 1)**2)) * sqrt(abs(abs(x) - 1)/(abs(x) - 1))"
heart  = "y = sqrt(1 -(abs(x)-1)**2) #-2<x<2, y=-3*sqrt(1-(sqrt(abs(x)/2))) #-2<x<2"

logos = ['batman','heart']

library_contents = letters + logos