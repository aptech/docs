
plotCloseAll
==============================================

Purpose
----------------
Closes all open graph tabs.

Format
----------------
.. function:: plotCloseAll()

Examples
----------------

::

    // Create data
    x = rndn(1000, 1);
    x2 = rndn(1000, 1);
    x3 = rndn(1000, 1);

    // Plot first vector as a percentage histogram with 30 bins
    plotHistP(x, 30);

    // Open new graphic window so the next plot
    // will not overwrite the histogram just created
    plotOpenWindow();

    // Plot second vector, drawing over the previously created
    // graph.
    plotHistP(x2, 30);

    // Close both graphics windows
    plotCloseAll();


Remarks
-------

If this was used in a program, it could be used at the start to clear out previous graphs before creating new ones.

.. seealso:: Functions :func:`plotOpenWindow`, :func:`plotSetNewWindow`, :func:`plotCanvasSize`
