
annotationSetBkd
==============================================

Purpose
----------------
Sets the background color and transparency level for a textbox, rectangle or ellipse.

Format
----------------
.. function:: annotationSetBkd(&myAnnotation, color, transparency)

    :param &myAnnotation: A pointer to an instance of a plotAnnotation structure.
    :type &myAnnotation: TODO

    :param color: color name or hex HTML color code.
    :type color: String

    :param transparency: transparency percentage. Valid range is between 0 and 1.
    :type transparency: Scalar

Examples
----------------

/*
** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
** and fill it in with default values
*/
struct plotAnnotation myAnnotation;
myAnnotation = annotationGetDefaults();

// Set background to light gray with 40% opacity
annotationSetBkd(&myAnnotation, "light gray", 0.4);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// Create and plot some simple data
x = seqa(1, 1, 10);
y = rndu(10, 1);
plotXY(x, y);

/*
** Declare 'myAnnotation' to be an instance of a plotAnnotation
** structure and fill it in with default values
*/
struct plotAnnotation myAnnotation;
myAnnotation = annotationGetDefaults();

// Set background to white with 80% opacity
annotationSetBkd(&myAnnotation, "#FFFFFF", 0.8);

// Add rectangle to 'xy' plot from above
// using settings from 'myAnnotation'
plotAddShape(myAnnotation, "rectangle", 1, 0.2, 3, 0.5);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

See Also
plotAddTextbox, plotAddShape, annotationGetDefaults

