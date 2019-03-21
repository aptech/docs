
missex
==============================================

Purpose
----------------

Converts numeric values to the missing value code according to the values given in a logical
expression.

Format
----------------
.. function:: missex(x, mask)

    :param x: 
    :type x: NxK matrix

    :param mask: 
    :type mask: NxK logical matrix (matrix of 0's and 1's) that serves as a "mask" for x; the 1's in mask correspond to the values in x that are to be
        converted into missing values

    :returns: y (*NxK matrix that equals x*), but with those
        elements that correspond to the 1's in  e converted to missing.

Examples
----------------

::

    //Set seed for repeatable random numbers
    
    rndseed 49728424;
    
    x = rndu(3,2);
    
    //Logical expression
    mask =(x .> .30) .and (x .< .60);
    y = missex(x,mask);

After the code above:

::

    0.525  0.419          1  1           .      . 
    x =  0.869  0.973   mask = 0  0   y = 0.869  0.973 
         0.021  0.357          0  1       0.021      .

A 3x2 matrix of uniform random numbers is created.
All values in the interval (0.30, 0.60) are converted
to missing.

Source
++++++

datatran.src

.. seealso:: Functions :func:`miss`, :func:`missrv`
