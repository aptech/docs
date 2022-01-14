Graphics
===================

Graph types
----------------------

===================================    ============================================================================
:doc:`plotarea`                        Creates a cumulative area plot.
:doc:`plotbar`                         Creates a bar plot.
:doc:`plotbox`                         Creates a box plot.
:doc:`plotcdfempirical`                Creats a cumulative distribution function (cdf) of the empirical distribution plot.
:doc:`plotcontour`                     Creates a contour plot.
:doc:`plothist`                        Calculates and creates a frequency histogram plot.
:doc:`plothistf`                       Creates a histogram plot from a vector of frequencies.
:doc:`plothistp`                       Calculates and creates a percentage frequency histogram plot.
:doc:`plotloglog`                      Creates a 2-dimensional line plot with logarithmic scaling of the both the X and Y axes.
:doc:`plotlogx`                        Creates a 2-dimensional line plot with logarithmic scaling of the X axis.
:doc:`plotlogy`                        Creates a 2-dimensional line plot with logarithmic scaling of the Y axis.
:doc:`plotpolar`                       Creates a polar plot.
:doc:`plotscatter`                     Creates a 2-dimensional scatter plot.
:doc:`plotsurface`                     Creates a 3-dimensional surface plot.
:doc:`plotts`                          Creates a graph of time series data.
:doc:`plottshf`                        Plots high-frequency and irregularly spaced time series data.
:doc:`plottslog`                       Creates a graph of time series data with the Y-axis on a log scale.
:doc:`plotxy`                          Creates a 2-dimensional line plot.
===================================    ============================================================================


Add graphs to existing canvas
--------------------------------
===================================    ============================================================================
:doc:`plotaddarea`                     Adds a cumulative area plot to an existing 2-D graph.
:doc:`plotaddbar`                      Adds a bar or a set of bars to an existing 2-D graph.
:doc:`plotadderrorbar`                 Adds an error bar or a set of bars to an existing 2-D graph.
:doc:`plotaddbox`                      Adds a box plot to an existing 2-D graph.
:doc:`plotaddhist`                     Adds a histogram to an existing 2-D graph.
:doc:`plotaddhistf`                    Adds a frequency histogram to an existing 2-D graph.
:doc:`plotaddhistp`                    Adds a percent frequency histogram to an existing 2-D graph.
:doc:`plotaddpolar`                    Adds a graph using polar coordinates to an existing polar graph.
:doc:`plotaddscatter`                  Adds a set of points to an existing 2-D graph.
:doc:`plotaddsurface`                  Adds a surface plot to an existing 3-D plot.
:doc:`plotaddts`                       Adds a curve of time series data to an existing time series plot.
:doc:`plotaddxy`                       Adds an XY plot to an existing 2-D graph.
===================================    ============================================================================


Color palletes
-------------------

===================================    ============================================================================
:doc:`blendcolorpalette`               Create a new palette that blends between a list of colors. ncolors must be greater than the length of the 'colors' vector.
:doc:`getcolorpalette`                 Retrieves a named color palette as a string array. Some names offer multiple palettes based on the number of colors requested. These generally range from a base of 3 to a maximum of 8-12 for color brewer palettes.
:doc:`gethslpalette`                   Create a set of evenly spaced colors in HSL hue space. The h, s, and l arguments must all be between 0 and 1.
:doc:`gethsluvpalette`                 Create a set of evenly spaced circular hues in the HSLuv system.
:doc:`listcolorpalettes`               List available color palettes known by GAUSS.
===================================    ============================================================================


Subplots and size
-----------------------

===================================    ============================================================================
:doc:`plotcanvassize`                  Controls the size of the canvas on which the next plot is drawn.
:doc:`plotclearlayout`                 Clears any previously set plot layouts.
:doc:`plotcustomlayout`                Plots a graph of user-specified size at a user-specified location.
:doc:`plotlayout`                      Divides a plot into a grid of subplots and assigns the cell location in which to draw the next created graph.
:doc:`plotopenwindow`                  Opens a new, empty graph whicow to be used by the next drawn graph.
===================================    ============================================================================

Export and save
-------------------

===================================    ============================================================================
:doc:`plotsave`                        Saves the last created graph to a user specified file type.
===================================    ============================================================================

Graph settings
------------------

===================================    ============================================================================
:doc:`plotgetdefaults`                 Gets default settings for graph types.
:doc:`plotsetaxespen`                  Sets the color for the axes line.
:doc:`plotsetbar`                      Sets the fill style and format of bars in a histogram or bar graph.
:doc:`plotsetbkdcolor`                 Sets background color of a graph.
:doc:`plotsetcolormap`                 Sets the color maps for a surface or contour plot.
:doc:`plotsetcontourlabels`            Sets the contour labels for a contour plot.
:doc:`plotsetfill`                     Settings for the background grid of a plot.
:doc:`plotsetgrid`                     Controls the settings for the background grid of a plot.
:doc:`plotsetlegend`                   Adds a legend to a graph.
:doc:`plotsetlegendbkd`                Sets the opacity and color for the background of a graph legend.
:doc:`plotsetlegendfont`               Set the legend font for a graph.
:doc:`plotsetlinecolor`                Sets line colors for a graph.
:doc:`plotsetlinestyle`                Sets line styles for a graph.
:doc:`plotsetlinesymbol`               Sets line symbols displayed on the plotted points of a graph.
:doc:`plotsetlinethickness`            Sets line thickness for a graph.
:doc:`plotsetnewwindow`                Sets whether or not graph should be drawn in the same window or a new window.
:doc:`plotsettextinterpreter`          Controls the text interpreter settings for a graph.
:doc:`plotsetticlabelfont`             Controls the font name, size and color for the X and Y axis tic labels.
:doc:`plotsettitle`                    Controls the settings for the title for a graph.
:doc:`plotsetwhichyaxis`               Assigns curves to the right or left Y-axis.
:doc:`plotsetxlabel`                   Controls the settings for the X-axis label on a graph.
:doc:`plotsetxrange`                   Sets the range for the X-axis.
:doc:`plotsetxticcount`                Controls the number of major tics on the X-axis of a 2-D plot.
:doc:`plotsetxticinterval`             Controls the interval between X-axis tic labels and also allows the user to specify the first tic to be labeled for 2-D time series graphs.
:doc:`plotsetxticlabel`                Controls the formatting and angle of X-axis tic labels for 2-D time series graphs.
:doc:`plotsetylabel`                   Controls the settings for the Y-axis label on a graph.
:doc:`plotsetyrange`                   Sets the range for the y-axis.
:doc:`plotsetyticcount`                Controls the number of major tics on the y-axis of a 2-D plot.
:doc:`plotsetyticlabel`                Controls the formatting and angle of Y-axis tick labels for 2-D graphs.
:doc:`plotsetzlabel`                   Controls the settings for the Z-axis label on a graph.
:doc:`plotsetzlevels`                  Controls the heights at which lines are drawn on a contour plot.
===================================    ============================================================================

Annotation settings
-----------------------

===================================    ============================================================================
:doc:`annotationgetdefaults`           Fills in an instance of a plotAnnotation structure with default values.
:doc:`annotationsetbkd`                Sets the background color and transparency level for a textbox, rectangle or ellipse.
:doc:`annotationsetfont`               Sets the font properties of a plotAnnotation structure for controlling text boxes added to a graph.
:doc:`annotationsetlinecolor`          Sets the line color for textbox, rectangle or ellipse borders as well as the color for lines and arrows.
:doc:`annotationsetlinestyle`          Sets the line style for textbox, rectangle or ellipse borders as well as the style for lines and arrows.
:doc:`annotationsetlinethickness`      Sets the line thickness for textbox, rectangle or ellipse borders as well as the color for lines and arrows.
===================================    ============================================================================
