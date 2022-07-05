import numpy as np 
from sympy import *
import scipy.signal as sp 
init_session
import matplotlib.pyplot as plt

def filters(R1,R2,C1,C2,G,Vi,c):
    if(c=='l'):
        s=symbols('s')
        A=Matrix([[0,0,1,-1/G],[-1/(1+s*R2*C2),1,0,0],[0,-G,G,1],[-1/R1-1/R2-s*C1,1/R2,0,s*C1]])
        b=Matrix([0,0,0,-Vi/R1])
        V = A.inv()*b
        return (A,b,V)
    if(c=='h'):
        s=symbols('s')
        A=Matrix([[0,0,1,-1/G],[-(s*R2*C2)/(1+s*R2*C2),1,0,0], [0,-G,G,1],[-(s*C1)-(s*C2)-(1/R1),s*C2,0,1/R1]])
        b=Matrix([0,0,0,-Vi*s*C1])
        V=A.inv()*b
        return (A,b,V)

s = symbols('s')
A,b,V=filters(10000,10000,1e-9,1e-9,1.586,1,'l')
Vo = V[3]
ww=np.logspace(0,8,801)
ss=1j*ww
hf=lambdify(s,Vo,'numpy')
v=hf(ss)
ph=np.angle(v)
plt.subplot(1,2,1)
plt.loglog(ww,abs(v),lw=2)
plt.title('Magnitude Plot for lowpass filter')
plt.xlabel('Frequency')
plt.ylabel('Magnitude in log scale')
plt.grid(True)
plt.subplot(1,2,1)
plt.semilogx(ww,np.angle(v),lw=2)
plt.title('Phase Plot for lowpass filter')
plt.xlabel('Frequency in log scale')
plt.ylabel('Phase in radians')
plt.grid(True)
plt.show()


poll=simplify(Vo).as_numer_denom()
num=poll[0]
den=poll[1]
isFloat = False
num = Poly(num).all_coeffs()      
den = Poly(den).all_coeffs()          
den2 = []
num2 = []
for i in den:
    den2.append(float(i))
den2 = np.array(den2)
for i in num:
    num2.append(float(i))
num2 = np.array(num2)
num=np.poly1d(num2)
den=np.poly1d(den2)
H1=sp.lti(num,den)
t = np.linspace(0,0.001,10000)
Vo = sp.step(H1,None,t)
plt.plot(Vo[0],Vo[1])
plt.title('Time domain output to step input')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()

Vi=1/s
A,b,V=filters(10000,10000,1e-9,1e-9,1.586,Vi,'l')
Vo = V[3]
ww=np.logspace(0,8,801)
ss=1j*ww
hf=lambdify(s,Vo,'numpy')
v=hf(ss)
ph=np.angle(v)
plt.loglog(ww,abs(v),lw=2)
plt.title('Step Response of the low pass filter')
plt.xlabel('Frequency in log scale')
plt.ylabel('Magnitude in log scale')
plt.grid(True)
plt.show()

t = np.linspace(0.0,4e-3,100001)     
x = np.sin(2000*np.pi*t) + np.cos(2*(10**6)*np.pi*t)   
t,y,svec = sp.lsim(H1,x,t)  

plt.subplot(1, 2,1)
plt.plot(t,y)
plt.grid()
plt.title('Output of lowpass filter to given input')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.subplot(1, 2,2)
plt.plot(t,x)
plt.grid()
plt.title('Input to lowpass filter')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.show()

s = symbols('s')
A,b,V=filters(10000,10000,1e-9,1e-9,1.586,1,'h')
Vo = V[3]
ww=np.logspace(0,8,801)
ss=1j*ww
hf=lambdify(s,Vo,'numpy')
v=hf(ss)
ph=np.angle(v)
plt.loglog(ww,abs(v),lw=2)
plt.title('Magnitude Plot for highpass filter')
plt.xlabel('Frequency')
plt.ylabel('Magnitude in log scale')
plt.grid(True)
plt.show()
plt.semilogx(ww,np.angle(v),lw=2)
plt.title('Phase Plot for highpass filter')
plt.xlabel('Frequency in log scale')
plt.ylabel('Phase in radians')
plt.grid(True)
plt.show()

poll=simplify(Vo).as_numer_denom()
num=poll[0]
den=poll[1]
isFloat = False
num = Poly(num).all_coeffs()      
den = Poly(den).all_coeffs()          
den2 = []
num2 = []
for i in den:
    den2.append(float(i))
den2 = np.array(den2)  
for i in num:
    num2.append(float(i))
num2 = np.array(num2)
num=np.poly1d(num2)
den=np.poly1d(den2)
H2=sp.lti(num,den)
t = np.linspace(0,0.001,10000)
Vo = sp.step(H2,None,t)
plt.plot(Vo[0],Vo[1])
plt.title('Time domain output to step input')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()
Vi=1/s
A,b,V=filters(10000,10000,1e-9,1e-9,1.586,Vi,'h')
Vo = V[3]
ww=np.logspace(0,8,801)
ss=1j*ww
hf=lambdify(s,Vo,'numpy')
v=hf(ss)
ph=np.angle(v)
plt.loglog(ww,abs(v),lw=2)
plt.grid(True)
plt.title('Step Response of the high pass filter')
plt.xlabel('Frequency in log scale')
plt.ylabel('Magnitude in log scale')
plt.show()

t = np.linspace(0.0,4e-3,100001)     
x = np.sin(2000*np.pi*t) + np.cos(2*(10**6)*np.pi*t)   
t,y,svec = sp.lsim(H2,x,t)  

plt.subplot(1, 2, 1)
plt.plot(t,y)
plt.grid()
plt.title('Output of highpass filter to given input')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.subplot(1, 2, 2)
plt.plot(t,x)
plt.grid()
plt.title('Input to highpass filter')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.show()

t = np.linspace(0.0,1,100000)     
x = (np.cos((10**4)*np.pi*t))*np.exp((-5)*t)
t,y,svec = sp.lsim(H2,x,t)   

plt.subplot(1, 2, 1)
plt.plot(t,y)
plt.grid()
plt.title('Output of highpass filter to given input')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.subplot(1, 2, 2)
plt.plot(t,x)
plt.grid()
plt.title('Input to highpass filter')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.show()