
squeeze
==============================================

Purpose
----------------
Remove any singleton dimensions from a multi-dimensional array.

Format
----------------
.. function:: squeeze(a)

    :param a: 
    :type a: Multi-dimensional array

    :returns: atrim (*TODO*), Multidimensional array or matrix with all dimensions
        equal to 1 removed.

Examples
----------------

::

    //Set seed for repeatable random numbers
    rndseed 431234;
    
    x = rndn(8,1);
    
    //Create 3 dimensional (2x1x4) array with 1 singleton dimension
    a = areshape(x, 2|1|4);
    
    //Create a 2x4 matrix 'x_2' from the 2x1x4 array 'a'
    x_2 = squeeze(a);

After the above code:

::

    a =     [1,.,.]
                 -0.94527  -0.07985  0.88879  -1.0082
    
            [2,.,.]
                 -0.45845   0.77882 -0.36897  0.78537
    
    x_2 =        -0.94527  -0.07985  0.88879  -1.0082
                 -0.45845   0.77882 -0.36897  0.78537

.. seealso:: Functions :func:`areshape`, :func:`atranspose`
