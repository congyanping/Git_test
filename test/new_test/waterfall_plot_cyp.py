import h5py
import matplotlib.cm as cm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#file_name='/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928081451_20160928082451.hdf5'

file_name='/node3_disk/disk2/20160927201537_122hrhdf5_part2/20160928235342_20160929000342.hdf5'
#file_name='20160928235342_20160929000342.hdf5_smooth.hdf5'
bi = 21#bl orderi
bi =188


f = h5py.File(file_name, 'r')
gg = h5py.File('varWin_masked_vis_data[0].hdf5_mask_value.hdf5','r')
vis1= gg['MaskData'][:,:]
vis = f['vis'][:, :,1]
bl_order=f['blorder'][bi]
#for i in range(10000):
#    if True:
#        print i,f['blorder'][i][0],f['blorder'][i][1]
#freq=[0,1000]
#y_aixs=[0,1000]
f0   =f.attrs["freqstart"]
fstep=f.attrs["freqstep"]
fn   =f.attrs["nfreq"]
freq=np.arange(f0,f0+fstep*fn,fstep)
y_aixs=np.arange(vis.shape[0])
print vis.shape,type(vis.shape)
print f0,fstep,fn,f0+fstep*fn
mask=[0]*1008
mask=[mask]*150
mask=np.array(mask)
for i in range(17,28):
    mask[i]=1
for i in range(77,88):
    mask[i]=1
for i in range(137,148):
    mask[i]=1
vis=np.ma.array(vis,mask=mask)

#stored the data
#g = h5py.File("masked_vis_data[1].hdf5",'w')
#g.create_dataset('vis',data=vis)
#g.close()












# mapping step
fig=plt.figure(figsize=(8,6),dpi=72,facecolor="white")
axes=plt.subplot(111)
extent = [freq[0], freq[-1], y_aixs[0], y_aixs[-1]]
#cmap=matplotlib.cm.jet
cmap = matplotlib.cm.gray
#norm = matplotlib.colors.Normalize(vmin=160, vmax=300)
pim=plt.imshow(vis1, extent=extent, origin='lower',cmap=cmap)
cbar = plt.colorbar(pim)
axes.set_ylabel('4t')
axes.set_xlabel('MHz')
plt.title('RFI_flag')
#fig_name='real_waterfall_%s_%s_smooth[1].png' %(bl_order[0],bl_order[1])
fig_name ='rfi_flag.png'
plt.savefig(fig_name)
  























