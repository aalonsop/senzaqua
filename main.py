# Library to work with netCDF files
from netCDF4 import Dataset,num2date
import xarray as xr
import matplotlib.pyplot as plt

# Open a .nc file ("file_name")
file_id = Dataset('Input/SPEI12_genlogistic_global_era5_moda_ref1991to2020_202311.nc')
print(file_id.variables)

print(file_id.variables.keys())
for d in file_id.dimensions.items():
  print(d)

time = file_id.variables['time']
spe12 = file_id.variables['SPEI12']
x,y = file_id.variables['lat'], file_id.variables['lon']
print(time)
print(x)
print(y)
print(spe12.dimensions)

#print(file_id.variables['SPEI12'][0,:,:])

## Assigning variables
lats = file_id.variables["lat"][:]
lons = file_id.variables["lon"][:]
time = file_id.variables["time"]

## Data for only one day
dates = num2date(time[:], time.units)
time_of_data = dates[0].strftime("%Y-%m-%d %H:%M:%S")
print(time_of_data)

Spe12 = spe12[0, :, :]  # remove the time dimension

ds = xr.Dataset(
    {
        "spe12": (("lat", "lon"), Spe12),
    },
    {
        "lon": lons,
        "lat": lats,
    },
)

df = ds.to_dataframe()

## Visualize the variations with longitude
plt.figure()
ds.mean(dim="lat").to_dataframe().plot(marker="o")
plt.savefig("variation_with_longitude.png", bbox_inches="tight")


## Visualize the variations with longitude
plt.figure()
ds.mean(dim="lat").to_dataframe().plot(marker="o")
plt.savefig("variation_with_longitude.png", bbox_inches="tight")

## Visualize the variations with latitude
plt.figure()
ds.mean(dim="lon").to_dataframe().plot(marker="o")
plt.savefig("variation_with_latitude.png", bbox_inches="tight")