
blendColorPalette
==============================================

Purpose
----------------
Create a new palette that blends between a list of colors.

Format
----------------
.. function:: color_blend = blendColorPalette(colors, n_colors)

    :param colors:  List of existing colors.
    :type colors: Nx1 string array

    :param n_colors:  The number of colors to create for the new palette.
    :type n_colors: scalar

    :return color_blend: containing color palette.

    :rtype color_blend: n_colorsx1 string array

Format
----------------

::

    /*
    ** Make color palette with 5 colors
    ** blending red, green, and yellow
    */
    clrs = blendColorPalette("Red"$|"Green"$|"Yellow", 5);

The resulting colors :

::

    clrs = #ff0000
           #813f00
           #008000
           #80c000
           #ffff00

Remarks
----------------
*n_colors* must be greater than the length of the *colors* vector.

.. seealso:: :func:`getColorPalette`, :func:`listColorPalettes`, :func:`getHSLPalette`, :func:`getHSLuvPalette`
