
recode
==============================================

Purpose
----------------
Changes the values of an existing vector from a vector of new values. Used in data transformations.

Format
----------------
.. function:: y = recode(x, e, v)

    :param x: data to be recoded (changed)
    :type x: Nx1 vector 

    :param e: matrix of 1's and 0's
    :type e: NxK matrix

    :param v: vector containing the new values to be assigned to the recoded variable
    :type v: Kx1 vector

    :return y: containing the recoded values of *x*.

    :rtype y: Nx1 vector

Examples
----------------

::

    x = { 20,
          45,
          32,
          63,
          29 };
    
    // Create 4 column vectors with a 1 where the statement
    // evaluates as 'true'
    e1 = (20 .lt x) .and (x .le 30);
    e2 = (30 .lt x) .and (x .le 40);
    e3 = (40 .lt x) .and (x .le 50);
    e4 = (50 .lt x) .and (x .le 60);
    
    // Horizontally concatenate the column vectors into a 5x4
    // matrix
    e = e1~e2~e3~e4;
     
    v = { 1.2,
          2.4,
          3.1,
          4.6 };
    
    // Replace elements of 'x' with elements from 'v' based upon
    // the 0's and 1's in 'e'
    y = recode(x,e,v);

The above code assigns *e* and *y* as follows:

::

        0   0   0   0
        0   0   1   0
    e = 0   1   0   0
        0   0   0   0
        1   0   0   0
    
    // Since the third column of the second row of 'e' is equal
    // to 1, the second row of 'y' is set equal to the third 
    // element of 'v', etc.
        20.000000
        3.1000000
    y = 2.4000000
        63.000000
        1.2000000

Remarks
-------

There should be no more than a single 1 in any row of *e*.

For any given row :math:`N` of *x* and *e*, if the Kth column of *e* is 1, the Kth
element of *v* will replace the original element of *x*.

If every column of e contains a 0, the original value of *x* will be unchanged.


Source
------

datatran.src

.. seealso:: Functions `code`, :func:`reclassifyCuts`, :func:`reclassify`, :func:`substute`, :func:`rescale`, :func:`dummy`

