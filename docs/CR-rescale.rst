
rescale
==============================================

Purpose
----------------
Scales the columns of a matrix

Format
----------------
.. function:: { x_s, location, scale_factor } = rescale(x, method)
              { x_s, location, scale_factor } = rescale(x, location, scale_factor)

    :param x: data to be rescaled
    :type x: NxK matrix or NxK array 

    :param location: used for column centering
    :type location: 1xK vector

    :param scale_factor: used for column scaling
    :type scale_factor: 1xK vector

    :param method: name of scaling and centering method:

        .. list-table::
            :widths: auto
            :header-rows: 1

            * - Method
              - Location
              - scale_factor
            * - "euclidean"
              - 0
              - Euclidean length: :math:`∑i=1nxi2`
            * - "mad"
              - Median
              - Absolute deviation from the median
            * - "maxabs"
              - 0
              - Maximum absolute value
            * - "midrange"
              - :math:`(Max+Min)/2`
              - :math:`Range/2`
            * - "range"
              - Minimum
              - Range
            * - "standardize"
              - Mean
              - Standard deviation
            * - "sum"
              - 0
              - Sum
            * - "ustd"
              - 0
              - Standard deviation about the origin

    :type method: string

    :return x_s: containing the scaled columns of *x*

    :type x_s: matrix or multi-dimensional array

    :return location: containing the values used to center the columns of the input matrix *x*

    :type location: 1xK vector

    :return scale_factor: containing the values used to scale the columns of the input matrix *x*

    :type scale_factor: 1xK vector

.. DANGER:: fix equations

Examples
----------------

Specifying a scaling method
+++++++++++++++++++++++++++

::

    // Create a column vector
    x = {   12.5,
            18.2,
            10.8,
             8.3,
            15.4,
            21.5,
            14.6,
            16.7 };
    
    // Standardize 'x' and return the location and scaling factors
    { x_s, location, scale_factor} = rescale(x, "standardize");
    				
    print "x_s = " x_s;				
    print "location = " location;				
    print "scale_factor = " scale_factor;

After the code above:

::

    x_s = 
    	-0.53463295 
    	 0.81977052 
    	-0.93857785 
    	 -1.5326145 
    	 0.15444952 
    	  1.6038989 
       -0.035642197 
    	 0.46334856 	
    				
    location =        14.750000 
    scale_factor =    4.2084948

Specifying a scaling method for multiple columns
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a matrix with 2 columns
    x = {   12.5 1088.5,
            18.2  879.3,
            10.8 1232.0,
             8.3 1189.8,
            15.4  932.1,
            21.5 1009.2,
            14.6  656.7,
            16.7 1251.5 };
    
    // Standardize 'x' and return the location and scaling factors
    { x_s, location, scale_factor } = rescale(x, "standardize");
    				
    print"x_s = " x_s;				
    print"location = " location;				
    print"scale_factor = " scale_factor;

After the code above:

::

    x_s = 
    	-0.53463295       0.28751716 
    	 0.81977052      -0.73869039 
    	-0.93857785       0.99144060 
    	 -1.5326145       0.78443315 
    	 0.15444952      -0.47968581 
    	  1.6038989      -0.10148025 
       -0.035642197       -1.8306302 
    	 0.46334856        1.0870957 
    								
    location =        14.750000        1029.8875 				
    scale_factor =    4.2084948        203.85740

Applying previously created location and scaling factors
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Continuing with the variables used in example 2, we can apply the returned location and 
scaling factors to standardize additional observations of our two variables.

::

    // Additional observations
    x_new = {  
    	 9.3  964.1,
    	10.9 1173.7,
    	11.1 1232.0,
    	 9.1 1051.2,
    	14.6 1124.1,
    	18.4  815.3,
    	20.2 1292.6,
    	18.5  833.1 };
    
    // Standardize 'x' using the location and scaling factors
    print"location = " location;				
    print"scale_factor = " scale_factor;
    								
    // returned in example 2
    x_new_s = rescale(x_new, location, scale_factor);
    				
    print"x_new_s = " x_new_s;				
    print"x_new = " x_new;

After the code above:

::

    location =        14.750000        1029.8875 
    scale_factor =    4.2084948        203.85740 
    
    x_new_s = 
    	 -1.2949998      -0.32271333 
    	-0.91481638       0.70545637 
    	-0.86729345       0.99144060 
    	 -1.3425227       0.10454612 
       -0.035642197       0.46214904 
    	 0.86729345       -1.0526353 
    	  1.2949998        1.2887072 
    	 0.89105492      -0.96531940 
    	
    x_new = 
    	  9.3000000        964.10000 
    	  10.900000        1173.7000 
    	  11.100000        1232.0000 
    	  9.1000000        1051.2000 
    	  14.600000        1124.1000 
    	  18.400000        815.30000 
    	  20.200000        1292.6000 
    	  18.500000        833.10000

.. seealso:: Functions `code`, :func:`recode`, :func:`reclassifyCuts`, :func:`reclassify`, :func:`rescale`, :func:`substute`

