
plotSetXLabel
==============================================

Purpose
----------------

Controls the settings for the X-axis label on a graph.

Format
----------------
.. function:: plotSetXLabel(&myPlot, label, font, fontSize, fontColor)plotSetXLabel(&myPlot, label, font, fontSize)plotSetXLabel(&myPlot, label, font)plotSetXLabel(&myPlot, label)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param label: the new label. This may contain HTML for the creation of Greek letters, mathematical symbols and text formatting.
    :type label: String

    :param font: font or font family name.
    :type font: String

    :param fontSize: font size in points.
    :type fontSize: Scalar

    :param fontColor: named color or RGB value.
    :type fontColor: String

Examples
----------------

//Declare plotControl structure
struct plotControl myPlot;

//Initialize plotControl structure
myPlot = plotGetDefaults("hist");

//Set the X-axis label, label font, label font size, and 
//label color 
plotSetXLabel(&myPlot, "Time (sec)", "verdana", 10, "black");

//Create data
x = rndn(1e5,1);

//Plot a histogram of the x data spread over 50 bins
plotHist(myPlot, x, 50);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You may add Greek letters, mathematical symbols, subscript and superscript to your axis labels using HTML. To add HTML to a label, you need to wrap the text to be interpreted as HTML in HTML tags.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    label_string = "<html>β</html>";
    plotSetXLabel(&myPlot, label_string);

The code above will add the letter β to the x-axis label. The HTML 'sup' tag will create superscript and the 'sub' tag will create subscript. For example:

::

    label_string = "<html>σ<sup>2</sup></html>";
    plotSetXLabel(&myPlot, label_string);

will add σ2 to your x-axis label. While,

::

    label_string = "<html>Y<sub>t-1</sub></html>";
    plotSetXLabel(&myPlot, label_string);

will create Yt-1

Remarks
+++++++

This function sets an attribute in a plotControl structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools->Preferences->Graphics**
menu.See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetXTicInterval`, :func:`plotSetXTicLabel`, :func:`plotSetYLabel`, :func:`plotSetZLabel`, :func:`plotSetLineColor`, :func:`plotSetGrid`
