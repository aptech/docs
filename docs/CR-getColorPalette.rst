
getColorPalettes
==============================================

Purpose
----------------
Retrieves a named color palette as a string array. Some names offer multiple palettes based on the number of colors requested. These generally range from a base of 3 to a maximum of 8-12 for color brewer palettes.

Format
----------------
.. function:: getColorPalette(name, ncolors)

    :param name:  The name of the color palette. The full set of built-in color palettes can be seen here. The list of palettes can be queried with listColorPalettes().
    :type name: string

    .. csv-table::
        :widths: auto

        "Valid options include:   * denotes colorblind friendly palette.col-md-1 {   text-align: right; }#color-chips rect {  stroke: #333;  stroke-width: .5px;}SpectralRdYlGnRdBu*PiYG*PRGn*RdYlBu*BrBG*RdGyPuOr*Set2*AccentDark2*Pastel2Pastel1Set1Set3Paired*YlOrRd*OrRd*PuBu*BuPu*Oranges*BuGn*YlOrBr*YlGn*Reds*RdPu*Greens*YlGnBu*Purples*GnBu*Greys*PuRd*Blues*PuBuGn*viridismagmainfernoplasma"

    :param ncolors:  Optional. The desired number of colors for a specific palette. Default value is 6. If 'ncolors' is fewer than the minimum number of colors offered by a palette, then the minimum will be returned with a warning. The same behavior occurs when 'ncolors' is greater than the maximum number of colors a palette supports.
    :type ncolors: scalar

    :returns: clrs (*ncolors x 1 string array*) of hex values for each color in the palette.

Examples
----------------
Example: Basic Usage

::

    //Get the first 3 colors from the ColorBrewer 'Dark2' palette
    clrs = getColorPalette("Dark2", 3);

After the above code, clrs should equal:

::

    #1b9e77 
    #d95f02 
    #7570b3

clrs
GAUSS
plotSet

.. seealso:: Functions :func:`listColorPalettes`, :func:`getHSLPalette`, :func:`getHSLuvPalette`, :func:`blendColorPalette`
