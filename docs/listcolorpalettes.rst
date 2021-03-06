
listColorPalettes
==============================================

Purpose
----------------
List available color palettes known by GAUSS.

Format
----------------
.. function:: palettes = listColorPalettes(category)

    :param category: List only color palettes that are defined as being part of the specified category.
        Some palettes do not have categories.

        Valid categories include:

        - ``""`` (list all available palettes)
        - ``"diverging"``
        - ``"qualitative"``
        - ``"sequential"``

    :type category: string

    :return palettes: containing color palette names.

    :rtype palettes: string array

Examples
----------------

List palettes in 'qualitative' category
+++++++++++++++++++++++++++++++++++++++

::

    p = listColorPalettes("qualitative");

After the above code, *p* should equal:

::

     Accent
     Dark2
     Paired
     Pastel1
     Pastel2
     Set1
     Set2
     Set3

Print all available palettes
++++++++++++++++++++++++++++

The following code will print a list of all available color palettes:

::

    print listColorPalettes("");

Remarks
-------

By default these are located in the :file:`colorpalettes` directory inside of
the GAUSS installation directory. Additional color palette files can be
added here that will be loaded by GAUSS for use inside a program.
Palettes can be defined to be associated with a specific "category", and
queried specifically using the corresponding argument.

.. seealso:: Functions :func:`getColorPalette`, :func:`getHSLPalette`, :func:`getHSLuvPalette`, :func:`blendColorPalette`
