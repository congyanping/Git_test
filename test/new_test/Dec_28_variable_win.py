#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import h5py
import sys
import math
import time
def stdev(array, xbar):
    var = 0
    count = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            var += (array[i,j]-xbar)**2
            count = count + 1
    	    print "the count value",count
        #end for j
    #end for i
    try:
       var = var/count
    except ZeroDivisionError:
           var = var/(count+1) 
	#variance
    std = np.sqrt(var)	#standard deviation
    return std
#end stdev



def calculateSigma(winD, winP, data, smooth):
    #sigma = 0
    if winP[0]+winD[0]/2 < data.shape[0] and winP[1]+winD[1]/2 < data.shape[1]:
   
       smoothR = smooth[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
                        winD[1]/2:winP[1]+winD[1]/2]
       dataR = data[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
                    winD[1]/2:winP[1]+winD[1]/2]
       xbar = np.median(smoothR)
       print "calculate_xbar",xbar
       print "calculate_smoothR",smoothR
       global sigma
       sigma = stdev(dataR, xbar)
       print "the value of sigma",sigma
    return sigma



#end calculateSigma
def flagWindow(winD, winP, data, smooth, sigma, mask):
    smoothR = smooth[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
                     winD[1]/2:winP[1]+winD[1]/2]
    dataR = data[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
                 winD[1]/2:winP[1]+winD[1]/2]
    maskR = mask[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
                 winD[1]/2:winP[1]+winD[1]/2]
    xbar = np.median(smoothR)
    for i in range(dataR.shape[0]):
        for j in range(dataR.shape[1]):
            if np.abs(sigma) > 0:
              if dataR[i,j].real - xbar >  3.0*np.abs(sigma):
                maskR[i,j] = 1
                dataR[i,j] = smoothR[i,j]
              #end if
            elif sigma==0:
              print "this is a zero point"
            else:
                #pass 
 	      print "sigma too low",sigma
        #end for j
    #end for i
    mask[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
                 winD[1]/2:winP[1]+winD[1]/2] = maskR
   # data[winP[0]-winD[0]/2:winP[0]+winD[0]/2,winP[1]-
   #             winD[1]/2:winP[1]+winD[1]/2] = dataR
#end flagWindow
def varyWindow(prevSize, deltaSigma):
    if deltaSigma >= 2:
        newSize = (prevSize[0], 128)
    elif deltaSigma >= 1:
        newSize = (prevSize[0], 192)
    else :
        newSize = (prevSize[0], 256)
    #end if
    return newSize
#end varyWindow
def main():
    if len(sys.argv) < 3:
       print "Include raw data and smoothing data"
       quit()
#end if
    dfn = sys.argv[1]
    sfn = sys.argv[2]
    print 'ok'
    dataFile = h5py.File(dfn, 'r')
    smoothFile = h5py.File(sfn, 'r')
    maskFile = h5py.File('varWin_'+str(dfn)+'_mask_value.hdf5', 'w')
    #the spectra like the 'visbility'
    #dset = dataFile['vis'][:,:,0].real   #for Tianlai
    #sset = smoothFile['vis'][:,:,0].real   #for Tianlai
    dset = dataFile['vis'][:,:]
    sset = smoothFile['vis'][:,:]#i simulated interplot date shape is (150,1008)
    data = np.abs(dset[...])#change
    smooth = np.abs(sset[...])#change
    mask = np.zeros_like(data,dtype = int)
    #Now actually do important algorithmic steps.
    print 'ok',dset.shape
    for k in range(3):
        dsig1 =0
        dsig2 = 0
        dsig3 = 0
        winDim = (4,8)#this will be an error point
        moveFreq = winDim[1]/2
        moveTim = winDim[0]/2
        run = 1
	trun = 1
        winPos = [moveTim*trun, moveFreq * run]
        #st = time.clock()
    #Now loop some other number of times, to move the window around
        print 'finish for loop'
        while winPos[0]+(winDim[0]/2)< data.shape[0]-1:
              dsig1 =0
              dsig2 = 0
              dsig3 = 0
              run = 1
              sigma_last = 500
              #Window dimensions set as a tuple (t,f)
              #winDim = (10,10)
              #winDim = (30,30)
              #calculate sigma
	      print 'while finish'
              sigma_now = calculateSigma(winDim, winPos, data, smooth)
	      print '###'
	      while winPos[1]+(winDim[1]/2) < data.shape[1]-1:
                    #run += 1
                    moveFreq = winDim[1]/2
                    winPos = (moveTim*trun, moveFreq * run)
                    flagWindow(winDim, winPos, data, smooth, sigma_now, mask)
                    dsig1 = dsig2
                    dsig2 = dsig3
                    dsig3 = sigma_last - sigma_now
                    deltaSigma = (dsig1 + dsig2 + dsig3) / 3
                    winDim = varyWindow(winDim, deltaSigma)	#winDim==newsize
                    sigma_last = sigma_now
                    sigma_now = calculateSigma(winDim, winPos, data, smooth)
		   #trun += 1
                    run = run + 1
                    print "inner while finish"
              trun = trun + 1
              winPos = (moveTim*trun, moveFreq * run)
    	print "the value of trun",trun
    maskFile.create_dataset('MaskData', data=mask)
    maskFile.close()
    dataFile.close()
    smoothFile.close()
main()
print "################################"
#if __name__=="__main__":
#   p=func()
#   print p.params_init
