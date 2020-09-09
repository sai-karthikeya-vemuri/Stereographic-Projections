import numpy as np 
import matplotlib.pyplot as plt 
import pytest 
from SymmopCub432 import SymmopCub432
from qu2om import qu2om
import matplotlib.cm as cm
def stereographic_projector(unit_norm,quaternion):
    #gives stereographic projection coordinate of the specific unit normal whose orientation is given by unit quaternion
    
    rotation_matrix = qu2om(quaternion)
    #print("Rotation matrix:",rotation_matrix)
    S=SymmopCub432()
    global_coordinates= np.transpose(unit_norm).dot(rotation_matrix)
    #print("global coordinates:",global_coordinates)
    
    stereographic_coordinates = []

    for i in range(0,24):
        temp=global_coordinates.dot(S[i])
        x=temp[0]
        y=temp[1]
        z=temp[2]
        
        val = [(x)/(1+z),(y)/(1+z)]
        if (val[0]**2.0+val[1]**2)<=1:
            stereographic_coordinates.append(val)

    stereographic_coordinates = np.unique(stereographic_coordinates,axis=0)    
    return np.array(stereographic_coordinates)
    
def circle(r):
    #To draw the circle of equatorial plane
    x=np.linspace(-r,r,1000)
    y=np.sqrt(r*r - x*x)
    return x,y

def normalise(a):
    #Normalise the given vector
    fact = np.sqrt(a[0]**2+a[1]**2+a[2]**2)
    val = np.array([a[0]/fact,a[1]/fact,a[2]/fact]) 
    return val
def read_from_file(filename):
    #reads a csv file of orientations and saves them in a numpy array
    orientations=np.genfromtxt(filename,delimiter=',',dtype=float)
    return orientations

if __name__ == "__main__":
    unit=[]
    n=3
    for i in range(0, n):
        print("Enter vector component", i, ":")
        item = int(input())
        unit.append(item)
    unit_norm=normalise(unit)
    x,y=circle(1)
    fig,ax1 = plt.subplots(ncols=2)
    
    #ax1.figure()
    ax1[0].plot(x,y,color='black')
    ax1[0].plot(x,-y,color='black')
    orientations=read_from_file("list_of_orientations.csv")
    temp=np.random.uniform(size=(4,100))
    colors = cm.rainbow(np.linspace(0, 1, len(orientations)))
    theta=np.linspace(0,(np.pi)*0.5,num=50)
    #Binning of data (normalised)
    xhi=np.linspace(0,(np.pi)*0.5,num=50) 
    x=np.sin(theta)*theta
    y=xhi 
    Sx=[]
    Sy=[]
    #Uncomment this below for loop if you have a list of orientations in a csv file
    #for row in orientations:
        #print("For orientation:",row)
        #s=stereographic_projector(unit_norm,row)
        
        #print("final stereographic projections:",s)
        #ax1[0].scatter(s[:,0],s[:,1],s=30,label=row)
        #print("nothing")
    for row in temp:
        s=stereographic_projector(unit_norm,row)
        for i in s[:,0]:
            Sx.append(i)
        for j in s[:,1]:
            Sy.append(j)
        

        ax1[0].scatter(s[:,0],s[:,1],s=30,label=row)
        


    print(Sx)
    
    
    
    #ax1[0].legend(loc="upper right",fontsize='xx-small')

    #ax1[1].legend(loc="upper right",fontsize='xx-small')
    plt.hist2d(s[:,0],s[:,1],bins=[x,y],cmap=plt.cm.Reds)
    cb = plt.colorbar()
    cb.set_label('counts in bin')
        
    plt.show()
