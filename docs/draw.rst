
draw
==============================================

Purpose
----------------

Graphs lines, symbols, and text using the PQG global
variables. This procedure does not require actual X,
Y, or Z data since its main purpose is to manually
build graphs using `_pline`, `_pmsgctl`, `_psym`,
`_paxes`, `_parrow` and other globals.

.. NOTE:: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: draw

Examples
----------------

::

    library pgraph;
    graphset;

    begwind;

    // make full size window for  plot
    makewind(9, 6.855, 0, 0, 0);

    // make small overlapping window for text
    makewind(3, 1, 3, 3, 0);

    setwind(1);

       // Generate x and y
       x = seqa(.1, .1, 100);
       y = sin(x);

       // plot data in first window
       xy(x, y);

    nextwind;

       _pbox = 15;
       _paxes = 0;
       _pnum = 0;
       _ptitlht = 1;
       margin(0,0,2,0);

       // add a smaller text window
       title("This is a text window.");

       // Create graph
       draw;

    endwind;

Remarks
-------

:func:`draw` is especially useful when used in conjunction with transparent windows.

Source
------

pdraw.src

.. seealso:: Functions :func:`window`, :func:`makewind`
