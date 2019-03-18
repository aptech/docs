
plotAddTextbox
==============================================

Purpose
----------------
Adds a textbox to an existing graph.

Format
----------------
.. function:: plotAddTextbox(text,  x_start,  y_start) 
			  plotAddTextbox(myAnnotation,  text,  x_start,  y_start)

    :param myAnnotation: a plotAnnotation structure.
    :type myAnnotation: Optional input

    :param text: the text to place in the textbox.
    :type text: String

    :param x_start: the X coordinate for the start of the bounding box for each respective text box.
    :type x_start: Scalar or Nx1 vector

    :param y_start: the Y coordinate for the start of the bounding box for each respective text box.
    :type y_start: Scalar or Nx1 vector

Examples
----------------

//Create text for textbox
box_text = "Periods of recession are highlighted";

x_start = 4;
y_start = 3;

//Add textbox to the (4,3) location on the last draw graph
plotAddTextbox(box_text, x_start, y_start);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//Simulate and plot simple linear model
b_0 = 2;
b_1 = 1.7;
x = rndn(100, 1);
y = b_0 + b_1 .* x + rndn(100, 1);
plotScatter(x, y);

//Declare instance of plotAnnotation structure
//and fill in with default values
struct plotAnnotation myTextbox;
myTextbox = annotationGetDefaults();

//Set textbox background to 'light gray' with 20% opacity
annotationSetBkd(&myTextbox, "light gray", 0.2);

//Turn off line surrounding textbox by setting thickness to 0px
annotationSetLineThickness(&myTextbox, 0);

//Create text for textbox, using HTML
box_text = "α = 2; β<sub>1</sub> = 1.7";

//The top-left corner of the text box
//will be located at the coordinates (0, -1)
x_start = 0;
y_start = -1;

//Add textbox to last draw graph
plotAddTextbox(myTextbox, box_text, x_start, y_start);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you use textboxes often and usually want the same styling, instead of going through the steps above
every time you would like to add a text box, you should create a simple procedure to do the set up for you. Here is
an example of a procedure that will return a customized plotAnnotation structure. You can pass this function in
to plotAddTextbox.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Add the procedure below to your user library
    //and you will only need one line for all the settings
    plotAddTextbox(grayTextSettings(), "My customized text box", 0.15, 0.2);
    
    proc (1) = grayTextSettings();
        struct plotAnnotation mytextbox;
    
        mytextbox = annotationGetDefaults();
        annotationSetBkd(&mytextbox, "#DDDDDD", 0.3);
        annotationSetFont(&mytextbox, "times", 18, "#555555");
        annotationSetLineThickness(&mytextbox, 2);
        annotationSetLineColor(&mytextbox, "#555555");
        retp(mytextbox);
    endp;

.. seealso:: Functions :func:`plotAddShape`, :func:`annotationGetDefaults`
