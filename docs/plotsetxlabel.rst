
plotSetXLabel
==============================================

Purpose
----------------

Controls the settings for the x-axis label on a graph.

Format
----------------
.. function:: plotSetXLabel(&myPlot, label[, font[, fontSize[, fontColor]]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param label: the new label. This may contain HTML for the creation of Greek letters, mathematical symbols and text formatting.
    :type label: string

    :param font: Optional argument, font or font family name.
    :type font: string

    :param fontSize: Optional argument, font size in points.
    :type fontSize: scalar

    :param fontColor: Optional argument, named color or RGB value.
    :type fontColor: string

Examples
----------------

Example 1: Basic usage
++++++++++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("hist");

    // Set the x-axis label, label font, label font size, and
    // label color
    plotSetXLabel(&myPlot, "Time (sec)", "verdana", 10, "black");

    // Create data
    x = rndn(1e5,1);

    // Plot a histogram of the x data spread over 50 bins
    plotHist(myPlot, x, 50);


Example 2: HTML
+++++++++++++++

You may add Greek letters, mathematical symbols, subscript and superscript to your axis labels using HTML. To add HTML to a label, you need to wrap the text to be interpreted as HTML in HTML tags.

::

    label_string = "<html>&beta;</html>";
    plotSetXLabel(&myPlot, label_string);

The code above will add the letter :math:`\beta` to the x-axis label. The HTML ``'sup'`` tag will create superscript and the ``'sub'`` tag will create subscript. For example:

::

    label_string = "<html>&sigma;<sup>2</sup></html>";
    plotSetXLabel(&myPlot, label_string);

will add :math:`\sigma^2` to your x-axis label. While,

::

    label_string = "<html>Y<sub>t-1</sub></html>";
    plotSetXLabel(&myPlot, label_string);

will create :math:`Y_{t-1}`

Example 3: Latex
++++++++++++++++

You can use Latex to add equations to axis labels. Note that double-backslashes must be used as shown below.

::

    // Tell GAUSS to interpret the axis label text as Latex
    plotSetTextInterpreter(&myPlot, "Latex", "axes");

    // Add Latex axis label.
    plotSetXLabel(&myPlot, "\\sqrt{\\lambda}");

The code above will add :math:`\sqrt{\lambda}` to your x-axis label.



Remarks
-------

.. include:: include/plotattrremark.rst
.. include:: include/plotsetactivexremark.rst

.. seealso:: Functions :func:`plotSetActiveX`, :func:`plotSetXTicInterval`, :func:`plotSetXTicLabel`, :func:`plotSetYLabel`, :func:`plotSetLinePen`, :func:`plotSetGridPen`

