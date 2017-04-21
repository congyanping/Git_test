import h5py
import matplotlib.cm as cm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
#file_name='/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928081451_20160928082451.hdf5'
#file_name='/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928120435_20160928121434.hdf5'
bi = 931#bl order
#file_name='/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928140426_20160928141425.hdf5'
file_name0='/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928133428_20160928134427.hdf5'
#file_name='/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928133428_20160928134427.hdf5'
#file_name1 = '/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928141425_20160928142424.hdf5'
file_name1 = '/node3_disk/disk1/20160927201537_122hrhdf5_part1/20160928134427_20160928135427.hdf5'
def read_date():
    """read two file and link together,mask noise data,and for visbility in 1 axis cut off,because there no data in two side for 1 axis"""
    vis = np.zeros((150*2, 1008), dtype=np.complex64)
    day_file = [file_name0,file_name1]
    for index, name in enumerate(day_file):
        f = h5py.File(name, 'r')
        vis[index*150:(index+1)*150] = f['vis'][:, :, bi]
    f = h5py.File(file_name0, 'r')
    bl_order=f['blorder'][bi]
    f0   =f.attrs["freqstart"]
    fstep=f.attrs["freqstep"]
    fn   =f.attrs["nfreq"]
    y_aixs=np.arange(vis.shape[0])
    freq=np.arange(f0+224*fstep,f0+fstep*fn-224*fstep,fstep)
    #freq=np.arange(f0,f0+fstep*fn,fstep)
    print bl_order
    print vis.shape,type(vis.shape)
    print f0,fstep,fn,f0+fstep*fn
    mask = np.zeros((150*2,1008))
    for i in range(17,28):
        mask[i]=1
    for i in range(77,88):
        mask[i]=1
    for i in range(137,148):
        mask[i]=1
    for i in range(197,208):
        mask[i]=1
    for i in range(257,268):
        mask[i]=1
    #for i in range(47,58):
    #    mask[i]=1
    #for i in range(107,118):
    #    mask[i]=1
    #for i in range(167,178):
    #    mask[i]=1
    #for i in range(227,238):
    #    mask[i]=1
    #for i in range(287,298):
    #    mask[i]=1
    #for i in range(45,60):
    #    mask[i]=1
    #for i in range(105,116):
    #    mask[i]=1
    vis=np.ma.array(vis,mask=mask)[:,244:-244]
    #print "vis.shape is" ,vis.shape
    return vis
    
    
# mapping step
def Plot_waterfall(read_data):
    from datetime import datetime
    import matplotlib.dates as mdates
    y_axis=[datetime(2016,9,28,14,04), datetime(2016,9,28,14,24)]
    y_aixs=mdates.date2num(y_axis)
    fig, ax = plt.subplots()
    extent = [freq[0], freq[-1], y_aixs[0], y_aixs[-1]]
    date_format = mdates.DateFormatter('%H:%M')
    ax.yaxis.set_major_formatter(date_format)
    vis = read_data()
    pim = ax.imshow(vis.imag, extent=extent, origin='lower', aspect='auto')
    cmap=matplotlib.cm.jet
    #pim=plt.imshow(vis.real, extent=extent, origin='lower',cmap=cmap)
    cbar = plt.colorbar(pim)
    ax.set_ylabel('Time')
    ax.set_xlabel('MHz')
    plt.title('sun_imag_waterfall')
    fig_name='sun_imag_waterfall_%s_%s.png' %(bl_order[0],bl_order[1])
    plt.savefig(fig_name)
Plot_waterfall()      

