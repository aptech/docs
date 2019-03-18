
annotationSetLineThickness
==============================================

Purpose
----------------
Sets the line thickness for textbox, rectangle or ellipse borders as well as the color for lines and arrows.

Format
----------------
.. function:: annotationSetLineThickness(&myAnnotation, thickness)

    :param myAnnotation: A pointer to an instance of a plotAnnotation structure.
    :type myAnnotation: TODO

    :param thickness: the thickness of the line in pixels.
    :type thickness: Scalar

Examples
----------------

/*
** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
** and fill it in with default values
*/
struct plotAnnotation myAnnotation;
myAnnotation = annotationGetDefaults();

// Set line thickness to 1 pixel
annotationSetLineThickness(&myAnnotation, 1);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// Create and plot some simple data
x = seqa(-1.5, 0.1, 31);
y = cos(x);
plotXY(x, y);

/*
** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
** and fill it in with default values
*/
struct plotAnnotation myAnnotation;
myAnnotation = annotationGetDefaults();

// Set line thickness to 1 pixel (for rectangle border in this case)
annotationSetLineThickness(&myAnnotation, 1);

/*
** Add rectangle to 'xy' plot from above
** using settings from 'myAnnotation'
*/
x_start = -pi ./ 4;
y_start = 0.07;
x_end = pi ./ 4;
y_end = 0.71;

plotAddShape(myAnnotation, "rectangle", x_start, y_start, x_end, y_end);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

See Also
plotAddTextbox, plotAddArrow, plotAddShape, annotationGetDefaults

