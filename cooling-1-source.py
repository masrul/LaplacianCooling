import numpy as np 
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

n=75  # grid size
r=10  # source size 
T=1000 # temperature 

niterations=10000 
dframes=5 # dumping inverval of frames  
duration=20 #sec 

room=np.zeros((n, n))

mid=n/2
r2=r*r

for i in range(int(mid-r),int(mid+r)):
    ix=abs(i-mid)
    for j in range(int(mid-r),int(mid+r)):
        jx=abs(j-mid)
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
nframes=niterations/dframes 
fps=nframes/duration
interval=(duration*1000)/nframes  
for itr in range(niterations):
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

    if((itr%dframes)==0):
        print("Dumping itration#:",itr)
        print() 
    
        im = plt.imshow(
                room, 
                interpolation='none', 
                cmap=cm.jet,
                origin='lower', 
                extent=[-10,10,-10,10],
                vmax=100, vmin=0
            )
        ims.append([im])

ani = animation.ArtistAnimation(fig,ims,interval=interval)
ani.save('cooling-1-source.gif',fps=fps, dpi=100,writer='imagemagick')
ani.save('cooling-1-source.mp4',fps=fps, dpi=100)
plt.show()
