
plotSetNewWindow
==============================================

Purpose
----------------

Determines whether each new graph is drawn in a new graph tab or re-uses a pre-existing graph tab.

Format
----------------
.. function:: plotSetNewWindow(&myPlot, new_window)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param new_window: 1 to create a new graph tab or 0 to re-use.
    :type new_window: scalar

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set graph to create a new graph tab
    new_window = 1;
    plotSetNewWindow(&myPlot, new_window);

    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);

    // Plot the data in a new graph tab window
    plotXY(myPlot, x, y);

Remarks
-------

To open a new graph window once, use :func:`plotOpenWindow`. This function sets
an attribute in a :class:`plotControl` structure. It does not affect an existing
graph, or a new graph drawn using the default settings that are
accessible in the main application window from the
:menuselection:`Tools --> Graphics --> Preferences` menu. See the `GAUSS Graphics chapter <GG-GAUSSGraphics.html>`_
for more information on the methods available for customizing your
graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotOpenWindow`, :func:`plotSetTitle`, :func:`plotSetLineColor`
