import h5py
import numpy as np
import sys
import h5py
import matplotlib.cm as cm
import matplotlib
matplotlib.use('Agg')
f=h5py.File(sys.argv[1],'r')
try:
   ff=f['MaskData']
except:
      ff=f['vis'].real

print "ff.shape",ff.shape

y=[]
for i in range(ff.shape[1]):
    y.append(np.sum(ff[:,i]))
    print ff[:,i]

#for i in range(ff.shape[0]):
#    for j in range(ff.shape[1]):
#        if ff[0:i,0:j]>=1:
#           print i,j
print "ff.shape is",ff.shape,np.sum(ff)#,list(ff[45:55,0:10])
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt




file_name='/node3_disk/disk2/20160927201537_122hrhdf5_part2/20160928235342_20160929000342.hdf5'
f = h5py.File(file_name, 'r')
f0   =f.attrs["freqstart"]
fstep=f.attrs["freqstep"]
fn   =f.attrs["nfreq"]
ff=f0+fstep*fn
x = np.arange(f0,ff,fstep)
plt.subplot(111)
#x=np.arange(len(y))
y=np.array(y)
plt.plot(x,y)
plt.savefig("mask_picture_of_"+str(sys.argv[1])+"smmoth.png")
