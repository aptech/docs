Graphics
===================

Graph types
----------------------

===================================    ============================================================================
:doc:`../plotacf`                         Plots the autocorrelations function (ACF).
:doc:`../plotarea`                        Creates a cumulative area plot.
:doc:`../plotbar`                         Creates a bar plot.
:doc:`../plotbarh`                        Creates a horizontal bar plot.
:doc:`../plotbox`                         Creates a box plot.
:doc:`../plotcdfempirical`                Creats a cumulative distribution function (cdf) of the empirical distribution plot.
:doc:`../plotcontour`                     Creates a contour plot.
:doc:`../plotfreq`                        Calculates and plots the frequencies of categorical variables.
:doc:`../plothist`                        Calculates and creates a frequency histogram plot.
:doc:`../plothistf`                       Creates a histogram plot from a vector of frequencies.
:doc:`../plothistp`                       Calculates and creates a percentage frequency histogram plot.
:doc:`../plotloglog`                      Creates a 2-dimensional line plot with logarithmic scaling of the both the X and Y axes.
:doc:`../plotlogx`                        Creates a 2-dimensional line plot with logarithmic scaling of the X axis.
:doc:`../plotlogy`                        Creates a 2-dimensional line plot with logarithmic scaling of the Y axis.
:doc:`../plotpacf`                        Plots the partial autocorrelations function (PACF).
:doc:`../plotpolar`                       Creates a polar plot.
:doc:`../plotscatter`                     Creates a 2-dimensional scatter plot.
:doc:`../plotsurface`                     Creates a 3-dimensional surface plot.
:doc:`../plotts`                          Creates a graph of time series data.
:doc:`../plottshf`                        Plots high-frequency and irregularly spaced time series data.
:doc:`../plottslog`                       Creates a graph of time series data with the y-axis on a log scale.
:doc:`../plotxy`                          Creates a 2-dimensional line plot.
:doc:`../plotxyfill`                      Creates an area plot between sets of lines.
===================================    ============================================================================


Add graphs to existing canvas
--------------------------------

===================================    ============================================================================
:doc:`../plotaddarea`                     Adds a cumulative area plot to an existing 2-D graph.
:doc:`../plotaddbar`                      Adds a bar or a set of bars to an existing 2-D graph.
:doc:`../plotaddbarh`                     Adds a horizontal bar or a set of horizontal bars to an existing 2-D graph.
:doc:`../plotadderrorbar`                 Adds an error bar or a set of bars to an existing 2-D graph.
:doc:`../plotaddbox`                      Adds a box plot to an existing 2-D graph.
:doc:`../plotaddhist`                     Adds a histogram to an existing 2-D graph.
:doc:`../plotaddhistf`                    Adds a frequency histogram to an existing 2-D graph.
:doc:`../plotaddhistp`                    Adds a percent frequency histogram to an existing 2-D graph.
:doc:`../plotaddpolar`                    Adds a graph using polar coordinates to an existing polar graph.
:doc:`../plotaddscatter`                  Adds a set of points to an existing 2-D graph.
:doc:`../plotaddsurface`                  Adds a surface plot to an existing 3-D plot.
:doc:`../plotaddts`                       Adds a curve of time series data to an existing time series plot.
:doc:`../plotaddxy`                       Adds an XY plot to an existing 2-D graph.
:doc:`../plotaddxyfill`                   Adds an area plot between sets of lines to an existing 2-D plot.
===================================    ============================================================================

Spanning bars and lines
--------------------------

===================================    ============================================================================
:doc:`../plotaddhbar`                  Adds one or more horizontal bars spanning the full extent of the y-axis to an existing graph.
:doc:`../plotaddhline`                 Adds one or more horizontal lines spanning the full extent of the y-axis to an existing graph
:doc:`../plotaddvbar`                  Adds one or more vertical bars spanning the full extent of the y-axis to an existing graph.
:doc:`../plotaddvline`                 Adds one or more vertical lines spanning the full extent of the y-axis to an existing graph
===================================    ============================================================================


Color palettes
-------------------

===================================    ============================================================================
:doc:`../blendcolorpalette`               Create a new palette that blends between a list of colors. ncolors must be greater than the length of the 'colors' vector.
:doc:`../getcolorpalette`                 Retrieves a named color palette as a string array. Some names offer multiple palettes based on the number of colors requested. These generally range from a base of 3 to a maximum of 8-12 for color brewer palettes.
:doc:`../gethslpalette`                   Create a set of evenly spaced colors in HSL hue space. The h, s, and l arguments must all be between 0 and 1.
:doc:`../gethsluvpalette`                 Create a set of evenly spaced circular hues in the HSLuv system.
:doc:`../listcolorpalettes`               List available color palettes known by GAUSS.
===================================    ============================================================================


Subplots and size
-----------------------

===================================    ============================================================================
:doc:`../plotcanvassize`                  Controls the size of the canvas on which the next plot is drawn.
:doc:`../plotclearlayout`                 Clears any previously set plot layouts.
:doc:`../plotcustomlayout`                Plots a graph of user-specified size at a user-specified location.
:doc:`../plotlayout`                      Divides a plot into a grid of subplots and assigns the cell location in which to draw the next created graph.
===================================    ============================================================================


Graph windows
-------------------

===================================    ============================================================================
:doc:`../plotcloseall`                    Closes all open graph tabs.
:doc:`../plotopenwindow`                  Opens a new, empty graph whicow to be used by the next drawn graph.
:doc:`../plotsetnewwindow`                Sets whether or not graph should be drawn in the same window or a new window.
===================================    ============================================================================

Export and save
-------------------

===================================    ============================================================================
:doc:`../plotsave`                        Saves the last created graph to a user specified file type.
===================================    ============================================================================

Graph settings
------------------

===================================    ============================================================================
:doc:`../plotgetdefaults`                 Gets default settings for graph types.
===================================    ============================================================================

Title, legend  and text labels
+++++++++++++++++++++++++++++++++
===================================    ============================================================================
:doc:`../plotsetlegend`                   Adds a legend to a graph.
:doc:`../plotsetlegendbkd`                Sets the opacity and color for the background of a graph legend.
:doc:`../plotsetlegendborder`             Controls the color and thickness of the legend border.
:doc:`../plotsetlegendfont`               Set the legend font for a graph.
:doc:`../plotsetlegendtitle`              Controls the legend title.
:doc:`../plotsettextinterpreter`          Controls the text interpreter (LaTeX, HTML) settings for a graph.
:doc:`../plotsetticlabelfont`             Controls the font name, size and color for the X and Y axis tick labels.
:doc:`../plotsettitle`                    Controls the settings for the title for a graph.
:doc:`../plotsetxlabel`                   Controls the settings for the x-axis label on a graph.
:doc:`../plotsetylabel`                   Controls the settings for the y-axis label on a graph.
:doc:`../plotsetzlabel`                   Controls the settings for the z-axis label on a graph.
===================================    ============================================================================

Axes, grid and ticks
+++++++++++++++++++++++++++

===================================    ============================================================================
:doc:`../plotsetaxespen`                  Sets the color for the axes line.
:doc:`../plotsetgridpen`                  Controls the thickness, color, and style for the grid lines.
:doc:`../plotsetticposition`              Controls if the x and y-axis tick is inside or outside the axis lines.
:doc:`../plotsetoutlineenabled`           Turns on an outline around the plot.
:doc:`../plotsetticlabelfont`             Controls the font name, size and color for the X and Y axis tick labels.
:doc:`../plotsetwhichxaxis`               Assigns curves to the top or bottom x-axis.
:doc:`../plotsetwhichyaxis`               Assigns curves to the right or left y-axis.
:doc:`../plotsetxgridpen`                 Controls the thickness, color, and style for the grid lines from the x-axis.
:doc:`../plotsetxpen`                     Controls the thickness, color, and style for the x-axis line.
:doc:`../plotsetxminorticcount`           Controls the number of minor ticks to place between major ticks on the x-axis of a 2-D plot.
:doc:`../plotsetxrange`                   Sets the range for the x-axis.
:doc:`../plotsetxticinterval`             Controls the interval between x-axis tick labels and also allows the user to specify the first tick to be labeled for 2-D time series graphs.
:doc:`../plotsetxticlabel`                Controls the formatting and angle of x-axis tick labels for 2-D time series graphs.
:doc:`../plotsetxticposition`             Controls if the x-axis tick is inside or outside the x-axis line.
:doc:`../plotsetygridpen`                 Controls the thickness, color, and style for the grid lines from the y-axis.
:doc:`../plotsetyminorticcount`           Controls the number of minor ticks to place between major ticks on the y-axis of a 2-D plot.
:doc:`../plotsetypen`                     Controls the thickness, color, and style for the y-axis line.
:doc:`../plotsetyrange`                   Sets the range for the y-axis.
:doc:`../plotsetyticinterval`             Controls the interval between y-axis tick labels and also allows the user to specify the first tick to be labeled for 2-D time series graphs.
:doc:`../plotsetyticlabel`                Controls the formatting and angle of y-axis tick labels for 2-D graphs.
:doc:`../plotsetyticposition`             Controls if the y-axis tick is inside or outside the y-axis line.
===================================    ============================================================================

Line color, style and fill
++++++++++++++++++++++++++++++++

===================================    ============================================================================
:doc:`../plotsetbkdcolor`                 Sets background color of a graph.
:doc:`../plotsetcolormap`                 Sets the color maps for a surface or contour plot.
:doc:`../plotsetcontourlabels`            Sets the contour labels for a contour plot.
:doc:`../plotsetfill`                     Settings for the background grid of a plot.
:doc:`../plotsetlinepen`                  Sets line color, thickness and style.
:doc:`../plotsetlinesymbol`               Sets line symbols displayed on the plotted points of a graph.
:doc:`../plotsetzlevels`                  Controls the heights at which lines are drawn on a contour plot.
===================================    ============================================================================

Box and Bar settings
+++++++++++++++++++++++++

===================================    ============================================================================
:doc:`../plotsetjitterrange`           Adds a small random perturbation (jitter) to :doc:`../plotbox` outliers, or :doc:`../plotscatter` plots so that overlapping observations can be better seen.
:doc:`../plotsetbarwidth`              Sets the width of the bars in bar plots.
:doc:`../plotsetboxwidth`              Sets the width of the boxes in box plots.
===================================    ============================================================================


Contour settings
+++++++++++++++++++++

===================================    ============================================================================
:doc:`../plotsetcontourlabels`         Sets the format and precision of contour height labels.
:doc:`../plotsetzlabels`               Controls the heights at which lines are drawn on a contour plot.
===================================    ============================================================================

Annotations
----------------

===================================    ============================================================================
:doc:`../plotaddarrow`                 Adds an arrow to an existing graph.
:doc:`../plotaddshape`                 Adds an arrow, line, ellipse or rectangle to an existing graph.
:doc:`../plotaddtextbox`               Adds a textbox to an existing graph.
===================================    ============================================================================

Annotation settings
-----------------------

=====================================    ============================================================================
:doc:`../annotationgetdefaults`           Fills in an instance of a plotAnnotation structure with default values.
:doc:`../annotationsetbkd`                Sets the background color and transparency level for a textbox, rectangle or ellipse.
:doc:`../annotationsetfont`               Sets the font properties of a plotAnnotation structure for controlling text boxes added to a graph.
:doc:`../annotationsetlinecolor`          Sets the line color for textbox, rectangle or ellipse borders as well as the color for lines and arrows.
:doc:`../annotationsetlinestyle`          Sets the line style for textbox, rectangle or ellipse borders as well as the style for lines and arrows.
:doc:`../annotationsetlinethickness`      Sets the line thickness for textbox, rectangle or ellipse borders as well as the color for lines and arrows.
=====================================    ============================================================================
