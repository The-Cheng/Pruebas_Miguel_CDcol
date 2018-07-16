import os
import re
import xarray as xr
import numpy as np

for i in range(0,1):
    xarr0=xarr[i] 
    del xarr
    
    xarr0.to_netcdf(str(i)+str(min_long)+'_'+str(min_lat)+"_salida.nc")
