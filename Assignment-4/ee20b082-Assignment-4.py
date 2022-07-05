import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.linalg import lstsq

num=3
def exp(x):
    return np.exp(x)
def coscos(x):
    return np.cos(np.cos(x))
def u(x,f,k):
    return f(x)*np.cos(k*x)
def v(x,f,k):
    return f(x)*np.sin(k*x)
def coefficients_vs_n(func,name):
    global num
    n=[i for i in range(51)]
    a=np.zeros(51,dtype=float)
    a[0]=integrate.quad(func,0,2*np.pi)[0]/(2*np.pi)
    for i in range(1,50,2):
        a[i]=integrate.quad(u,0,2*np.pi,args=(func,(i//2)+1))[0]/np.pi
        a[i+1]=integrate.quad(v,0,2*np.pi,args=(func,(i//2)+1))[0]/np.pi
    plt.semilogy(n,np.abs(a),'ro')
    plt.xlabel(r'n$\rightarrow$')
    plt.ylabel(r'Magnitude of coefficients $\rightarrow$')
    plt.title('semilogy plot for magnitude of the coefficients of {} vs n'.format(name))
    plt.legend()
    plt.savefig('Figure{}.png'.format(num))
    plt.grid()
    plt.show()
    num=num+1
    plt.loglog(n,np.abs(a),'ro')
    plt.xlabel(r'n$\rightarrow$')
    plt.ylabel(r'Magnitude of coefficients $\rightarrow$')
    plt.title('loglog plot for magnitude of the coefficients of {} vs n'.format(name))
    plt.legend()
    plt.savefig('Figure{}.png'.format(num))
    plt.grid()
    plt.show()
    num=num+1
    return a
def least_squares_approach(func,a,name):
    global num
    n=[i for i in range(51)]
    A=np.zeros((400,51))
    A[:,0]=1
    xi=np.linspace(0,2*np.pi,401)
    xi=xi[:-1]
    b= func(xi)
    for k in range(1,26):
        A[:,2*k-1]=np.cos(k*xi)
        A[:,2*k]=np.sin(k*xi)
    c=np.linalg.lstsq(A,b,rcond = None)[0]
    plt.semilogy(n,np.abs(c),'go',label='Least squares approach')
    plt.semilogy(n,np.abs(a),'ro',label='Fourier series approach')
    plt.xlabel(r'n$\rightarrow$')
    plt.ylabel(r'Magnitude of coefficients$\rightarrow$')
    plt.title('semilogy plot for magnitude of the coefficients of {} vs n'.format(name))
    plt.legend()
    plt.savefig('Figure{}.png'.format(num))
    plt.grid()
    plt.show()
    num=num+1
    plt.loglog(n,np.abs(c),'go',label='Least squares approach')
    plt.semilogy(n,np.abs(a),'ro',label='Fourier series approach')
    plt.xlabel(r'n$\rightarrow$')
    plt.ylabel(r'Magnitude of coefficients$\rightarrow$')
    plt.title('loglog plot for magnitude of the coefficients {} vs n'.format(name))
    plt.legend()
    plt.savefig('Figure{}.png'.format(num))
    plt.grid()
    plt.show()
    num=num+1
    return c,A
def compare(a,c1,name):
    global num
    deviation=abs(a-c1)
    n=[i for i in range(51)]
    coloumn=np.argmax(deviation)
    plt.plot(n,deviation,'ro')
    plt.plot(coloumn,deviation[coloumn],'dg',label=r"maximum deviation at %d= %f"%(coloumn,deviation[coloumn]))
    plt.xlabel(r'n$\rightarrow$')
    plt.ylabel(r'Deviation$\rightarrow$')
    plt.title('Deviation between least squares approach and direct integration({})'.format(name))
    plt.legend()
    plt.savefig('Figure{}.png'.format(num))
    plt.show()
    num+=1
x=np.linspace(-2*np.pi,4*np.pi,500)
plt.semilogy(x,exp(x))
plt.grid(True)
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'$e^{x}\rightarrow$')
plt.title('semilogy plot of $e^{x}$')
plt.savefig('Figure1.png')
plt.legend()
plt.show()
plt.plot(x,coscos(x))
plt.grid()
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'$\cos(\cos(x))\rightarrow$')
plt.title('Plot of $\cos(\cos(x))$')
plt.legend()
plt.savefig('Figure2.png')
plt.show()

a1=coefficients_vs_n(exp,name='$e^x$')
a2=coefficients_vs_n(coscos,name='$\cos(\cos(x))$')
c1,A=least_squares_approach(exp,a1,name='$e^x$')
c2,B=least_squares_approach(coscos,a2,name='$\cos(\cos(x))$')
compare(a1,c1,name='$e^x$')
compare(a2,c2,name='$\cos(\cos(x))$')

x1 = np.linspace(0,2*np.pi,401)
x1=x1[:-1]

b1=np.matmul(A,c1)
plt.semilogy(x1,b1,'go',label='estimated')
plt.semilogy(x1,exp(x1),label='True function')
plt.grid()
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'$e^{x}\rightarrow$')
plt.title('semilogy plot of estimated $e^{x}$ and it\'s estimated function.')
plt.legend()
plt.savefig('Figure{}.png'.format(num))
plt.show()
num+=1

b2=np.matmul(B,c2)
plt.plot(x1,b2,'go',label='estimated')
plt.plot(x1,coscos(x1),label='True function')
plt.grid()
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'$\cos(\cos(x))\rightarrow$')
plt.title('plot of $\cos(\cos(x))$ and it\'s estimated function.')
plt.legend()
plt.savefig('Figure{}.png'.format(num))
plt.show()
num+=1