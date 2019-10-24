
plotAddShape
==============================================

Purpose
----------------
Adds an arrow, line, ellipse or rectangle to an existing graph.

Format
----------------
.. function:: plotAddShape([myAnnotation, ]which_shape, x_start, y_start, x_end, y_end)

    :param myAnnotation: Optional argument, an instance of a :class:`plotAnnotation` structure.
    :type myAnnotation: struct

    :param which_shape: indicating which shape to create, options include:

        - "ellipse"
        - "line" (to which you may add an arrow head)
        - "rectangle"

    :type which_shape: string

    :param x_start: the X coordinate for the start of the bounding box for each respective shape.
    :type x_start: scalar or Nx1 vector

    :param y_start: the Y coordinate for the start of the bounding box for each respective shape.
    :type y_start: scalar or Nx1 vector

    :param x_end: the X coordinate for the end of the bounding box for each respective shape.
    :type x_end: scalar or Nx1 vector

    :param y_end: the Y coordinate for the end of the bounding box for each respective shape.
    :type y_end: scalar or Nx1 vector

Examples
----------------

Add a rectangle
+++++++++++++++

::

    // Draw simple graph
    x = rndu(10, 1);
    y = rndu(10, 1);
    plotScatter(x, y);

    // The rectangle will be drawn between
    // third and sixth points on the plot
    x_start = x[3];
    y_start = y[3];
    x_end = x[6];
    y_end = y[6];

    // Shape type will be rectangle
    annotation_type = "rectangle";

    // Add rectangle to graph
    plotAddShape(annotation_type, x_start, y_start, x_end, y_end);

Remarks
-------

:func:`plotAddShape` will add shapes to existing graphs. It will not create a
new graph, however, if one does not already exist.

.. NOTE:: The top left corner of the bounding box for the shape will be placed at
    the coordinates that you specify. The bounding box is rectangular and
    will, therefore, not touch the edge of an ellipse at that point.

:func:`plotAddShape` is not yet supported for surface plots.

.. seealso:: Functions :func:`plotAddTextbox`, :func:`annotationGetDefaults`
