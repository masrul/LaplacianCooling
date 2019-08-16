import numpy as np 
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
n=150
r=5    
T=500

nframes=3000  
duration=20 #sec 

room=np.zeros((n, n))

r2=r*r

icenter=n/4
jcenter=n/4
for i in range(int(icenter-r),int(icenter+r)):
    ix=abs(i-icenter)
    for j in range(int(jcenter-r),int(jcenter+r)):
        jx=abs(j-jcenter)
        if (ix*ix+jx*jx<=r2):
            room[i,j]=T

icenter=3*(n/4)
jcenter=n/4
for i in range(int(icenter-r),int(icenter+r)):
    ix=abs(i-icenter)
    for j in range(int(jcenter-r),int(jcenter+r)):
        jx=abs(j-jcenter)
        if (ix*ix+jx*jx<=r2):
            room[i,j]=T

icenter=(n/4)
jcenter=3*(n/4)
for i in range(int(icenter-r),int(icenter+r)):
    ix=abs(i-icenter)
    for j in range(int(jcenter-r),int(jcenter+r)):
        jx=abs(j-jcenter)
        if (ix*ix+jx*jx<=r2):
            room[i,j]=T

icenter=3*(n/4)
jcenter=3*(n/4)
for i in range(int(icenter-r),int(icenter+r)):
    ix=abs(i-icenter)
    for j in range(int(jcenter-r),int(jcenter+r)):
        jx=abs(j-jcenter)
        if (ix*ix+jx*jx<=r2):
            room[i,j]=T

fig = plt.figure()

plt.tick_params(
    axis='x',          
    which='both',      
    bottom=False,      
    top=False,         
    labelbottom=False) 
plt.tick_params(
    axis='y',          
    which='both',      
    left=False,      
    right=False,        
    labelleft=False) 

ims=[]
fps=nframes/duration
interval=(duration*1000)/nframes 
for itr in range(nframes):
    print ('iteration# :', itr)  
    for i in range(1,n-1):
        for j in range(1,n-1):
            room[i,j]=(1/8.0)*(
                room[i-1,j]+
                room[i+1,j]+
                room[i,j-1]+
                room[i,j+1]+
                room[i-1,j+1]+
                room[i-1,j-1]+
                room[i+1,j+1]+
                room[i+1,j-1]
            )
    
    im = plt.imshow(
            room, 
            interpolation='none', 
            #cmap=cm.RdYlBu_r,
            cmap=cm.Spectral_r,
            origin='lower', 
            extent=[-10,10,-10,10],
            vmax=100, vmin=0
        )
    ims.append([im])

ani = animation.ArtistAnimation(fig,ims,interval=interval)
ani.save('cooling-4-source.gif',fps=fps, dpi=100,writer='imagemagick')
plt.show()
