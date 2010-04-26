import glob
from datetime import datetime

from LMAtools.make_grids import grid_h5flashfiles


h5_filenames = glob.glob('LYL*.flash.h5')
start_time = datetime(2009,7,24, 1,00,00)
end_time   = datetime(2009,7,24, 1,04,00)

frame_interval=60.0
dx=8.0e3
dy=8.0e3
x_bnd = (-100e3, 100e3)
y_bnd = (-100e3, 100e3)

# # KOUN
# ctr_lat = 35.23833
# ctr_lon = -97.46028

# DC
ctr_lat =  38.889444
ctr_lon =  -77.035278


grid_h5flashfiles(h5_filenames, start_time, end_time, frame_interval=frame_interval, 
            dx=dx, dy=dy, x_bnd=x_bnd, y_bnd=y_bnd, ctr_lon=ctr_lon, ctr_lat=ctr_lat)