
median
==============================================

Purpose
----------------

Computes the medians of the columns of a matrix.

Format
----------------
.. function:: median(x)

    :param x: 
    :type x: NxK matrix

    :returns: m (*Kx1 vector*) containing the medians of the respective columns of x.

Remarks
-------

median will return a missing value for any column that contains a
missing value.


Examples
----------------

::

    //Set the seed for repeatable random data
    rndseed 4320993;
    
    //Create uniform random integers between 1 and 10
    x = ceil(10*rndu(100,3));
    
    //Calculate the median of each column of 'x'
    md = median(x);

After the code above, md is equal to:

::

    5.0000
    5.0000
    6.0000

Source
------

median.src

median matrix column
