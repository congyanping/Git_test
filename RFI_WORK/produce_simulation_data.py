#! /usr/bin/python
import numpy as np
b=[]
c=[]
def random_number():
    """the code result two hdf5 date,one is use sin as meshgrid then no people maked RFI the name called smooth_simulated_data_no_RFI.hdf5,the other one have the same data as the one, but i add some manmade RFI,the data called smooth_simulated_data_with_RFI.hdf5"""
    #a=np.random.randint(15, size=(150, 1008))
    #a=np.random.rand(152, 152)
    #a=2.5 * np.random.randn(160,160) + 3
    from scipy import interpolate
    x = np.arange(-5.01, 20.04, 0.25)
    y = np.arange(-5.01, 20.04, 0.25)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(xx**2+yy**2)
    f = interpolate.interp2d(x, y, z, kind='cubic')

    xnew = np.arange(-5.01, 20.04, 1e-2)
    ynew = np.arange(-5.01, 20.04, 1e-2)
    a = f(xnew, ynew)



    global c
    c=a.copy()
    print a.shape
    a[200]=100
    #a[52]=40
    a[1800]= -50
    a[120]=37
    global b
    b=a       
    return b
random_number()
print "b.value",b[50],type(b)

#plot smmoth data and having RFI data
import matplotlib.pyplot as plt
plt.subplot(211)
x=np.arange(len(b))
y=b[:,1]
if len(x)==len(y):
    print 'ok'
print len(x) ,'==',len(y)
plt.plot(x,y)

plt.subplot(212)
xx=np.arange(len(c))
yy=c[:,3]
plt.plot(xx,yy)
plt.show()




import h5py
simulated_data=h5py.File('smooth_simulated_data_with_RFI.hdf5','w')
simulated_data.create_dataset('vis', data=b)
simulated_data.close()

simulated_data_smooth=h5py.File('smooth_simulated_data_no_RFI.hdf5','w')
simulated_data_smooth.create_dataset('vis', data=c)
simulated_data_smooth.close()


