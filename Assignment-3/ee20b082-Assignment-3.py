import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy.special as sp
from scipy.linalg import lstsq
def graphs(n1):
    if(n1==4):
        for j in range(0,k):
            plt.plot(time,yy[:,j],label=r'$\sigma$=%.3f'%sigma[j])
        plt.plot(time,g(time,1.05,-0.105),label="True value")
        plt.title("Data to be fitted to theory")
        plt.ylabel(r'f(t)+noise$\rightarrow$')
        plt.xlabel(r't$\rightarrow$')
        plt.legend(loc="upper right")
        plt.savefig('question-4.png')
        plt.show()
    if(n1==5):
        for i in range(0,N,5):
            plt.errorbar(time[i],yy[i][0],yerr=sigma[0],fmt="ro")
        plt.plot(time,g(time,1.05,-0.105),label="True value")
        plt.title("Data points for 0.10 along with exact function")
        plt.xlabel(r't$\rightarrow$')
        plt.legend(loc="upper right")
        plt.savefig('question-5.png')
        plt.show()
    if(n1==6):
        if(np.array_equal(np.dot(M,[[1.05],[-0.105]]),g(time,1.05,-0.105))):
            print("Equal")
        else:
            print("Not Equal")
    if(n1==8):
        e=np.zeros((21,21),dtype=float)
        A=np.linspace(0,2,21)
        B=np.linspace(-0.2,0,21)
        x=yy[:,0]
        for i in range(21):
            for j in range(21):
                for m in range(101):
                    e[i][j]+=(x[m]-g(time[m],A[i],B[j]))**2
                e[i][j]=e[i][j]/101
        plt.contour(A,B,e,21)
        plt.clabel(plt.contour(A,B,e,21),inline=1)
        plt.title(r"Contour plot of $\epsilon_{ij}$")
        plt.ylabel(r'B$\rightarrow$')
        plt.xlabel(r'A$\rightarrow$')
        min=np.argmin(e)
        if(min):
            print("There is a minimum")
        r=min//21
        c=min%21
        plt.plot(A[r],B[c],'dr',label=r"minimum at %.2f,%.2f"%(A[r],B[c]))
        plt.legend(loc="upper right")
        plt.savefig('question-8.png')
        plt.show()
    estimate=[]
    solution=[]
    for i in range(9):
        p,resid,rank,sig=lstsq(M,yy[:,i])
        estimate.append(p)
        solution.append(rank)
    estimate=np.array(estimate)
    error_in_estimate_A=abs(estimate[:,0]-1.05)
    error_in_estimate_B=abs(estimate[:,1]+0.105)
    if(n1==10 and all(solution)):
        plt.plot(sigma,error_in_estimate_A,'--ro',label='Aerr')
        plt.plot(sigma,error_in_estimate_B,'--bo',label='Berr')
        plt.title("Variation of error with noise")
        plt.ylabel(r'MS Error$\rightarrow$')
        plt.xlabel(r'Noise standard deviation$\rightarrow$')
        plt.legend(loc='upper right')
        plt.savefig('question-10.png')
        plt.show()
    if(n1==11 and all(solution)==True):
        plt.loglog(sigma,error_in_estimate_A,'bo',label='Aerr')
        plt.loglog(sigma,error_in_estimate_B,'ro',label='Berr')
        plt.title("Variation of error with noise")
        plt.ylabel(r'MS Error$\rightarrow$')
        plt.xlabel(r'$\sigma_{n}\rightarrow$')
        plt.legend(loc='upper left')
        plt.savefig('question-11.png')
        plt.show()

def g(t,a,b):
    return a*sp.jn(2,t)+b*t
N=101
k=9
data=np.loadtxt("fitting.dat",dtype=float)
time=np.array(data[:,0])
yy=np.array(data[:,1:])
y0=g(time,1.05,-0.105)
sigma=np.logspace(-1,-3,9)
M=np.c_[sp.jn(2,time),time]
print("Enter question number for which you need graph(Enter one of this values 4,5,6,8,10,10):")
question_number=int(input())
graphs(question_number)