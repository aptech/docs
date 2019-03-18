
plotContour
==============================================

Purpose
----------------

Graphs a matrix of contour data.

Format
----------------
.. function:: plotContour(myPlot, x, y,  z)plotContour(x, y,  z)

    :param myPlot: Optional input: plotControl structure.
    :type myPlot: TODO

    :param x: the X axis data.
    :type x: 1xK vector

    :param y: the Y axis data.
    :type y: Nx1 vector

    :param z: the matrix of height data to be plotted.
    :type z: NxK matrix

Examples
----------------

::

    //Clear out variables in GAUSS workspace
    new;
    				
    //Create contour data 
    x = seqa(-4,.125,161)';
    y = seqa(-8,.125,161);
    z = sin(x) .* cos(y) * .5;
    z = z .* sin(x/3) .* cos(y/3);
    z = z .* sin(x/5) + sin(y/2.5)/3 + sin(x/2.5)/3;
    
    //Set up control structure with defaults 
    //for surface plots
    struct plotControl myPlot;
    myPlot = plotGetDefaults("surface");
    
    //Set title and Z axis label 
    plotSetTitle(&myPlot, "Contour plot example", "Courier bold", 16, "black");
    plotSetZLabel(&myPlot, "Height (m)", "Arial", 18);
    
    //Turn off X and Y axis labels 
    plotSetXLabel(&myPlot, "");
    plotSetYLabel(&myPlot, "");
    
    //Set contour level colors
    string rainbow = { "Red", "Orange", "Yellow", "Green", "Blue", "Purple" };
    plotSetLineColor(&myPlot, rainbow);
    
    //Draw graph using plotcontrol structure
    plotContour(myPlot, x, y, z);

Remarks
+++++++

A vector of evenly spaced contour levels will be generated automatically
from the z matrix data. Each contour level will be labeled. For
unlabeled contours, use ztics.

To specify a vector of your own unequal contour levels, set the vector
\_plev before calling contour.

To specify your own evenly spaced contour levels, see ztics.

.. seealso:: Functions :func:`plotSurface`
