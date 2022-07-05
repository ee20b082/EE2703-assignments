from pylab import *
fignum = [0]
t = linspace(-pi, pi, 65)[:-1]
dt = t[1] - t[0]; fmax = 1/dt
y=sin(sqrt(2)*t)
y[0]=0                              # the sample corresponding to -tmax should be set zero
y=fftshift(y)                       # make y start with y(t=0)
Y=fftshift(fft(y))/64.0
w=linspace(-pi*fmax,pi*fmax,65)[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-10,10])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin\left(\sqrt{2}t\right)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-10,10])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t1=linspace(-pi,pi,65)[:-1]
t2=linspace(-3*pi,-pi,65)[:-1]
t3=linspace(pi,3*pi,65)[:-1]
figure(2)
plot(t1,sin(sqrt(2)*t1),'b',lw=2)
plot(t2,sin(sqrt(2)*t2),'r',lw=2)
plot(t3,sin(sqrt(2)*t3),'r',lw=2)
ylabel(r"$y$",size=16)
xlabel(r"$t$",size=16)
title(r"$\sin\left(\sqrt{2}t\right)$")
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t1=linspace(-pi,pi,65)[:-1]
t2=linspace(-3*pi,-pi,65)[:-1]
t3=linspace(pi,3*pi,65)[:-1]
y=sin(sqrt(2)*t1)
figure(3)
plot(t1,y,'bo',lw=2)
plot(t2,y,'ro',lw=2)
plot(t3,y,'ro',lw=2)
ylabel(r"$y$",size=16)
xlabel(r"$t$",size=16)
title(r"$\sin\left(\sqrt{2}t\right)$ with $t$ wrapping every $2\pi$ ")
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-pi,pi,65)[:-1]
dt=t[1]-t[0]
fmax=1/dt
y=t
y[0]=0                                  # the sample corresponding to -tmax should be set zeroo
y=fftshift(y)                           # make y start with y(t=0)
Y=fftshift(fft(y))/64.0
w=linspace(-pi*fmax,pi*fmax,65)[:-1]
figure()
semilogx(abs(w),20*log10(abs(Y)),lw=2)
xlim([1,10])
ylim([-20,0])
xticks([1,2,5,10],["1","2","5","10"],size=16)
ylabel(r"$|Y|$ (dB)",size=16)
title(r"Spectrum of a digital ramp")
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t1=linspace(-pi,pi,65)[:-1]
t2=linspace(-3*pi,-pi,65)[:-1]
t3=linspace(pi,3*pi,65)[:-1]
n=arange(64)
wnd=fftshift(0.54+0.46*cos(2*pi*n/63))
y=sin(sqrt(2)*t1)*wnd
figure(3)
plot(t1,y,'bo',lw=2)
plot(t2,y,'ro',lw=2)
plot(t3,y,'ro',lw=2)
ylabel(r"$y$",size=16)
xlabel(r"$t$",size=16)
title(r"$\sin\left(\sqrt{2}t\right)\times w(t)$ with $t$ wrapping every $2\pi$ ")
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-pi,pi,65)[:-1]
dt=t[1]-t[0]
fmax=1/dt
n=arange(64)
wnd=fftshift(0.54+0.46*cos(2*pi*n/63))
y=sin(sqrt(2)*t)*wnd
y[0]=0                              # the sample corresponding to -tmax should be set zeroo
y=fftshift(y)                       # make y start with y(t=0)
Y=fftshift(fft(y))/64.0
w=linspace(-pi*fmax,pi*fmax,65)[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-8,8])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin\left(\sqrt{2}t\right)\times w(t)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-8,8])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-4*pi,4*pi,257)[:-1]
dt=t[1]-t[0];fmax=1/dt
n=arange(256)
wnd=fftshift(0.54+0.46*cos(2*pi*n/256))
y=sin(sqrt(2)*t)
y=y*wnd
y[0]=0                              # the sample corresponding to -tmax should be set zeroo
y=fftshift(y)                       # make y start with y(t=0)
Y=fftshift(fft(y))/256.0
w=linspace(-pi*fmax,pi*fmax,257)[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-8,8])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin\left(\sqrt{2}t\right)\times w(t)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-8,8])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-4*pi,4*pi,257);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
w0 = 0.86
y=(cos(w0*t))**3
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/256.0
w=linspace(-pi*fmax,pi*fmax,257);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-3,3])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos^3(w_0t)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-3,3])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-4*pi,4*pi,257);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
w0 = 0.86
y=cos(w0*t)**3
n=arange(256)
wnd=fftshift(0.54+0.46*cos(2*pi*n/256))
y = y*wnd
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/256.0
w=linspace(-pi*fmax,pi*fmax,257);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-3,3])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos^3(w_0t)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-3,3])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

#Q3
t=linspace(-pi,pi,129);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
delta = 0.5
w0 = 1.5
y=cos(w0*t + delta)
n=arange(128)
wnd=fftshift(0.54+0.46*cos(2*pi*n/128))
y = y*wnd
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/128.0
w=linspace(-pi*fmax,pi*fmax,129);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-3,3])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos(w_0t + \delta)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-3,3])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

ii = where(w>0)
omega = (sum(abs(Y[ii])**2*w[ii])/sum(abs(Y[ii])**2))       #weighted average
print ("omega = ", omega)

sup = 1e-4
window = 1
ii_1=np.where(np.logical_and(np.abs(Y)>sup, w>0))[0]
np.sort(ii_1)
points=ii_1[1:window+1]
print ("delta = ",np.sum(np.angle(Y[points]))/len(points))

#Q4
t=linspace(-pi,pi,129);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
delta = 0.5
w0 = 1.5
y=cos(w0*t + delta) + 0.1*np.random.randn(128)
n=arange(128)
wnd=fftshift(0.54+0.46*cos(2*pi*n/128))
y = y*wnd
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/128.0
w=linspace(-pi*fmax,pi*fmax,129);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-3,3])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos(w_0t + \delta)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-3,3])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

ii = where(w>0)
omega = (sum(abs(Y[ii])**2*w[ii])/sum(abs(Y[ii])**2))       #weighted average
print ("omega = ", omega)

sup = 1e-4
window = 1
ii_1=np.where(np.logical_and(np.abs(Y)>sup, w>0))[0]
np.sort(ii_1)
points=ii_1[1:window+1]
print ("delta = ",np.sum(np.angle(Y[points]))/len(points))

#Q5
t=linspace(-pi,pi,1025);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt

y=cos(16*(1.5 + t/(2*pi))*t)
n=arange(1024)
wnd=fftshift(0.54+0.46*cos(2*pi*n/1024))
y = y*wnd
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/1024.0
w=linspace(-pi*fmax,pi*fmax,1025);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-60,60])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of chirp function")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-60,60])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-pi,pi,1025);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt

y=cos(16*(1.5 + t/(2*pi))*t)
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/1024.0
w=linspace(-pi*fmax,pi*fmax,1025);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-60,60])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of chirp function")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-60,60])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

t=linspace(-pi,pi,1025);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
t_pieces = np.split(t,16)

Ymag = np.zeros((16,64))
Yangle = np.zeros((16,64))

for i in range(16):
  n=arange(64)
  y=cos(16*(1.5 + t_pieces[i]/(2*pi))*t_pieces[i])
  wnd=fftshift(0.54+0.46*cos(2*pi*n/64))
  y = y*wnd
  y[0]=0 # the sample corresponding to -tmax should be set zeroo
  y=fftshift(y) # make y start with y(t=0)
  Y=fftshift(fft(y))/64.0
  Ymag[i] = abs(Y)
  Yangle[i] = angle(Y)
w=linspace(-pi*fmax,pi*fmax,65);w=w[:-1]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t=t[::64]
t,w=np.meshgrid(t,w)

surf=ax.plot_surface(w,t,Ymag.T,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.ylabel("Frequency")
plt.xlabel("time")
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(w,t,Yangle.T,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.ylabel("Frequency")
plt.xlabel("time")
savefig('fig{}.png'.format(fignum[0]))
fignum[0] += 1
show()