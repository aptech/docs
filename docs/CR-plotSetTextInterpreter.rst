
plotSetTextInterpreter
==============================================

Purpose
----------------
Controls the text interpreter settings for a graph.

Format
----------------
.. function:: plotSetTextInterpreter(&myPlot, interpreter)plotSetTextInterpreter(&myPlot, interpreter, location)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param interpreter: "html", "plain", "latex".
    :type interpreter: String

    :param location: "all", "legend", "title" or "axes". Default is "all".
    :type location: String

Examples
----------------

Plain interpreter
+++++++++++++++++

::

    new;
    					
    //Declare plotControl structure
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("hist");
    
    //Set the interpreter of axes 
    plotSetTextInterpreter(&myPlot, "plain", "axes");
    
    //Set the X-axis label, using the > character which would
    //would fail with the default HTML interpreter.
    plotSetXLabel(&myPlot, "Weight > 50 Kg");
    
    //Create data
    x = rndn(1e5,1);
    
    //Plot a histogram of the x data spread over 50 bins
    plotHist(myPlot, x, 50);

HTML interpreter
++++++++++++++++

You may add Greek letters, mathematical symbols, subscript and superscript to your title, axes and legend using HTML. To add HTML to a label, you can use plotSetTextInterpreter to set "html" for the text to be interpreted as HTML.

::

    //Set the interpreter of axes 
    plotSetTextInterpreter(&myPlot, "html", "axes");		
    
    label_string = "β";
    
    //Set the X-axis label
    plotSetXLabel(&myPlot, label_string);

The code above will add the letter β to the graph title. The HTML 'sup' tag will create superscript and the 'sub' tag will create subscript. For example:

::

    label_string = "σ<sup>2</sup>";
    
    //Set the X-axis label
    plotSetXLabel(&myPlot, label_string);

will add σ2 to your title. While,

::

    label_string = "Y<sub>t-1</sub>";
    
    //Set the X-axis label
    plotSetXLabel(&myPlot, label_string);

will create Yt-1.

Latex Interpreter
+++++++++++++++++

You can also use Latex to add complex math expression, or non-Latin scripts to your title, axes, and legend. You can use plotSetTextInterpreter to set "latex"for the text to be interpreted as Latex.

::

    new;
    				
    // Declare plotControl structure
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    // Set up text interpreter
    plotSetTextInterpreter(&myPlot, "latex", "all");
    
    // Set up X-axis label
    label_string = "x";
    plotSetXLabel(&myPlot, label_string, "arial", 20);
    
    // Set up legend in LateX format
    string legend_string = {
    "y_1 = \\cos{(x)}",
    "y_2 = \\sin{(\\frac{x}{2})} = \\pm \\sqrt{\\frac{1-\\cos{(x)}}{2}}",
    "y_3 = \\cos{(\\frac{x}{2})} = \\pm \\sqrt{\\frac{1+\\cos{(x)}}{2}}"};
        
    plotSetLegend(&myPlot, legend_string, "bottom",1);
    plotSetLegendFont(&myPlot, "arial", 20);
    
    // Set up title
    title_string = "Trigonometric\\ Functions";
    plotSetTitle(&myPlot, title_string, "arial", 24);
    
    // Create data
    n = 50;
    x = seqa(0,(2*pi)/(n-1), n);
    
    // Plot
    plotXY(myPlot, x, cos(x)~sin(x/2)~cos(x/2));

The plot is

Remarks
-------

When the text interpreter is set to use Latex:

-  Since backslashes inside of a string represent the escaping of a
   character, use double backslashes to represent a backslash.
-  The default mode is that of an in-line equation. To add a section of
   strictly text, wrap the text only section in \\text{}. For example:

   ::

      "\\text{The formula is } \\alpha + \\beta_1 X + \\epsilon"

-  Text outside of a \\text{} section will use the TeX font. Text inside
   of a \\text{} section will use whatever font was specified for the
   label.

The 'plain' text interpreter will allow you to pass in characters that
would be invalid HTML, such as the symbols '<' and '>'.

This function sets an attribute in a plotControl structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools->Preferences->Graphics**
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions 
labels <GG-GAUSSGraphics/GG-LaTeXinGAUSSGraphics.html>`__\,\ `plotGetDefaults <CR-plotGetDefaults.html#plotGetDefaults>`__\,\ `plotSetYLabel <CR-plotSetYLabel.html#plotSetYLabel>`__\,\ `plotSetXLabel <CR-plotSetXLabel.html#plotSetXLabel>`__\,\ `plotSetTitle <CR-plotSetTitle.html#plotSetTitle>`__\,\ `plotSetLegend <CR-plotSetLegend.html#plotSetLegend>`__

plot control text interpreter Latex HTML plain
