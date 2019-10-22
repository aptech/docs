
plotBar
==============================================

Purpose
----------------
Generates a bar graph.

Format
----------------
.. function:: plotBar([myPlot, ]labels, height) 

    :param myPlot: Optional argument, a :class:`plotControl` structure
    :type myPlot: struct

    :param labels: bar labels. If scalar 0, a sequence from 1 to ``rows(height)`` will be created.
    :type labels: Nx1 numeric vector or Nx1 string array 

    :param height: bar heights. *K* overlapping or side-by-side sets of *N* bars will be graphed.
    :type height: NxK numeric vector

Examples
----------------

::

    // Create data and labels
    labels = "January" $| "June";
    temp = { 68, 105 };
    
    // Draw bar graph
    plotBar(labels, temp);

Remarks
-------

To control the color and texture of the bars as well as whether they are
stacked or side by side:

If you are passing a :class:`plotControl` structure to your graph, you may use
the function :func:`plotSetBar`.

If you are not passing a :class:`plotControl` structure, these properties are set
in the Preferences. To access the Graphics Preferences, select
:menuselection:`Tools --> Preferences` from the GAUSS main menu. Select **Graphics** on
the left side of the preferences and then select **Bar** from the list
of graph types.

.. seealso:: Functions :func:`plotXY`, :func:`plotLogX`, :func:`plotHist`

