import sys
import glob
import os, platform
import os.path
import re
import operator

from os import path
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
from collections import Counter
import subprocess
from datetime import datetime

# Extract the ISPs from the nc files in input directory. Generates a same-name with isp extension in output dir (auto generated).
sys.path.append('./input/')

# Generate output folder if not exists
if not os.path.exists('output'):
    os.makedirs('output')

# Generate the ISP files
os.chdir("./input/")
for file in glob.glob("*.nc"):
    print("### Processing file: "+file+" ###")
    nc = Dataset(file)
    tm_packets = nc.groups['data'].variables['tm_packets']

    print(tm_packets)

    f = open("../output/"+file+".isp", "wb")
    for item in tm_packets:
        f.write(item)
    f.close()
    print("### Done ###\n")
    
    