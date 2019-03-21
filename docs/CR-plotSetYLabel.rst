
plotSetYLabel
==============================================

Purpose
----------------

Controls the settings for the Y-axis label on a graph.

Format
----------------
.. function:: plotSetYLabel(&myPlot, label, font, fontSize, fontColor)plotSetYLabel(&myPlot, label, font, fontSize)plotSetYLabel(&myPlot, label, font)plotSetYLabel(&myPlot, label)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param label: the new label or labels. If you are using more than one Y-axis, the first element of the 2x1 label string array
        will set the label for the left Y-axis and the second element will set the label for the right Y-axis. This may contain HTML for the creation of Greek letters, mathematical symbols and text formatting.
    :type label: String or 2x1 string array

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

//Set the Y-axis label, label font, font size and color 
plotSetYLabel(&myPlot, "Time (sec)", "verdana", 10, "black");

//Create data
x = rndn(1e5,1);

//Plot a histogram of the x data spread over 50 bins
plotHist(myPlot, x, 50);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//Create with different Y-ranges
x = seqa(1,1,5);
y = { 98  1.5,
      92  0.9,
      97  1.3,
      94  2.1,
      95  2.4 };

//Declare plotControl structure
struct plotControl myPlot;

//Initialize plotControl structure
myPlot = plotGetDefaults("xy");

//Set the first curve to use the left Y-axis and the second curve to use the right
plotSetWhichYAxis(&myPlot, "left" $| "right");

//Set the left and right Y-axis labels
plotSetYLabel(&myPlot, "Number of subjects", "Percent classified");

//Plot the data
plotXY(myPlot, x, y);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You may add Greek letters, mathematical symbols, subscript and superscript to your axis labels using HTML. To add HTML to a label, you need to wrap the text to be interpreted as HTML in HTML tags.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    label_string = "<html>β</html>";
    plotSetYLabel(&myPlot, label_string);

The code above will add the letter β to the y-axis label. The HTML 'sup' tag will create superscript and the 'sub' tag will create subscript. For example:

::

    label_string = "<html>σ<sup>2</sup></html>";
    plotSetYLabel(&myPlot, label_string);

will add σ2 to your y-axis label. While,

::

    label_string = "<html>Y<sub>t-1</sub></html>";
    plotSetYLabel(&myPlot, label_string);

will create Yt-1

Remarks
+++++++

This function sets an attribute in a plotControl structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools->Preferences->Graphics**
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetXLabel`, :func:`plotSetXTicInterval`, :func:`plotSetXTicLabel`, :func:`plotSetZLabel`, :func:`plotSetLineColor`, :func:`plotSetGrid`
