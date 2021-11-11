
plotOpenWindow
==============================================

Purpose
----------------
Opens a new, empty graphic window to be used by the next drawn graph.

Format
----------------
.. function:: plotOpenWindow()

Examples
----------------

::

    // Create data
    x = rndn(10000, 1);
    x2 = rndn(10000, 1);
    x3 = rndn(10000, 1);

    // Plot first vector as a percentage histogram with 30 bins
    plotHistP(x, 30);

    // Plot second vector, drawing over the previously created
    // graph.
    plotHistP(x2, 30);

    // Create a new graphic window and plot the second vector as
    // a percentage histogram with 30 bins inside this new
    // window.
    plotOpenWindow();

    // Draw the graph
    plotHistP(x3, 30);

Remarks
-------

To automatically open each new graph in a new graph window, use
:func:`plotSetNewWindow` or set the preference in the main application menu. This
may be found by selecting :menuselection:`Tools --> Preferences` and then clicking on
**Graphics** on the left side of the preferences window.

If you select **Open a new tab** next to **When a graph is added** at the top of the
graphics preferences window on the **General** tab, each new graph will be automatically drawn
in a new graphics window.

.. seealso:: Functions :func:`plotSave`, :func:`plotCustomLayout`, :func:`plotCloseWindow`, :func:`plotSetNewWindow`, :func:`plotCanvasSize`
