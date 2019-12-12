# Load the libraries
import numpy as np


# Creating arrays 
# Method 1 : From a list/tuple
arr_list = np.array([[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]],
                    [[13,14,15,16],
                     [17,18,19,20],
                     [21,22,23,24]]],dtype="int32")

print(f'Numpy array from a list :\n{arr_list}')   


# Method 2 : From Built-in routines

print(f"\n Using np.ones to create an array : \
\n{np.ones((3,2),dtype=float)}") 

print(f"\n Using np.zeros to create an array : \
\n{np.zeros((4,3),dtype=int)}") 

print(f"\n Using np.full to create an array : \
\n{np.full((3,4,5),0.34)}") 

# Uses numerical range built-in functions

print(f'\n Using np.arange with step of 5 to create ndarray : \
\n{np.arange(25,40,5)}')

print(f'\n Using np.linspace with equally spaced elements to create ndarray : \
\n{np.linspace(25,40,4)}')

# Uses np.random 
print(f'\n Using np.random.rand to create a uniform random array : \
\n{np.random.rand(2,4)}')

print(f'\n Using np.random.randn to create a normal random array : \
\n{np.random.randn(2,4)}')

print(f'\n Using np.random.normal to create a  \
random array of float in given interval : \
\n{np.random.normal(-15,15,(2,3,4))}')

print(f'\n Using np.random.randint to create a  \
random array of integers in given interval : \
\n{np.random.randint(25,75,(2,3,4))}')

# Uses np.eye
print(f'\n Using np.eye to create a matrix with kth diagonal \
elements set to 1 and others as 0: \
\n{np.eye(4,k=1)}')




# Loading files(txt,csv) to form numpy arrays 

# 1. Using np.fromfile
np.random.rand(2,10000).tofile("/Users/pavitragajanana/development/5. InternalFiles/randomtext")
# Reading the file using fromfile
randtext = np.fromfile("/Users/pavitragajanana/development/5. InternalFiles/randomtext")


# 2. Using np.genfromtxt
datafile_genfromtxt = np.genfromtxt("/Users/pavitragajanana/development/2. Data Files/CrudeOil_Daily_Cushing_OK_WTI_Spot_Price_FOB.csv",
                                    usecols=[1],
                                    delimiter=",",
                                    skip_header=1)


# 3. Loading csv files into numpy array using np.loadtxt
datafile_arr = np.loadtxt("/Users/pavitragajanana/development/2. Data Files/CrudeOil_Daily_Cushing_OK_WTI_Spot_Price_FOB.csv",
                          delimiter=",",
                          skiprows=1, # Header
                          usecols=[1]) 


# 4. Using csv library
import csv
from datetime import datetime

with open("/Users/pavitragajanana/development/2. Data Files/CrudeOil_Daily_Cushing_OK_WTI_Spot_Price_FOB.csv", 'r') as f:
    datafile = list(csv.reader(f, delimiter=","))

# Converts the list to an ndarray
datafile = np.array(datafile)
# Converts into default datetime format
datearray = np.array([datetime.strptime(x, "%m/%d/%y").strftime('%Y-%m-%d') for x in datafile[1:,0]])
nominal = datafile[1:,1]

# Recreates original array
datafile = np.vstack([datearray,nominal]).T




# Array Attributes (size,shape,ndim,nbytes,itemsize,dtype) 

# We create a 1D, 2D and a 3D array to explore the attributes
# One-Dimensional Array
one_dim_array = np.random.randint(12, size=7)

# Two-Dimensional Array
two_dim_array = np.array([["Cupcake","Donut"],
                   ["Eclair","Froyo"],
                   ["Gingerbread","Honeycomb"],
                   ["Ice Cream Sandwich","Jelly Bean"],
                   ["KitKat","Lollipop"],
                   ["Marshmallow","Nougat"],
                   ["Oreo","Pie"]])

# Three-Dimensional Array
three_dim_array = np.array([[["Civic","Accord","Pilot","FR-V"],
                       ["Odyssey","Jazz","CR-V","NSX"]],
                      [["Insight","Ridgeline","Legend","HR-V"],
                       ["Passport","S660","Clarity","Mobilio"]],
                      [["Airwave","Avancier","Beat","Shuttle"],
                       ["Concerto","Element","Logo","Stream"]]])

# Array Attributes for 1D array
print(f'Dimensions of 1D array : {one_dim_array.ndim}')
print(f'Size of 1D array : {one_dim_array.size}')
print(f'Shape of 1D array : {one_dim_array.shape}')
print(f'Total Bytes consumed by 1D array : {one_dim_array.nbytes}')
print(f'dtype of 1D array : {one_dim_array.dtype}')
print(f'Itemsize of 1D array : {one_dim_array.itemsize}')

# Array Attributes for 2D array
print(f'Dimensions of 2D array : {two_dim_array.ndim}')
print(f'Size of 2D array : {two_dim_array.size}')
print(f'Shape of 2D array : {two_dim_array.shape}')
print(f'Total Bytes consumed by 2D array : {two_dim_array.nbytes}')
print(f'dtype of 2D array : {two_dim_array.dtype}')
print(f'Itemsize of 2D array : {two_dim_array.itemsize}')

# Array Attributes for 3D array
print(f'Dimensions of 3D array : {three_dim_array.ndim}')
print(f'Size of 3D array : {three_dim_array.size}')
print(f'Shape of 3D array : {three_dim_array.shape}')
print(f'Total Bytes consumed by 3D array : {three_dim_array.nbytes}')
print(f'dtype of 3D array : {three_dim_array.dtype}')
print(f'Itemsize of 3D array : {three_dim_array.itemsize}')
