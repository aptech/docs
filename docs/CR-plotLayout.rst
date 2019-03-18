
plotLayout
==============================================

Purpose
----------------
Divides a plot into a grid of subplots and assigns the cell location in which to draw the next created graph.

Format
----------------
.. function:: plotLayout(gRows, gCols, ind)

    :param gRows: number of rows of the graph layout.
    :type gRows: scalar

    :param gCols: number of columns of the graph layout.
    :type gCols: scalar

    :param ind: cell location in which to place the next created graph.
    :type ind: scalar

Examples
----------------

::

    //Create 10x4 matrix where each column is an additive
    //sequence from 0.1 to 1.0
    x = seqa(0.1, 0.1, 10);
    y = ones(10, 4).*x;
    
    //Apply a function to each column of 'y'
    y[.,1] = cos(x);
    y[.,2] = sin(x);
    y[.,3] = cdfn(x);
    y[.,4] = exp(x);
    
    for i(1, 4, 1);
       //Divide plot canvas into a 2x2 grid of subplot
       //locations and place each newly created graph in the
       //next available cell location.
       plotLayout(2, 2, i);
    
       //Plot each column of y in a separate subplot window.
       plotXY(x, y[.,i]);
    endfor;
    
    //Clear the layout so the next plot will not be inside this 
    //layout
    plotClearLayout();

Remarks
+++++++

After calling this function all subsequent graphs will be plotted inside
of the specified layout until the layout is reset with plotLayout, or
the layout is cleared with plotClearLayout.

.. seealso:: Functions :func:`plotBar`, :func:`plotClearLayout`, :func:`plotCustomLayout`, :func:`plotHist`
