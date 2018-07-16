import os
import re
import xarray as xr
import numpy as np
import datacube
from datacube.storage import netcdf_writer
from datacube.model import Variable, CRS


execID=10
algorithm = "MEDIANAS"
version= "1.0"

product = 'LS8_OLI_LASRC' #Producto sobre el que se hará la consulta (unidad de almacenamiento)
bands=["blue","green","red","nir", "swir1","swir2"] #arreglo de bandas 
time_ranges = [("2013-01-01", "2013-12-31")] #Una lista de tuplas, cada tupla representa un periodo
#área sobre la cual se hará la consulta:
min_long = -75
min_lat = 5


dc = datacube.Datacube(app="{}_{}_{}".format(algorithm,version,execID))
xarr={}
i=0
for tr in time_ranges:
    xarr[i] = dc.load(product=product, longitude=(min_long, min_long+1.0), latitude=(min_lat, min_lat+1), time=tr)
    i+=1

for i in range(0,1):
    xarr0=xarr[i] 
    del xarr
    
    xarr0.to_netcdf(str(i)+str(min_long)+'_'+str(min_lat)+"_salida.nc")
