import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp 
fignum=1
def time_response(decay_constant,w,labell):
    pol1=np.poly1d([1,decay_constant])
    pol2=np.poly1d([1,2*decay_constant,decay_constant*decay_constant+w*w])
    pol3=np.poly1d([1,0,w*w])
    newpol=np.polymul(pol2,pol3)
    H=sp.lti(pol1,newpol)
    t=np.linspace(0,50,1000)
    t,x=sp.impulse(H,None,t)
    plt.plot(t,x,label="{}".format(labell))
    plt.title("Time response of a spring ")
    plt.xlabel(r'time$\rightarrow$',fontsize=15)
    plt.ylabel(r'x(t)$\rightarrow$',fontsize=15)
    plt.legend()
    plt.savefig('{}.png'.format(labell))
    plt.show()
def responses_at_diff_freq():
    transfer_function=sp.lti([1],[1,0,2.25])
    i=1
    for w in np.arange(1.4,1.6,0.05):
        t=np.linspace(0,50,1000)
        f=(np.cos(w*t))*(np.exp(-0.05*t))
        x=sp.lsim(transfer_function,f,t)
        plt.subplot(3,2,i)
        plt.plot(t,x[1],label=r'$\omega$''={}'.format(w))
        plt.xlabel(r'time$\rightarrow$',fontsize=15)
        plt.ylabel(r'x(t)$\rightarrow$',fontsize=15)
        plt.legend()
        i+=1
    plt.savefig('diff_omega=.png')
    plt.show()
def coupled_spring():
    t=np.linspace(0,20,1000)
    Hx=sp.lti([1,0,2],[1,0,3,0])
    Hy=sp.lti([2],[1,0,3,0])
    x=sp.impulse(Hx,None,t)
    y=sp.impulse(Hy,None,t)
    plt.plot(x[0],x[1],label='x(t)')
    plt.plot(y[0],y[1],label='y(t)')
    plt.title("coupled spring solution")
    plt.xlabel(r'time$\rightarrow$',fontsize=15)
    plt.ylabel(r'x(t),y(t)',fontsize=15)
    plt.legend()
    plt.savefig("coupled_spring.png")
    plt.show()
def two_port_network(H):
    freq,mag,phase=H.bode()
    plt.semilogx(freq,mag)
    plt.title("Magnitude of Transfer function of given two-port network.")
    plt.xlabel(r'$\omega$(log scale)$\rightarrow$',fontsize=15)
    plt.ylabel(r'Magnitude',fontsize=15)
    plt.savefig("Magnitude.png")
    plt.show()
    plt.semilogx(freq,phase)
    plt.title("phase of Transfer function of given two-port network.")
    plt.xlabel(r'$\omega$(log scale)$\rightarrow$',fontsize=15)
    plt.ylabel(r'Phase',fontsize=15)
    plt.savefig("Phase.png")
    plt.show()
def output_voltage(H,tmax,label):
    t=np.linspace(0,tmax,10000)
    vi=np.cos(1000*t)-np.cos(1000000*t)
    v0=sp.lsim(H,vi,t)
    plt.plot(t,v0[1])
    plt.xlabel(r't$\rightarrow$',fontsize=15)
    plt.ylabel(r'$V_{o}(t)$',fontsize=15)
    plt.savefig("{}.png".format(label))
    plt.show()
time_response(0.5,1.5,'decay_constant=0.5')
time_response(0.05,1.5,'decay_constant=0.05')
responses_at_diff_freq()
coupled_spring()
H=sp.lti([1000000],[0.000001,100,1000000])
two_port_network(H)
output_voltage(H,30*0.000001,'fast_Variation')
output_voltage(H,10*0.001,'slow_variation')