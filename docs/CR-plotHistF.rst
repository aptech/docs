
plotHistF
==============================================

Purpose
----------------
Graphs a histogram given a vector of frequency counts.

Format
----------------
.. function:: plotHistF(myPlot, f, c)plotHistF(f, c)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param f: frequencies to be graphed.
    :type f: Nx1 vector

    :param c: numeric labels for categories. If this is a scalar 0, a sequence from 1 to
        rows(f) will be created.
    :type c: Nx1 vector



Remarks
-------

The axes are not automatically labeled. Use the functions plotSetXLabel
and plotSetYLabel.

.. seealso:: Functions :func:`plotHist`, :func:`plotBar`, :func:`plotSetXLabel`
