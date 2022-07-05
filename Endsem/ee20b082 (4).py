from cmath import pi
import numpy as np
from matplotlib.pylab import *

#Given conditions
l=0.5
c=2.9979e8
mu0=4e-7*pi
Im=1.0
a=0.01
lamda=l*4.0
f=c/lamda
k=2*pi/lamda
N=100

#Q1
#creating z,u arrays based on given conditions
dz=l/N
z=np.zeros(2*N+1)
i=np.arange(2*N+1)
z=(i-N)*dz
u = delete(z,[0,N,2*N])#delete will remove the elements in list mentioned after the list
print("Array z=",z)
print("Array u=",u)


#Q2-creating matrix
def Matrix(N,a):
    M = (1/(2*pi*a))*identity(2*N -2)
    return M
J = np.zeros(2*N-2) # current vector at points corresponding to vector u.
H_phi=Matrix(N,a)*J


#Q3
#calculating Ru,Rz,P_B,P,Q,Q_B

#computing and creating Rz,Ru vectors.
#using meshgrid to neglect usage of loops. for Rz,Ru we need differece between to positions which can be done by using loops and also by meshgrid.
#Here both Rz,Ru are vectors.
zx, zy = meshgrid(z, z)
Rz = sqrt((zx - zy) ** 2 + ones([2 * N + 1, 2 * N + 1], dtype=complex) * a ** 2)
ux, uy = meshgrid(u, u)
Ru = sqrt((ux - uy) ** 2 + ones([2 * N - 2, 2 * N - 2], dtype=complex) * a ** 2)
print("matrix Rz=",Rz)
print("matrix Ru=",Ru)
# P_B is the contribution to the vector potential due to current I_N. so P_B depends on Nth coloumn Rz values.
#so we need to create a array RiN without boundary conditions.
#then we need to calculate P, P_B
RiN = delete(Rz[:][N],[0,N,2*N])
P = (mu0 / (4 * pi)) * (exp(-k * Ru * 1j) / Ru) * dz
P_B = (mu0 / (4 * pi)) * (exp(-k * RiN * 1j) / RiN) * dz
print("matrix P=",P)
print("matrix P_B=",P_B)

#Then we need to calculate Q,Q_B from formulas we derived.
Q = -(a / mu0) * P * ((-k * 1j / Ru) + (-1 / Ru ** 2))
Q_B = -(a / mu0) * P_B * ((-k * 1j / RiN) + (-1 / RiN ** 2))
print("matrix Q=",Q)
print("matrix Q_B=",Q_B)

#Q4
#calculating J,I
#. Our final equation is MJ = QJ +QB*Im i.e., (M −Q) J = QB*Im. Invert (M −Q) and obtain J use inv(M-Q). Add the Boundary currents(zero at i=0, i=2N, and Im at i=N). 
J = matmul(inv(Matrix(N, a) - Q) , Q_B) * Im
print("j=",J)

I_derived = concatenate(([0], J[: N - 1], [Im], J[N - 1 :], [0]))
#I_assumed equation is given initially in question itself.
I_assumed = concatenate((Im * sin(k * (l - z[:N])), Im * sin(k * (l + z[N:]))))
print("I_derived=",I_derived)
print("I_assumed=",I_assumed)

plot(z,abs(I_derived),label = "Derived Current")
plot(z,I_assumed,label = "Assumed Current")
xlabel(r"$z$")
ylabel(r"$I$")
title("Antenna currents in a dipole antenna at N=100")
grid()
legend()
savefig('Endsem.png')
show()