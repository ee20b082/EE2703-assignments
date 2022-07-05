from pylab import *
i=0
class function:
    def __init__(self,function,N,tmin,tmax,xlim,name,gauss):
        self.fun=function
        self.N=N
        self.tmin=tmin
        self.tmax=tmax
        self.xlim=xlim
        self.name=name
        self.gauss=gauss
def plotting(f):
    global i
    t=linspace(f.tmin,f.tmax,f.N+1);t=t[:-1]
    y=f.fun(t)
    Y=fftshift(fft(y))/f.N
    w=linspace(-64,64,f.N+1)
    w=w[:-1]
    if (f.name == 'gauss'): 
        Y = fftshift(abs(fft(y)))/f.N
        Y = Y*sqrt(2*pi)/max(Y)
        Y0 = exp(-w**2/2)*sqrt(2*pi)
        print("maximum error is {} at time range={} and period={}".format(abs(Y-Y0).max(),format(2*f.tmax),format(f.N)))
    figure()
    subplot(2,1,1)
    plot(w,abs(Y),lw=2)
    xlim([-f.xlim,f.xlim])
    ylabel(r"$|Y|$",size=16)
    if (f.name == 'gauss'): 
        title(r"Spectrum of gauss at time range of ${}$".format(2*f.tmax))
    else:
        title(r"Spectrum of ${}$".format(f.name))
    grid(True)
    subplot(2,1,2)
    ii=where(abs(Y)>1e-3)
    if (f.gauss):
        plot(w,angle(Y),'ro',lw=2)
    plot(w[ii],angle(Y[ii]),'go',lw=2)
    xlim([-f.xlim,f.xlim])
    ylabel(r"Phase of $Y$",size=16)
    xlabel(r"$k$",size=16)
    grid(True)
    savefig("plot{}.png".format(i))
    i+=1
    show()
sin5x=function(lambda x:sin(5*x),128,0,2*pi,10,"sin(5*x)",1)
plotting(sin5x)
AMmod=function(lambda x : (1 + 0.1 * cos(x))*cos(10*x),512,-4*pi,4*pi,15,"(1 + 0.1 * cos(x))*cos(10*x)",1)
plotting(AMmod)
sinx3=function(lambda x:sin(x)**3,512,-4*pi,4*pi,15,"sin(x)^3",1)
plotting(sinx3)
cosx3=function(lambda x:cos(x)**3,512,-4*pi,4*pi,15,"cos(x)^3",1)
plotting(cosx3)
cossx=function(lambda x:cos(20*x+5*cos(x)),512,-4*pi,4*pi,40,"cos(20*x+5*cos(x))",0)
plotting(cossx)
gauss=function(lambda x : exp(-x**2/2),512,-4*pi,4*pi,10,"gauss",1)
plotting(gauss)
gauss1=function(lambda x : exp(-x**2/2),512,-6*pi,6*pi,10,"gauss",1)
plotting(gauss1)
gauss2=function(lambda x : exp(-x**2/2),512,-8*pi,8*pi,10,"gauss",1)
plotting(gauss2)
gauss3=function(lambda x : exp(-x**2/2),256,-4*pi,4*pi,10,"gauss",1)
plotting(gauss3)
gauss4=function(lambda x : exp(-x**2/2),1024,-4*pi,4*pi,10,"gauss",1)
plotting(gauss4)