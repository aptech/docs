
putvals
==============================================

Purpose
----------------

Inserts values into a matrix or N-dimensional array.

Format
----------------
.. function:: putvals(x, inds, vals)

    :param x: 
    :type x: MxK matrix or N-dimensional array

    :param inds: specifying where the new values
        are to be inserted, where D is the number of dimensions
        in x.
    :type inds: LxD matrix of indices

    :param vals: new values to insert.
    :type vals: Lx1 vector

    :returns: y (*MxK matrix or N-dimensional array*) , copy of x
        containing the new values in  vals.

Remarks
-------

If x is a vector, inds should be an Lx1 vector. If x is a matrix, inds
should be an Lx2 matrix. Otherwise if x is an N-dimensional array, inds
should be an LxN matrix.

putvals allows you to insert multiple values into a matrix or
N-dimensional array at one time. This could also be accomplished using
indexing inside a for loop.


Examples
----------------

::

    x = { -0.8750  0.3616  0.6032 -0.3974,
           0.7644 -1.8509 -0.2703 -0.8190,
           0.7886  1.2678 -1.4998 -0.5876,
           0.6639 -0.7972  1.2713  0.1896,
           0.6303  0.7879 -0.7451 -0.5419 };
    inds = { 1 1, 2 4, 3 2, 3 4, 5 3 };
    v = seqa(1,1,5);
    y = putvals(x,inds,v);

After the code above:

::

    1.000  0.362  0.603 -0.397      1.00
        0.764 -1.851 -0.270  2.000      2.00
    y = 0.789  3.000 -1.500  4.000  v = 3.00
        0.664 -0.797  1.271  0.190      4.00
        0.630  0.788  5.000 -0.542      5.00

