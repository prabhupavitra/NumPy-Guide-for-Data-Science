# Importing numpy library
import numpy as np

# Arrays to demonstrate unary ufuncs
randomint_arr = np.random.randint(-20,20,size = (2,3,4))
randomfloat_arr = np.random.randn(2,5,4)


# Unary Ufuncs
""" 
>> ufuncs operate element by element on whole arrays.
>> ufuncs are highspeed because they are written in C.
Most common unary ufuncs include :
round, rint, fix, abs, absolute, fabs, sqrt, square, exp, exp2, log, log10, log2, 
logp, sign, ceil, floor, modf, isnan, isinfinte, isinf, cos, cosh, 
arccos, sin, sinh, arcsin, tan, tanh, arctan,logical_not
"""

# Round an array to the given number of decimals.
print(f'\n Round to 2 decimals = \n{np.round(randomfloat_arr,2)}')

# Round elements of the array to the nearest integer.
print(f'\n Round to nearest integer = \n{np.rint(randomfloat_arr)}')

# Round to nearest integer towards zero.
print(f'\n Round to nearest integer towards zero = \n{np.fix(randomfloat_arr,2)}')

# Computes the absolute value of a integer array; cannot handle complex values like a+ib
print(f'\nAbsolute value = \n{np.abs(randomint_arr)}')

# Calculates the absolute value for complex arrays too; absolute =  sqrt(a^2+b^2)
print(f'\nAbsolute value for complex numbers = \n{np.absolute(4+3j)}')

# Computes the absolute value of a floating point array
print(f'\nAbsolute value for floating point= \n{np.fabs(randomfloat_arr)}')

# Return the fractional and integral parts of an array, element-wise.
print(f'\n Fractional and integral parts =\n {np.modf(randomfloat_arr)}')

# Computes the Square root of the elements; sqrt of negative number gives nan
print(f'\nSquare root = \n{np.sqrt(np.abs((randomint_arr)))}')

# Computes the Square of the elements
print(f'\nSquare = \n{np.square(randomint_arr)}')

# Calculate the exponential of all elements in the input array.
print(f'\nExponential = \n{np.exp(randomint_arr)}')

# Calculate 2**p for all p in the input array.
print(f'\n 2**p = \n{np.exp2(np.array([1,2,3,4]))}')

# Return the natural logarithm of the input array, element-wise.
print(f'\nlog = \n{np.log(np.abs(randomint_arr))}')

# Return the base 10 logarithm of the input array, element-wise.
print(f'\nlog10 =\n {np.log10(np.abs(randomint_arr))}')

# Returns the Base-2 logarithm of x.
print(f'\nlog2=\n {np.log2(np.abs(randomint_arr))}')

# Returns the natural logarithm of one plus the input array, element-wise.
print(f'\nlog1p = \n{np.log1p(np.abs(randomint_arr))}')

# Returns an element-wise indication of the sign of a number.
print(f'\nSign of array elements =\n {np.sign(randomint_arr)}')

# Return the ceiling of the input, element-wise.
print(f'\n Ceiling of elements in array =\n {np.ceil(randomfloat_arr)}')

# Return the floor of the input, element-wise.
print(f'\n Floor of elements in array =\n {np.floor(randomfloat_arr)}')

# Returns the Trigonometric sine, element-wise.
print(f'\nsin(array) =\n {np.sin(randomint_arr)}')

# Returns the Hyperbolic sine, element-wise.
print(f'\nsinh(array) =\n {np.sinh(randomint_arr)}')

# Returns the Inverse sine, element-wise; 
print(f'\narcsin(array) =\n {np.arcsin(np.array([-1, 1, 0]))}')

# Returns the Trigonometric cosine, element-wise.
print(f'\ncos(array) =\n {np.cos(randomint_arr)}')

# Returns the Hyperbolic cosine, element-wise.
print(f'\ncosh(array) =\n {np.cosh(randomint_arr)}')

# Returns the Inverse cosine, element-wise; 
print(f'\narccos(array) =\n {np.arccos(np.array([-1, 1, 0]))}')

# Returns the Trigonometric sine, element-wise.
print(f'\ntan(array) =\n {np.tan(randomint_arr)}')

# Returns the Hyperbolic tan, element-wise.
print(f'\ntanh(array) =\n {np.tanh(randomint_arr)}')

# Returns the Inverse tan, element-wise; 
print(f'\narctan(array) =\n {np.arctan(np.array([-1, 1, 0]))}')



# Creating an array with nan and inf
arr_naninf = np.array([[np.inf,np.nan,np.NaN],
                       [np.NAN,33,0],
                       [5/np.inf,np.inf*np.nan,np.inf/np.inf]])

print(f'\nOriginal array = \n{arr_naninf}')

# Test element-wise for NaN and return result as a boolean array.
print(f'\n Boolean array checking for nan =\n {np.isnan(arr_naninf)}')

# Test element-wise for inf and return result as a boolean array.
print(f'\n Boolean array checking for inf =\n {np.isinf(arr_naninf)}')

# Test element-wise for finiteness (not infinity or not Not a Number).
print(f'\n Boolean array checking for finiteness =\n {np.isfinite(arr_naninf)}')

# Some concepts regarding NaN and inf

# nan is never equal to nan; result of nan==nan is always false
print("nan==nan ? {}".format(np.nan==np.nan))

# inf is equal to inf;
print("inf==inf ? {}".format(np.inf==np.inf))

# np.any on NaN, positive infinity and negative infinity evaluate to True 
print(f"np.any(np.NaN) is {np.any(np.NaN)}")
print(f"np.any(+np.inf) is {np.any(+np.inf)}")
print(f"np.any(-np.inf) is {np.any(-np.inf)}")

# np.all is True if all elements over the axis chosen in True
# np.all performs a logical AND between elements on the axis chosen
print(f"\nnp.all(arr_naninf,axis=0) = \n{np.all(arr_naninf,axis=0)}")
print(f"\narr_naninf.all(axis=1) = \n{arr_naninf.all(axis=1)}")



# Binary universal functions
"""
Since these operators always result in a boolean array, we can use 
these ufuncs to do element-wise comparisons over arrays.
We can use the  operators or their equivalent ufunc for 
accomplishing the task.
For instance, Operator "+" is same as "np.add".
"""
# Arrays to demonstrate binary ufuncs that utilize mathematical operations
arr_x = np.round(np.random.randn(2,3,4),2)
arr_y = np.random.randint(10,size=(2,3,4))

# Mathematical Operators
# Add arguments element-wise.
print(f'\nSum = \n{np.add(arr_x,arr_y)}')
print(f'\nSum = \n{arr_x+arr_y}')

# Subtracts arguments element-wise.
print(f'\nDifference = \n{np.subtract(arr_x,arr_y)}')
print(f'\nDifference = \n{arr_x-arr_y}')

# Multiply arguments element-wise.
print(f'\nProduct = \n{np.multiply(arr_x,arr_y)}')
print(f'\nProduct = \n{arr_x*arr_y}')

# Returns a true division of the inputs, element-wise.
print(f'\n Result of True Divison = \n{np.divide(arr_x,arr_y)}')
print(f'\n Result of True Divison = \n{np.true_divide(arr_x,arr_y)}')
print(f'\n Result of True Divison = \n{arr_x/arr_y}')

# Return element-wise remainder of division.
print(f'\n Remainder of True Divison = \n{np.mod(arr_x,arr_y)}')
print(f'\n Remainder of True Divison = \n{np.remainder(arr_x,arr_y)}')
print(f'\n Remainder of True Divison = \n{arr_x%arr_y}')

# Return element-wise quotient and remainder simultaneously.
# print(f'\n Quotient, Remainder = \n{np.divmod(arr_x,arr_y)}')

# Return the largest integer smaller or equal to the division of the inputs. 
print(f'\n Result of Floor Divison = \n{arr_x//arr_y}')
print(f'\n Result of Floor Divison = \n{np.floor_divide(arr_x,arr_y)}')

# First array elements raised to powers from second array, element-wise.
print(f'\n arr_y to the power of arr_x = \n{np.power(arr_y,arr_x)}')
print(f'\n arr_y to the power of arr_x = \n{arr_y**arr_x}')

# Element-wise maximum of array elements.
print(f'\nmaximum of arrays  = \n{np.maximum(arr_y,arr_x)}')

# Element-wise minimum of array elements.
print(f'\nminimum of arrays  = \n{np.minimum(arr_y,arr_x)}')

# Change the sign of x1 to that of x2, element-wise.
print(f'\n Changes sign of array 1 to that of 2  = \n{np.copysign(arr_x,arr_y)}')




# Comparison Operators
"""
Comparison operators discussed here include :
equal, less_equal, less, greater_equal, greater
array_equiv, array_equal
"""
# Arrays to demonstrate binary ufuncs that utilize comparison operations
arr_x1 = np.arange(10)
arr_x2 = np.array([0,1,5,3,2,5,6,8,8,9])
arr_x3 = np.tile(arr_x1,(3,4,1))


# Return (x1 == x2) element-wise; x1 and x2 need not have same datatype
# x1 and x2 are arrays
print(f'\n Boolean array checking for equality  = \n{np.equal(arr_x1,arr_x2)}')
print(f'\n Boolean array checking for equality  = \n{arr_x1==arr_x2}')
# x1 is of "int" type and x2 is an array
print(f'\n Boolean array checking for equality  = \n{8==arr_x2}')
print(f'\n Boolean array checking for equality  = \n{np.equal(8,arr_x2)}')

# Return the truth value of (x1 =< x2) element-wise.
# x1 and x2 are arrays
print(f'\n Boolean array checking if 1st array =< 2nd array  = \n{np.less_equal(arr_x1,arr_x2)}')
print(f'\n Boolean array checking if 1st array =< 2nd array  = \n{arr_x1<=arr_x2}')
# x1 is an array and x2 is of "int" type 
print(f'\n Boolean array checking if 1st array =< 2nd element  = \n{np.less_equal(arr_x2,5)}')
print(f'\n Boolean array checking if 1st array =< 2nd element  = \n{arr_x2<=5}')

# Return the truth value of (x1 < x2) element-wise.
# x1 and x2 are arrays
print(f'\n Boolean array checking if 1st array < 2nd array  = \n{np.less(arr_x1,arr_x2)}')
print(f'\n Boolean array checking if 1st array < 2nd array  = \n{arr_x1<arr_x2}')
# x1 is an array and x2 is of "int" type 
print(f'\n Boolean array checking if 1st array < 2nd element  = \n{np.less(arr_x2,5)}')
print(f'\n Boolean array checking if 1st array < 2nd element  = \n{arr_x2<5}')

# Return the truth value of (x1 >= x2) element-wise.
# x1 and x2 are arrays
print(f'\n Boolean array checking if 1st array >= 2nd array  = \n{np.greater_equal(arr_x1,arr_x2)}')
print(f'\n Boolean array checking if 1st array >= 2nd array  = \n{arr_x1>=arr_x2}')
# x1 is an array and x2 is of "int" type 
print(f'\n Boolean array checking if 1st array >= 2nd element  = \n{np.greater_equal(arr_x2,5)}')
print(f'\n Boolean array checking if 1st array >= 2nd element  = \n{arr_x2>=5}')

# Return the truth value of (x1 > x2) element-wise.
# x1 and x2 are arrays
print(f'\n Boolean array checking if 1st array > 2nd array  = \n{np.greater(arr_x1,arr_x2)}')
print(f'\n Boolean array checking if 1st array > 2nd array  = \n{arr_x1>arr_x2}')
# x1 is an array and x2 is of "int" type 
print(f'\n Boolean array checking if 1st array > 2nd element  = \n{np.greater(arr_x2,5)}')
print(f'\n Boolean array checking if 1st array > 2nd element  = \n{arr_x2>5}')

# Returns True if input arrays are shape consistent and all elements equal.
print(f'\n Consistency in Shape and elements :{np.array_equiv(arr_x1,arr_x2)}')
# Returns True even if one of the arrays are broadcastable
print(f'\n Consistency in Shape and elements :{np.array_equiv(arr_x1,arr_x3)}')

# True if two arrays have the same shape and elements, False otherwise.
print(f'\n Equality in Shape and elements :{np.array_equal(arr_x1,arr_x2)}')
# Returns False even if one of them is broadcastable 
print(f'\n Equality in Shape and elements :{np.array_equal(arr_x1,arr_x3)}')



# Logical Operands - Element-wise 
# Compute the truth value of x1 XOR x2, element-wise; True only when one of the conditions is True
print(f'\n Boolean array checking for arr_x2 is either 5 or 8 : {np.logical_xor(arr_x2==5,arr_x2==8)}')

# Compute the truth value of x1 AND x2 element-wise; both conditions should hold 
print(f'\n Boolean array checking for 1<= arr_x1 <=5 : \n{np.logical_and(arr_x1>=1,arr_x2<=5)}')

# Compute the truth value of x1 OR x2 element-wise; atleast one of the conditions should hold
print(f'\n Boolean array checking for elements in arr_x2>5 or arr_x2==0 : \n{np.logical_or(arr_x2==0,arr_x2>5)}')

# Compute the truth value of x1 NOT x2 element-wise.
print(f'\n Boolean array returning NOT(array): \n{np.logical_not(arr_x2==0)}')





# ufunc special methods
"""
All binary ufuncs support four methods for performing specialized functions.
>> reduce
>> accumulate
>> reduceat
>> outer
"""

# Array creation
arr_multidim = np.random.randint(9,size=(2,4,2,6))

# Reduces array’s dimension by one, by applying ufunc along one axis.
np.add.reduce(arr_multidim,axis=2,initial=10)
# Keyword "initial" lets you initialize the 

# Accumulate the result of applying the operator to all elements.
np.add.accumulate(arr_multidim,axis=2)

# Performs a (local) reduce with specified slices over a single axis;
"""
np.ufunc.reduceat : Reduces contiguous slices of data to produce aggregated array
Format            : np.ufunc.reduceat(array,indices,axis,dtype,none)

For example : For i in range(length(indices)),reductions are performed on the contiguous slices of data
i < i+1 ; slice is i:(i+1) where (i+1) is a exclusive outerbound
i >= i+1; slice is i
i >= length(array) or i<0; raises an error
"""
np.add.reduceat(arr_multidim,[0,4,5,2,4,1],axis=3)
# Slices : [0:4],[4:5],[5],[2:4],[4],[1+]'


# Apply the ufunc operation to all pairs for every a in A and b in B
"""
np.ufunc.outer : Applies ufunc operation to every pair; Resulting array has shape A.shape + B.shape
Format         : np.ufunc.outer(array_A,arr_B)   
If shape of array A is (x,y) and B is (l,m,n) ; resulting array will have shape (x,y,l,m,n)
"""
np.add.outer(arr_multidim[0,0,0],arr_multidim[0,1])
# Shape of resulting array is (6,2,6)



# Broadcasting
"""
Broadcasting is a set of rules for applying binary UFuncs on arrays of different sizes.

Rules of Broadcasting : 

1. Rule 1 : If the 2 arrays differ in dimensions, the shape of the one with fewer dimensions is padded with 1s on its leading side
2. Rule 2 : If the shape of the 2 arrays does not match in any dimension, tha array with shape equal to 1 is stretched to match the other shape
3. Rule 3 : If neither sizes match in any dimension nor is 1, then an error is raised
"""

arr_brdcst1 = np.random.randint(40,size=(2,4,2,1))
arr_brdcst2 = np.random.randint(20,size=(2,3))
arr_brdcst3 = np.random.randint(20,size=(2,3,5))

arr_viable = arr_brdcst1 + arr_brdcst2 
# Rule 1 : Smaller array arr_brdcst2 padded with 1s on left making its dimensions (1,1,2,3)
# Rule 2 : Due to dimension mismatch, both arr_brdcst1 and arr_brdcst2 are stretched/broadcasted 
arr_viable.shape
# Forms an output array of dimensions (2,4,2,3)


arr_error_brdcst = arr_brdcst1 + arr_brdcst3
# Raises an error : operands could not be broadcast together with shapes (2,4,2,1) (2,3,5) 
