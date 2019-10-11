
sampleData
==============================================

Purpose
----------------

Returns a sample of the rows of a matrix, chosen with or without replacement

Format
----------------
.. function:: s = sampleData(x, size[, replace])

    :param x: population from which to take a sample
    :type x: matrix

    :param size: the requested sample size
    :type size: scalar

    :param replace: Optional argument, if *replace* is 0, the sample is drawn without replacement. If *replace* is 1, the sample is drawn with replacement. Default is 0.
    :type replace: scalar

    :return s: containing the sample taken from *x*.

    :rtype s: size x cols(x) matrix

Examples
----------------

Basic example without replacement
+++++++++++++++++++++++++++++++++

::

    // Set seed for repeatable random draws
    rndseed  23423;
    
    // Create a 7x1 vector
    x  = { 1,
           2,
           3,
           4,
           5,
           6,
           7 };
    
    // Take a sample of 3 elements without replacement
    s  = sampleData(x, 3);

After running the code above, *s* is equal to:

::

    5
    3
    7

Basic example with replacement
++++++++++++++++++++++++++++++

::

    // Set seed for repeatable random draws
    rndseed  23423;
    
    // Create a 7x2 vector
    x  = { 1.2 1.8,
           2.7 2.1,
           3.0 3.3,
           4.8 4.1,
           5.1 5.4,
           6.0 2.8,
           7.2 3.9 };
    
    replace = 1;
    
    // Take a sample of 5 rows of 'x' with replacement
    sample = sampleData(x, 5, replace);

After running the code above, sample is equal to:

::

    5.1    5.4 
    3.0    3.3 
    6.0    2.8 
    4.8    4.1 
    3.0    3.3

Remarks
-------

Indices for taking a random sample can be created with GAUSS function
rndi.

The random number generator used in :func:`sampleData` to choose the samples is
automatically seeded using the system clock when GAUSS first starts.
However, that can be overridden using the `rndseed` statement.

.. seealso:: Functions :func:`rndi`, :func:`rndn`, :func:`rndseed`

