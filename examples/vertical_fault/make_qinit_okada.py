"""
Make data for qinit by evaluation Okada in the grid cells
determined by grid.data
"""

from pylab import *

import setfault

fault = setfault.make_fault()

tend = 0.
for s in fault.subfaults:
    tend = max(tend, s.rupture_time + 2*s.rise_time)

times = [tend + 10]  # after all rupture motion

xgrid,zgrid = loadtxt('grid.data', skiprows=1, unpack=True)
xcell = 0.5*(xgrid[:-1] + xgrid[1:]) # cell centers

x = xcell / 111.e3  # convert meters to longitude
y = array([0,1])  # for 1d Okada

dtopo = fault.create_dtopography(x,y,times)

dz = dtopo.dZ[-1,0,:]  # slice in x at final time

savetxt('qinit_okada.data',dz)


if 1:
    figure(351)
    clf()
    plot(xcell,dz)
    title('Okada final deformation')
    
