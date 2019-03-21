
plotCustomLayout
==============================================

Purpose
----------------

Plots a graph of user-specified size at a user-specified location.

Format
----------------
.. function:: plotCustomLayout(xStart, yStart, width, height)

    :param xStart: the distance from the left edge of the canvas to the left edge of the custom
        plot expressed as a number between 0 and 1.
    :type xStart: scalar

    :param yStart: the distance from the bottom edge of the canvas to the bottom edge of the custom plot expressed as a number between 0 and 1.
    :type yStart: scalar

    :param width: the width of the custom plot expressed as a number between 0 and 1.
    :type width: scalar

    :param height: the height of the custom plot expressed as a number between 0 and 1.
    :type height: scalar

Examples
----------------

::

    //Create an additive sequence starting from -pi and moving 
    //forward in 0.1 increments
    x = seqa(-pi, 0.1, 63);
    
    //Plot the cosine of x
    plotXY(x, cos(x));
    
    //Create a custom section for the next graph starting 10% 
    //from the main graph's left edge, 10% from the bottom of 
    //the main graph, with a width and height both equalling 
    //30% of the width of the main graph.
    plotCustomLayout(0.1, 0.1, 0.3, 0.3);
    
    //Plot the next graph in the custom layout
    plotXY(x[1:20], cos(x[1:20] ) ));
    
    //Prevent the next graph from being drawn in this custom 
    //region
    plotClearLayout();

Remarks
-------

After calling this function all subsequent graphs will be plotted inside
of the specified custom layout until the layout is reset with
plotLayout, or the layout is cleared with plotClearLayout.

.. seealso:: Functions :func:`plotSetBar`, :func:`plotBar`, :func:`plotHistP`, :func:`plotGetDefaults`
