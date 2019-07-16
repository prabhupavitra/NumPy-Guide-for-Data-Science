# NumPy-Guide-for-Data-Science
A Hands-On NumPy Tutorial for Data Scientists

    NumPy, short for Numerical Python, is one of the indispensable foundational packages for scientific 
		computing in Python. At the core of NumPy is, ndarray, an efficient multidimensional array that is 
		a container of homogeneous data. 
		It is predominantly used in a majority of tasks in the data science ecosystem and is the fundamental 
		package for scientific computing with Python.

    Its key features include:

    - Provides efficient data storage compared to the built-in python sequences since NumPy internally 
		  stores data in a contiguous block of memory.

    - Operations are efficient whether it’s for complex computations or as the arrays grow larger in size 
		  since it does not need "for" loops.

    - It provides an abundance of functions for mathematical, logical, matrix manipulation, discrete Fourier 
		  transforms, basic linear algebra, basic statistical operations, random simulation, sorting, I/O and 
			various other computations.

     This Hands-on NumPy tutorial covers all the core aspects of NumPy and the features one needs to know, 
		 as a beginner in Data science. 

    For usability reasons, this tutorial is divided into three sections.
    The following list of contents is a walk-through of NumPy features discussed in this tutorial:

    1.	Basics of NumPy 
        This notebook gives an overview of basic concepts of NumPy.
          -	NumPy Installation
          -	NumPy Array Creation
          -	NumPy Array Attributes
          -	NumPy Array Manipulation 
        	 (includes simple array indexing, array slicing, creating copies of    
          	arrays, reshaping arrays, raveling arrays, flattening arrays, concatenating arrays, 
						splitting arrays, repeating elements in arrays)

    2.	NumPy Vectorized Computations
        This notebook introduces concepts of vectorization, implemented through NumPy’s universal functions 
				that enables NumPy to make repeated calculations on array elements much more efficient. Ufuncs perform 
				Element-Wise operations on data in ndarrays. It’s important to note that ufuncs can return multiple arrays
				(E.g. divmod) although less frequently used.
          -	Unary ufuncs
          -	Unary ufuncs for nan
          -	Binary ufuncs
          -	Broadcasting

    3.	Other NumPy Essentials
        This notebook introduces concepts of fancy indexing, sorting, aggregations, masking, set operations 
				and various others that demonstrates the computational efficiency of NumPy in the data science world.
          -	Fancy Indexing
          -	Sorting Arrays
          -	Aggregations**
          -	Set Operations**
            
    **explained using real world datasets from energy markets and finance
  
    References:

    1.	NumPy Documentation: https://docs.scipy.org/doc/numpy/reference/#
    2.	McKinney, Wes (2017). Python for Data Analysis (2nd ed.). 
    3.	VanderPlas, Jake (2016). Python Data Science Handbook.
