# Suppose we want to interpolate the 2-D function
import numpy as np

#def func(x, y):
#    return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

# on a grid in [0, 1]x[0, 1]

#grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

import matplotlib                                                             
matplotlib.use('Agg')# but we only know its values at 1000 data points:
import matplotlib.pyplot as plt
import h5py
import sys
f= h5py.File(sys.argv[1],'r')
vis=[]
for i in range(1008):
    vi = np.sum(np.abs(f['vis'][48:66,i]))/18.0
    vis.append(vi)
print "vis shape",len(vis)
import scipy.signal as signal
x = np.linspace(1,1008,1008)
y = vis
y_new = signal.medfilt(y,5)
print "y_new type",type(y_new)
file = np.zeros((150,1008))
for i in range(file.shape[1]):
    file[:,i]=y_new[i]
g= h5py.File('20160928235342_20160929000342.hdf5_smooth.hdf5','w')
g.create_dataset('vis',data=file)
g.close()


"""
from scipy import interpolate
x = np.linspace(1,1008,1008)
y =list(vis)
xnew = np.linspace(1,1008,10080)
print xnew.shape
plt.plot(x,y,'ro')
for kind in ['nearest']:
    f = interpolate.interp1d(x,y,kind=kind)
    ynew =f(xnew)
    plt.plot(xnew,ynew,label=str(kind))
    g= h5py.File('20160928235342_20160929000342.hdf5_smooth.hdf5','w')
    print "line of ynew",len(ynew)
    file = np.zeros((150,10080))
    for i in range(file.shape[1]):
        file[:,i] = ynew[i]
        #print ynew[i]
    #print [j for j in file[2,:] if j >0]
    file = file[:,0:10080:10]
    print "file shape is", file.shape
    g.create_dataset('vis',data=file)
    g.close()
plt.legend(loc='lower right')
plt.savefig("new_picture")
"""





#points = np.random.rand(150, 2)
#x= np.linspace(1,150,150)
#y=np.linspace(1,150,150)
#values = func(x, y)
#print "the line of values is",len(values)
#print "the values is",values
## This can be done with `griddata` -- below we try out all of the
## interpolation methods:
#
#from scipy.interpolate import griddata
#grid_z0 = griddata(points, vis, (grid_x, grid_y), method='nearest')
#grid_z1 = griddata(points, vis, (grid_x, grid_y), method='linear')
#grid_z2 = griddata(points, vis, (grid_x, grid_y), method='cubic')
#
#print "type of grid_z0 is",grid_z0
#


# One can see that the exact result is reproduced by all of the
# methods to some degree, but for this smooth function the piecewise
# cubic interpolant gives the best results:

#import matplotlib.pyplot as plt
#plt.subplot(221)
#plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
#plt.plot(points[:,0], points[:,1], 'k.', ms=1)
#plt.title('Original')
#plt.subplot(222)
#plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
#plt.title('Nearest')
#plt.subplot(223)
#plt.imshow(grid_z1.T, extent=(0,1,0,1), origin='lower')
#plt.title('Linear')
#plt.subplot(224)
#plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')
#plt.title('Cubic')
#plt.gcf().set_size_inches(6, 6)
#plt.savefig('for_interplot.png')
