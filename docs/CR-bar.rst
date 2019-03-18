
bar
==============================================

Purpose
----------------
Generates a bar graph. NOTE: This function is for the deprecated PQG graphics, use plotBar instead.

Format
----------------
.. function:: bar(val,  ht)

    :param val: bar labels. If scalar 0, a
        sequence from 1 to rows(ht) will be created.
    :type val: Nx1 numeric vector

    :param ht: bar heights.
    :type ht: NxK numeric vector

Examples
----------------
In this example, three overlapping sets of bars will be created. The three heights for the ith
bar are stored in x[i,.].

::

    library pgraph;
    graphset;
     
    t = seqa(0,1,10);
    x =(t^2/2).*(1~0.7~0.3);
     
    _plegctl = { 1 4 };
    _plegstr = "Accnt #1\000Accnt #2\000Accnt #3";
    title("Theoretical Savings Balance");
    xlabel("Years");
    ylabel("Dollars x 1000");
    _pbartyp = { 1 10 }; /* Set color of the bars */
    _pnum = 2;
    
    bar(t,x); /* Use t vector to label X axis. */

Source
++++++

pbar.src

.. seealso:: Functions :func:`asclabel`, :func:`xy`, :func:`logx`, :func:`logy`, :func:`loglog`, :func:`scale`, :func:`hist`
