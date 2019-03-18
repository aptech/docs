
cdfTnc
==============================================

Purpose
----------------

The integral under noncentral Student's  t distribution, from
-∞ to x. It can return a vector of values,
but the degrees of freedom and noncentrality parameter
must be the same for all values of x.

Format
----------------
.. function:: cdfTnc(x,  v,  d)

    :param x: values of upper limits of integrals.
    :type x: Nx1 vector

    :param v: degrees of freedom, v > 0.
    :type v: scalar

    :param d: noncentrality parameter.
        
        This is the square root of the noncentrality parameter
        that sometimes goes under the symbol lambda. (See Scheffe,
        The Analysis of Variance, App. IV, 1959.)
    :type d: scalar

    :returns: y (*Nx1 vector*), integrals from -∞ to x of
        noncentral t.

Examples
----------------

noncentral t distributions with different parameters.
+++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // sigma = 5
    x = seqa(0,0.2,101);
    sigma = 5;
    df = 1~2~5~10~100;
    y = cdfTnc(x, df, sigma');
    plotxy(x, y);

After running above code,

noncentral t distributions with different degree of freedoms.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // df = 10
    x = seqa(-5,0.5,41);
    sigma = seqa(0, 0.5, 7);
    df = 10;
    y = cdfTnc(x, df, sigma');
    plotxy(x, y);

After running above code,

::

    

Remarks
+++++++

cdfTc(x, v) = 1 - cdfTnc(x, v,0).

.. seealso:: Functions :func:`cdfFnc`, :func:`cdfChinc`

non central student t cdf cumulative distribution function
