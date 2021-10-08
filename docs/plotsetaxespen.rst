
plotSetAxesPen
==============================================

Purpose
----------------
Sets the color, thickness and style for the axes lines.

Format
----------------
.. function:: plotSetAxesPen(&myPlot, thickness[, clr[, style]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: the thickness of the axes line in pixels.
    :type thickness: Scalar

    :param clr: Optional argument, name or rgb value of the new color for the axes.
    :type clr: string

    :param style: the style of the pen. Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: Scalar

Examples
----------------

::

   // Declare plotControl structure
   struct plotControl myPlot;
   
   // Initialize plotControl structure
   myPlot = plotGetDefaults("xy");
   
   // Set drawn axes lines to be 2 pixels wide and black
   plotSetAxesPen(&myPlot, 2, "black");
   
   // Create data
   x = seqa(0.1, 0.1, 50);
   y = sin(x)~cos(x);
   
   // Plot the data with the new line colors
   plotXY(myPlot, x, y);


Remarks
-------

- The X and Y axis line properties can be set separately with :func:`plotSetXPen` and :func:`plotSetYPen`.
- A bounding box can be set around the entire graph with :func:`plotSetOutlineEnabled`.

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLinePen`, :func:`plotSetXPen`, :func:`plotSetYPen`

