
plotSetYLabel
==============================================

Purpose
----------------

Controls the settings for the y-axis label on a graph.

Format
----------------
.. function:: plotSetYLabel(&myPlot, label[, font[, fontSize[, fontColor]]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param label: the new label or labels. If you are using more than one y-axis, the first element of the 2x1 label string array
        will set the label for the left y-axis and the second element will set the label for the right y-axis.
        This may contain HTML for the creation of Greek letters, mathematical symbols and text formatting.
    :type label: String or 2x1 string array
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

    // Set the y-axis label, label font, font size and color
    plotSetYLabel(&myPlot, "Time (sec)", "verdana", 10, "black");

    // Create data
    x = rndn(1e5, 1);

    // Plot a histogram of the x data spread over 50 bins
    plotHist(myPlot, x, 50);

Example 2: Setting both Y-axes
++++++++++++++++++++++++++++++

::

    // Create with different Y-ranges
    x = seqa(1, 1, 5);
    y = { 98  1.5,
          92  0.9,
          97  1.3,
          94  2.1,
          95  2.4 };

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set the first curve to use the left y-axis and the second curve to use the right
    plotSetWhichYAxis(&myPlot, "left" $| "right");

    // Set the left and right y-axis labels
    plotSetYLabel(&myPlot, "Number of subjects"$|"Percent classified");

    // Plot the data
    plotXY(myPlot, x, y);

Example 3: HTML
+++++++++++++++

You may add Greek letters, mathematical symbols, subscript and superscript to your axis labels using HTML. To add HTML to a label, you need to wrap the text to be interpreted as HTML in HTML tags.

::

    label_string = "<html>&beta;</html>";
    plotSetYLabel(&myPlot, label_string);

The code above will add the letter :math:`\beta` to the y-axis label. The HTML ``'sup'`` tag will create superscript and the ``'sub'`` tag will create subscript. For example:

::

    label_string = "<html>&sigma;<sup>2</sup></html>";
    plotSetYLabel(&myPlot, label_string);

will add :math:`\sigma^2` to your y-axis label. While,

::

    label_string = "<html>Y<sub>t-1</sub></html>";
    plotSetYLabel(&myPlot, label_string);

will create :math:`Y_{t-1}`

Example 4: Latex
++++++++++++++++

You can use Latex to add equations to axis labels. Note that double-backslashes must be used as shown below.

::

    // Tell GAUSS to interpret the axis label text as Latex
    plotSetTextInterpreter(&myPlot, "Latex", "axes");

    // Add Latex axis label.
    plotSetYLabel(&myPlot, "\\sqrt{\\lambda}");

The code above will add :math:`\sqrt{\lambda}` to your y-axis label.


Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetXLabel`, :func:`plotSetXTicInterval`, :func:`plotSetXTicLabel`, :func:`plotSetZLabel`, :func:`plotSetLineColor`, :func:`plotSetGrid`

