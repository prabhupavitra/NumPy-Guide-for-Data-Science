# Importing required libraries
import numpy as np
from datetime import datetime 
import matplotlib.pylab as plt

# Creating 1D, 2D and 3D arrays
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



# Array Indexing 
# 1D Array Indexing
print("Original 1D array :\n{}\n".format(one_dim_array))
print(f'9th item can be indexed by one_dim_array[4]: {one_dim_array[4]}')
print(f'one_dim_array[-3]: {one_dim_array[-3]}')

# 2D Array Indexing
print("Original 2D array :\n{}\n".format(two_dim_array))
print(f'5th row,2nd column can be indexed by two_dim_array[4,1]: {two_dim_array[4,1]}')
print(f'Using Negative indexing, two_dim_array[-3,-1]: {two_dim_array[-3,-1]}')

# 3D Array Indexing
print("Original 3D array :\n{}\n".format(three_dim_array))
print(f'2nd slab, 1st row, 3rd column can be indexed by three_dim_array[1,0,2]: {three_dim_array[1,0,2]}')
print(f'Using Negative indexing, three_dim_array[-2,-2,-2]: {three_dim_array[-2,-2,-2]}')




# Array Slicing 
# 1D Array Slicing (Format -> start:stop:step)
print("Original 1D array :\n{}\n".format(one_dim_array))

# Some common examples of 1D array slicing; Starting at 0 and stop is exclusive
print(f"First 3 elements :{one_dim_array[:3]}")

print(f"Last 4 elements :{one_dim_array[-4:]}")

print(f"Elements from 2,3,4,5 :{one_dim_array[2:6]}")

print(f"Alternating Elements 1,3,5  :{one_dim_array[0:6:2]}")

print(f"Reversed array :{one_dim_array[::-1]}")

# 2D Array Slicing
print("Original 2D array :\n{}\n".format(two_dim_array))

print(f"Second column elements :\n{two_dim_array[:,1:]}")
# print(f"Second column elements :\n{two_dim_array[:,-1:]}")

print(f"Fourth row elements :\n{two_dim_array[3:4,:]}")
print(f"Fourth row elements till end of array :\n{two_dim_array[3:,:]}")

print(f"Alternating even rows :\n{two_dim_array[::2,:]}")
print(f"Alternating odd rows :\n{two_dim_array[1::2,:]}")

print(f"Reversed array :\n{two_dim_array[::-1,::-1]}")

# 3D Array Slicing
print("Original 3D array :\n{}\n".format(three_dim_array))

print(f"Alternating slabs :\n{three_dim_array[::2,:,:]}")
print(f"Alternating odd rows of all slabs  :\n{three_dim_array[::,1::2,:]}")
print(f"Alternating odd columns of all slabs  :\n{three_dim_array[::,::,::2]}")

# Negative Indexing
print(f"Alternating slabs :\n{three_dim_array[-3::2,:,:]}")
print(f"Alternating odd rows of all slabs  :\n{three_dim_array[::,-1::2,:]}")
print(f"Alternating odd columns of all slabs  :\n{three_dim_array[::,::,::-2]}")

# Reversed
print(f"Reversed 3D array :\n{three_dim_array[::-1,::-1,::-1]}")




# Creating Copies of Arrays

# Case 1 : Using "=" sign to create a reference of the original array
ref_two_dim_array =  two_dim_array[:,:]

# Changing value of one of the array elements will change original array
ref_two_dim_array[3,0] = "Pie Android"
# All cell values are True; Changing value of referenced array changed the original array
ref_two_dim_array == two_dim_array 

# Reinitializing Original array
two_dim_array = np.array([["Cupcake","Donut"],
                          ["Eclair","Froyo"],
                          ["Gingerbread","Honeycomb"],
                          ["Ice Cream Sandwich","Jelly Bean"],
                          ["KitKat","Lollipop"],
                          ["Marshmallow","Nougat"],
                          ["Oreo","Pie"]])

# Case 2 :Creating copy of the array using copy()
copy_two_dim_array = two_dim_array[:,:].copy()
copy_two_dim_array[3,0] = "Pie Android"
# Created a copy and hence the original array did not change
copy_two_dim_array == two_dim_array 



# Reshaping Arrays 

"""
>> Using reshape function 
>> Raveling and Flattening : Collapsing a multi-dim array to 1D array
>> Adding dimensions to an array using np.newaxis
>> Repeating elements or as tiles 
>> Joining Arrays using concatenate, stack, vstack, hstack and dstack
>> Permuting Dimensions of arrays
>> Swapping Axes of an array using transpose
>> Splitting Arrays using split, vsplit, hsplit and dsplit
>> Finding array Diagonals using np.diagonal
"""
# Lets consider a Random 3D integer array
threedim_arr = np.random.randint(1,50,(3,4,5))

# Using reshape() to change the shape of the array
threedim_arr.reshape(5,1,12)


# Raveling 
"""
Raveling : Returns a contiguous flattened array; 
Default order 'C'(Also called Column Major which means it will Traverse Higher dimension first)
Order 'F' (Also called Row Major which means Traverses higher dimensions last)
>> It is a library-level function
>> Creates a reference/view of original array ; Faster than flatten
"""
# Using ravel() ; Default order 'C' : 
threedim_arr.ravel() # Uses default order of 'C'
threedim_arr.ravel('F') # axis 0 before advancing on axis 1


# Flattening 
"""
Flattening : Same as Raveling other than those listed below,
>> ndarray object method
>> It creates copy of original and thus occupies memory; hence slower 
"""
# Using flatten() 
threedim_arr.flatten()
threedim_arr.flatten('F')


# Adding dimensions to an array
# Reshapes array of (x,y,z) shape to (1,x,y,z)
print(f'\n\tShape of array threedim_arr[np.newaxis,:].shape : {threedim_arr[np.newaxis,:].shape}')

# Reshapes array of (x,y,z) shape to (x,1,y,z)
print(f'\n\tShape of array threedim_arr[:,np.newaxis].shape : {threedim_arr[:,np.newaxis].shape}')

# Repeating individual elements and tiles

# Repeating Individual elements
threedim_arr.repeat(2)  # Repeats elements twice and array is flattened

threedim_arr.repeat(2,axis=0) # Repeats slabs twice

# Repeating whole array or rows/columns/slabs without collapsing structure

# Repeats over axis 2
threedim_arr.repeat(2,axis=2) 

# Repeats slabs; For a 3D array of shape (3,y,z)
threedim_arr.repeat([1,2,3],axis=0) 

# Repeats rows; For a 3D array of shape (x,4,z)
threedim_arr.repeat([1,2,3,4],axis=1)

# Repeats columns ; For a 3D array of shape (x,y,5)
threedim_arr.repeat([1,2,3,4,5],axis=2) 


# Repeating Specified array as a tile using np.tile(array,reps) 

# Case 1: When Array dim is greater than reps dim
np.tile(threedim_arr,2)
# is same as np.tile(threedim_arr,(1,1,1,2))

np.tile(threedim_arr,(2,2)) 
# is same as np.tile(threedim_arr,(1,2,2))

np.tile(threedim_arr,(1,2))
# is same as np.tile(threedim_arr,(1,1,2))

# Case 2: When reps dim is greater than array dim; arr is promoted to 2D
np.tile(np.array([1,2,3]),(2,3))
# is same as np.tile(np.array([[1,2,3]]),(2,3))



# Concatenating arrays using np.concatenate

# Concatenating a 1D array
print(f'\nConcatenating 1D arrays: \
      {np.concatenate((np.ones(4),np.zeros(3)))}')

# Concatenating a 2D array
# For more info please visit : https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.dtypes.html

# Lets load a datafile of Crude oil prices and the date on which it was recorded
# Use the path of your dataset
arr_one = np.loadtxt("/Users/pavitragajanana/development/2. Data Files/CrudeOil_Daily_Cushing_OK_WTI_Spot_Price_FOB.csv",
                         dtype={'names':('Day','WTISpotPrice'),
                                'formats':('<U12','f4')},
                         delimiter=",",
                         skiprows=1, # Header
                         usecols=(0,1)) 
                        # unpack=True   

# Convert into an ndarray and parsing "Day" to datetime format
arr_one = np.array([[day,nominal] for (day,nominal) in arr_one])
arr_two = np.array([datetime.strptime(x, "%m/%d/%y").strftime('%Y-%m-%d') for x in arr_one[:,0]])

# Concatenating a 2D array with a 1D array of similar shape except for concatenating axis
concat_arr = np.concatenate([arr_one,arr_two[:,np.newaxis]],axis=1)


# Using stack,vstack,hstack and dstack

# Using vstack ; which will stack row-wise i.e. concatenate with axis 0 
concat_vstack = np.vstack([arr_one.T,arr_two[np.newaxis,:]]).T
# is same as np.stack([arr_one,arr_two],axis=0)

# Using hstack ; which stacks column-wise  i.e. concatenate with axis 1
concat_hstack = np.hstack([arr_one,arr_two[:,np.newaxis]])

# Using dstack ; which stacks depth-wise  i.e. concatenate with axis 2
concat_dstack = np.dstack([arr_one[:,0],arr_two,arr_one[:,1]])

# 3D array
# Lets load an image to work with 3D array
img_arr = plt.imread("/Users/pavitragajanana/development/5. InternalFiles/Image1.jpg")
img_dup = img_arr.copy()
np.concatenate([img_arr,img_arr],axis=0)



## Transposing arrays
"""
An array with shape (w,x,y,z) will have a shape (z,y,x,w) when transposed
"""
threedim_arr.T 


## Axes Swapping using transpose()
""" For higher dimensional arrays, transpose will accept 
a tuple of axis numbers to permute the dimensions of the array """
# Original Array has shape (0,1,2)
# Transpose (2,1,0) has the same shape as threedim_arr.T
threedim_arr.transpose((2,1,0)) 

# Useful for permuting the axes for higher dimensional arrays
threedim_arr.transpose((1,2,0))


## Splitting arrays
"""Split an array into multiple sub-arrays
>> np.split
>> np.hsplit is same as np.split(axis=1)
>> np.vsplit is same as np.split(axis=0)
>> np.dsplit is same as np.split
"""
# Lets create a 3D array
periodic_table = np.array([[["Hydrogen","Helium","Lithium","Beryllium"],
                            ["Boron","Carbon","Nitrogen","Oxygen"],
                            ["Flourine","Neon","Sodium","Magnesium"]],

                          [["Aluminium","Silicon","Phosphorus","Sulfur"],
                           ["Chlorine","Argon","Potassium","Calcium"],
                           ["Scandium","Titanium","Vanadium","Chromium"]],
                         
                           [["Manganese","Iron","Cobalt","Nickel"],
                            ["Copper","Zinc","Gallium","Germanium"],
                            ["Arsenic","Selenium","Bromine","Krypton"]]])

# Using split,vsplit,hsplit and dsplit
# np.vsplit splits array along axis 0
print(f'{np.vsplit(periodic_table,[1,2])}')
print(f'{np.split(periodic_table,[1,2],axis=0)}')


# np.hsplit splits array along axis 1
print(f'{np.hsplit(periodic_table,[1,2])}')
print(f'{np.split(periodic_table,[1,2],axis=1)}')

# np.dsplit splits array along axis 2
print(f'{np.dsplit(periodic_table,[2])}')
print(f'{np.split(periodic_table,[2],axis=2)}')


# Finds the diagonal elements of an array; np.diagonal(offset,axis1,axis2)
"""
a(i,i) gives diagonal elements of an array; offset is applied on axis 2
For higher dimensions, 2D subarray is made of axis 1 and 2 passed in the input
a(i,i+offset) offsets diagonal elements on axis 2;
"""
arr_diagonal = np.arange(48).reshape(4,3,4)
print(f'Original array :\n {arr_diagonal}')

 
# Diagonal array with axis 2 and axis 0; offsetting axis 0 by 1
# [(1,0)(2,1)(3,2)] for each of the axis 1 rows
print(f'\nDiagonal array :\n\n{arr_diagonal.diagonal(1,2,0)} ')
