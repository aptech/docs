
plotAddArrow
==============================================

Purpose
----------------
Adds an arrow to an existing graph.

Format
----------------
.. function:: plotAddArrow(myAnnotation, x_start, y_start, x_end, y_end, head_size) 
			          plotAddArrow( x_start, y_start, x_end, y_end, head_size)

    :param myAnnotation: an instance of a plotAnnotation structure.
    :type myAnnotation: Optional argument

    :param x_start: the X coordinate for the start of each respective arrow.
    :type x_start: Scalar or Nx1 vector

    :param y_start: the Y coordinate for the start of each respective arrow.
    :type y_start: Scalar or Nx1 vector

    :param x_end: the X coordinate for the end of each respective arrow.
    :type x_end: Scalar or Nx1 vector

    :param y_end: the Y coordinate for the end of each respective arrow.
    :type y_end: Scalar or Nx1 vector

    :param head_size: the size of the arrowhead(s) in pixels. The first element of head_size is the size for head at the end of the arrow. The second element is the size of the head at the start of the arrow.
    :type head_size: 2x1 vector

Remarks
-------

Please note that plotAddArrow will add arrows to existing graphs, it
will not create a new graph if one does not exist. plotAddArrow is not
yet supported for surface plots.


Examples
----------------

x_start = 0.2;
y_start = 0.25;
x_end = 0.4;
y_end = 0.5;

//Set arrowhead at the end to 15 px
//No arrowhead at the beginning of the arrow
head_size = { 15, 0 };

//Add an arrow to graph
plotAddArrow(x_start, y_start, x_end, y_end, head_size);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//Draw random scatter plot
x = rndu(10,1);
y = rndu(10, 1);
plotScatter(x, y);

//Add arrow from the first point to the ninth point
plotAddArrow(x[1], y[1], x[9], y[9], 12);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. seealso:: Functions :func:`plotAddTextbox`, :func:`annotationGetDefaults`, :func:`annotationSetLineColor`
