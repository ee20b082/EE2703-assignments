from turtle import color
import numpy as np 
import sys
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from scipy.linalg import lstsq
def max_error(A,B,N):
    return -A*(np.exp(B*(N+0.5)))/B
try:
    Nx=int(sys.argv[1])
    Ny=int(sys.argv[2])
    radius=int(sys.argv[3])
    Niter=int(sys.argv[4])
except:
    Nx=25
    Ny=25
    radius=8
    Niter=1500
phi=np.zeros((Ny,Nx),dtype=float)
y = np.linspace(-(Ny-1)/2,(Ny-1)/2,Ny)
x = np.linspace(-(Nx-1)/2,(Nx-1)/2,Nx)
Y,X = np.meshgrid(y,x)
phi[np.where((X*X+Y*Y)<=64)]=1.0
ii = np.where((X**2 + Y**2) <= ((radius)**2))
plt.contour(Y,X,phi)
plt.plot(ii[1]-(Nx-1)/2,ii[0]-(Ny-1)/2,'ro',label='V=1 nodes')
plt.xlabel(r'x$\rightarrow$',fontsize=15)
plt.ylabel(r'y$\rightarrow$',fontsize=15)
plt.title('contour plot of the potential')
plt.legend()
plt.savefig('fig1.png')
plt.show()


err = np.zeros(Niter)
for k in range(Niter):
    oldphi=phi.copy()
    phi[1:-1,1:-1]=0.25*(oldphi[1:-1,0:-2]+ oldphi[1:-1,2:]+ oldphi[0:-2,1:-1] + oldphi[2:,1:-1])
    phi[:,0]=phi[:,1]
    phi[:,Nx-1]=phi[:,Nx-2] 
    phi[0,:]=phi[1,:] 
    phi[np.where((X*X+Y*Y)<=64)]=1.0
    err[k]=(abs(phi-oldphi)).max()
Niterarr=[i for i in range(Niter)]
plt.semilogy(Niterarr,err,'ro',label='Whole error curve')
plt.semilogy(Niterarr[::50],err[::50],'go',label="every 50th error point")
plt.xlabel("No of iterations")
plt.ylabel("Error")
plt.title("Plot of Error vs Iterations.(semilog plot)")
plt.legend()
plt.savefig('fig2.png')
plt.show()


plt.loglog(Niterarr,err,'ro',label='Whole error curve')
plt.loglog(Niterarr[::50],err[::50],'go',label="every 50th error point")
plt.xlabel("No of iterations")
plt.ylabel("Error")
plt.title("Plot of Error vs Iterations.(loglog plot)")
plt.legend()
plt.savefig('fig3.png')
plt.show()


c1=np.ones(Niter)
c2=Niterarr
C=np.c_[c1,c2]
y=np.log(err)
a,B=lstsq(C,y)[0]
A=np.exp(a)
fit_arr=A*np.exp(B*range(Niter))
plt.semilogy(Niterarr,err,'ro',label='errors')
plt.semilogy(Niterarr[:500],fit_arr[:500],'go',label='fit1')
plt.semilogy(Niterarr[500:],fit_arr[500:],'bo',label='fit2')
plt.title("Best fit for error on a semilog scale")
plt.xlabel("No of iterations")
plt.ylabel("Error")
plt.grid(True)
plt.legend()
plt.savefig('fig4.png')
plt.show()


plt.semilogy(Niterarr[::50],err[::50],'ro',label='errors')
plt.semilogy(Niterarr[:500:50],fit_arr[:500:50],'go',label='fit1')
plt.semilogy(Niterarr[500::50],fit_arr[500::50],'bo',label='fit2')
plt.grid(True)
plt.title("Best fit for error on a semilog scale(Every 50th iteration)")
plt.xlabel("No of iterations")
plt.ylabel("Error")
plt.legend()
plt.savefig('fig5.png')
plt.show()

plt.semilogy(range(Niter)[::50],max_error(A,B,np.arange(Niter))[::50],'ro',markersize=3)
plt.title('Plot of maximum Error values On a semilog scale')
plt.xlabel("iterations")
plt.ylabel("maximum error")
plt.savefig('fig6.png')
plt.show()

fig4=plt.figure(0)
ax=p3.Axes3D(fig4) # Axes3D is the means to do a surface plot
plt.title('The 3-D plot of potential')
surf = ax.plot_surface(Y, X, phi.T, rstride=1, cstride=1, cmap=plt.cm.jet)
plt.savefig('fig7.png')
plt.show()

plt.contour(Y,X,phi)
plt.plot(ii[1]-(Nx-1)/2,ii[0]-(Ny-1)/2,'ro',label='V=1 nodes')
plt.xlabel(r'x$\rightarrow$',fontsize=15)
plt.ylabel(r'y$\rightarrow$',fontsize=15)
plt.title('contour plot of the potential')
plt.legend()
plt.savefig('fig8.png')
plt.show()

Jx = np.zeros((Ny,Nx))
Jy = np.zeros((Ny,Nx))
Jx[0:,1:-1]=0.5*(phi[0:,0:-2]-phi[0:,2:])
Jy[1:-1,0:]=0.5*(phi[0:-2,0:]-phi[2:,0:])
plt.quiver(range(Nx),range(Ny),-Jx[::-1,:],-Jy[::-1,:])
plt.plot(ii[1],ii[0],'ro')
plt.title("The vector plot of the current flow")
plt.xlabel(r"x$\rightarrow$")
plt.ylabel(r'y$\rightarrow$')
plt.savefig('fig9.png')
plt.show()