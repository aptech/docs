
plotSetTitle
==============================================

Purpose
----------------
Controls the settings for the title for a graph.

Format
----------------
.. function:: plotSetTitle(&myPlot, title[, font[, fontSize[, fontColor]]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param title: the new title. This may contain HTML for the creation of Greek letters, mathematical symbols and text formatting.
    :type title: string

    :param font: Optional argument, font or font family name.
    :type font: string

    :param fontSize: Optional argument, font size in points.
    :type fontSize: scalar

    :param fontColor: Optional input, named color or RGB value.
    :type fontColor: string

Examples
----------------

Example 1
+++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("hist");

    // Set the title, title font and title font size
    plotSetTitle(&myPlot, "GAUSS Example Graph", "verdana", 10);

    // Create data
    x = rndn(1e5,1);

    // Plot a histogram of the x data spread over 50 bins
    plotHist(myPlot, x, 50);

Example 2
+++++++++

You may add Greek letters, mathematical symbols, subscript and superscript to your title using HTML.
To add HTML to a label, you need to wrap the text to be interpreted as HTML in HTML tags.

::

    label_string = "<html>&beta;</html>";
    plotSetTitle(&myPlot, label_string);

The code above will add the letter :math:`\beta` to the graph title. The HTML ``sup`` tag will create superscript and the ``sub`` tag will create subscript. For example:

::

    label_string = "<html>&sigma;<sup>2</sup></html>";
    plotSetTitle(&myPlot, label_string);

will add :math:`\sigma^2` to your title. While,

::

    label_string = "<html>Y<sub>t-1</sub></html>";
    plotSetTitle(&myPlot, label_string);

will create :math:`Y_{t-1}`

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetYLabel`, :func:`plotSetLineColor`, :func:`plotSetGrid`

