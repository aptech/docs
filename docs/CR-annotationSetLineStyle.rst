
annotationSetLineStyle
==============================================

Purpose
----------------
Sets the line style for textbox, rectangle or ellipse borders as well as the style for lines and arrows.

Format
----------------
.. function:: annotationSetLineStyle(&myAnnotation, style)

    :param &myAnnotation: A pointer to an instance of a plotAnnotation structure.
    :type &myAnnotation: TODO

    :param style: line style. Valid options include:
        1 - solid2 - dash3 - dot4 - dash-dot5 - dash-dot-dot
    :type style: Matrix

Examples
----------------

/*
** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
** and fill it in with default values
*/
struct plotAnnotation myAnnotation;
myAnnotation = annotationGetDefaults();

// Set line style to 'dot'
line_style = 3;
annotationSetLineStyle(&myAnnotation,line_style);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// Create and plot some simple data
x = seqa(0.1, 0.2, 10);
y = 3 .* sin(x) + rndu(10, 1);
plotXY(x, y);

/*
** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
** and fill it in with default values
*/
struct plotAnnotation myAnnotation;
myAnnotation = annotationGetDefaults();

// Set line style to dash (for ellipse border in this case)
annotationSetLineStyle(&myAnnotation, 2);

/*
** Add ellipse to 'xy' plot from above
** using settings from 'myAnnotation'
*/
plotAddShape(myAnnotation, "ellipse", 0.4, 1.5, 1, 2.9);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

See Also
plotAddTextbox, plotAddArrow, plotAddShape, annotationGetDefaults

