
plotPolar
==============================================

Purpose
----------------

Graph data using polar coordinates.

Format
----------------
.. function:: plotPolar([myPlot, ]radius, theta)

    :param myPlot: Optional argument, a :class:`plotControl` structure
    :type myPlot: struct

    :param radius: Each column contains the magnitude for a particular line.
    :type radius: Nx1 or NxM matrix

    :param theta: Each column represents the angle values for a particular line.
    :type theta: Nx1 or NxM matrix


Examples
----------------

::

        // Declare plotControl structure
        struct plotControl myPlot;

        // Initialize plotControl structure
        myPlot = plotGetDefaults("polar");

        // Set new background color to light grey
        plotSetBkdColor(&myPlot, "light grey");

        // Create data
        x = seqa(0.1, 0.1, 200);
        y = x;

        // Create a polar plot of the data with the new background
        // color
        plotPolar(myPlot, x, y);

.. seealso:: Functions :func:`plotXY`, :func:`plotLogX`, :func:`plotLayout`, :func:`plotSetXLabel`
