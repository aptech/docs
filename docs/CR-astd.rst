
astd
==============================================

Purpose
----------------
Computes the standard deviation of the elements across one dimension of an N-dimensional array.

Format
----------------
.. function:: astd(x,  dim)

    :param x: N-dimensional array.
    :type x: TODO

    :param dim: number of dimension to sum across.
    :type dim: scalar

    :returns: y (*TODO*), N-dimensional array, standard deviation across specified dimension of x.

Examples
----------------

::

    //Create a 1e6x1 vector of random normal numbers with a
    //standard deviation of 25 and reshape it into a 
    //2e5x3x2 array
    rndseed 456;
    a = areshape(25*rndn(2e6,1),2e5|3|2);
    y = astd(a,3);

The code above should produce a 3x2 matrix with all elements close to 25 similar to what we see below.

::

    25.070091        24.994774 
    24.988263        24.990370 
    24.956467        24.987882

.. seealso:: Functions :func:`astds`, :func:`stdc`

standard deviation elements dimension array
