#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:30:49 2024

@author: alonso-pinar_a
"""

#%% Import modules

from netCDF4 import Dataset,num2date
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#%% Read files

filepath = 'Input/'
filename = 'SPEI12_genlogistic_global_era5_moda_ref1991to2020_202311.nc'

ds = xr.open_dataset( filepath + filename )


#%% Inspect data

plt.figure()
plt.imshow( ds['SPEI12'][0,:,:] )
plt.colorbar()
plt.show()

#This is too difficult to visualize
#Lets get rid of oceans

ds['SPEI12mod'] = ds['SPEI12'].where(ds['SPEI12'] != -9999, np.nan)

plt.figure()
plt.imshow( ds['SPEI12mod'][0,:,:] )
plt.colorbar()
plt.show()

#%% Second file

filename2 = 'SPEI12_genlogistic_global_era5_moda_ref1991to2020_19910101to20231001_mozambique.nc'

ds_moz = xr.open_dataset( filepath + filename2 )

#%%

#Same as before
ds_moz['SPEI12mod'] = ds_moz['SPEI12'].where(ds_moz['SPEI12'] != -9999, np.nan)


day = 10 #0 is 01/01/1991 and 393 is 01/10/2023

formatted_date = str(ds_moz['SPEI12mod'].time[day].values)[:10]

plt.figure()
plt.imshow( ds_moz['SPEI12mod'][10,:,:] )
plt.colorbar()
plt.title( formatted_date )
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()


