
format
==============================================

Purpose
----------------

Controls the format of matrices and numbers printed out with print statements.

Format
----------------
.. function:: format [[/typ]] [[/fmted]] [[/mf]] [[/jnt]] [[f,p]]

    :param /typ: symbol type flag(s). Indicate which symbol types you are setting the output format for.
    :type /typ: literal

    .. csv-table::
        :widths: auto

        "/mat, /sa, /str", "Formatting parameters are maintained separately for matrices and arrays (/mat), string arrays (/sa), and strings (/str).You can specify more than one /typ flag; the format will be set for all types indicated. If no /typ flag is listed, format assumes /mat."

    :param /fmted: enable formatting flag.
    :type /fmted: literal

    .. csv-table::
        :widths: auto

        "/on, /off", "Enable/disable formatting. When formatting is disabled, the contentsof a variable are dumped to the screen in a "raw" format./off is currently supported only for strings. "Raw" format for stringsmeans that the entire string is printed, starting at the currentcursor position. When formatting is enabled for strings, they arehandled the same as string arrays. This shouldn't be too surprising,since a string is actually a 1x1 string array."

    :param /mf: matrix row format flag.
    :type /mf: literal

    .. csv-table::
        :widths: auto

        "/m0", "no delimiters before or after rows when printing out matrices."
        "/m1 or /mb1", "print 1 carriage return/line feed pair before each row of a matrix with more than 1 row."
        "/m2 or /mb2", "print 2 carriage return/line feed pairs before each row of a matrix with more than 1 row."
        "/m3 or /mb3", "print ''Row 1'', ''Row 2''... before each row of a matrix with more than one row."
        "/ma1", "print 1 carriage return/line feed pair after each row of a matrix with more than 1 row."
        "/ma2", "print 2 carriage return/line feed pairs after each row of a matrix with more than 1 row."
        "/a1", "print 1 carriage return/line feed pair after each row of a matrix."
        "/a2", "print 2 carriage return/line feed pairs after each row of a matrix."
        "/b1", "print 1 carriage return/line feed pair before each row of a matrix."
        "/b2", "print 2 carriage return/line feed pairs before each row of a matrix."
        "/b3", "print ''Row 1'', ''Row 2''... before each row of a matrix."

    :param /jnt: matrix element format flag - controls justification, notation and trailing character.
    :type /jnt: literal

    .. csv-table::
        :widths: auto

        "Right-Justified"
        "/rd", "Signed decimal number in the form ####.####, where #### is one or more decimal digits. The number of digits before the decimal point depends on themagnitude of the number, and the number of digits after the decimal point depends on the precision. If theprecision is 0, no decimal point will be printed."
        "/re", "Signed number in the form #.##E±###,where # is one decimal digit, ## is one or more decimaldigits depending on the precision, and ### is three decimal digits. If precision is 0, the form will be[-]#E±### with no decimal point printed."
        "/ro", "This will give a format like /rd or /re depending on whichis most compact for the number being printed. A format like /re will be used only if the exponent value is less than -4 or greater than the precision. If a /re format is used,a decimal point will always appear. The precision signifies the number of significant digits displayed."
        "/rz", "This will give a format like /rd or /re depending on which is most compact for the number being printed. A format like /re will be used only if the exponent value is less than -4 or greater than the precision. If a /re format is used,trailing zeros will be supressed and a decimal point will appear only if one or more digits follow it. Theprecision signifies the number of significant digits displayed."
        "Left-Justified"
        "/ld", "Signed decimal number in the form [-]####.####, where #### is one or more decimal digits. The number of digits before the decimal point depends on the magnitude of the number, and the number of digits after the decimal point depends on the precision. If the precision is 0, no decimal point will be printed. If the number is positive, a space character will replace the leading minus sign."
        "/le", "Signed number in the form [-]#.##E±###, where # is one decimal digit, ## is one or more decimal digits depending on the precision, and ### is three decimal digits. If precision is 0, the form will be [-]#E±### with no decimal point printed. If the number is positive, a space character will replace the leading minus sign."
        "/lo", "This will give a format like /ld or /le depending on which is most compact for the number being printed. A format like /le will be used only if the exponent value is less than -4 or greater than the precision. If a /le format is used, a decimal point will always appear. If the number is positive, a space character will replace the leading minus sign. The precision specifies the number of significant digits displayed."
        "/lz", "This will give a format like /ld or /le depending on whichis most compact for the number being printed. A format like /le will be used only if the exponent value is less than -4 or greater than the precision. If a /le format is used, trailing zeros will be supressed and a decimal point will appear only if one or more digits follow it. If the number is positive, a space character will replace the leading minus sign. The precision specifies the number of significant digits displayed."
        "Trailing CharacterThe following characters can be added to the /jnt parametersabove to control the trailing character if any:                            format /rdn 1,3;"
        "s", "The number will be followed immediately by a space character. This is the default."
        "c", "The number will be followed immediately by a comma."
        "t", "The number will be followed immediately by a tab character."
        "n", "No trailing character."

    :param f: controls the field width.
    :type f: Scalar expression

    :param p: controls the precision.
    :type p: Scalar expression

Examples
----------------
For the examples below we will use a matrix elements of different magnitudes to more clearly show the differences between the different formatting options. This code will create that matrix:

::

    rndseed 642354;
    x = rndn(3,3);
    x[2,2] = x[2,2] .* 1e8;
    x[1,1] = x[1,1] .* 1e-12;
    x[3,1] = x[3,1] .* 1e-3;

::

    // GAUSS default format
    format /m1 /ros 16,8;
    print x;

::

    -1.1777603e-12      -0.92450840      -0.39442934 
        -0.023389275        70796411.       0.19679620 
      -0.00076864628       0.47818734      -0.13173939

::

    // r: right justified d: decimal
    // 16: field width is 16 places
    // 8: print 8 digits after the decimal point
    format /rd 16,8;
    print x;

::

    0.00000000      -0.92450840      -0.39442934 
         -0.02338927 70796411.12351108       0.19679620 
         -0.00076865       0.47818734      -0.13173939

As mentioned in the Remarks section, if the number is too large to fit in the field, the field size will be ignored. The [2,2] element in the matrix above, needs a field width of 17 to print the 8 places after the decimal plus the 8 in front of the decimal and one for the decimal place. This causes the [2,3] element to be bumped over 1 space.

::

    // r: right justified. 
    // z: decimal or scientific notation, whichever is more compact.
    // 16: field width is 16 places
    // 4: 4 digits after the decimal point, or 4 significant digits.
    format /m3 /rz 16,4;
    print x;

::

    Row 1
          -1.178e-12          -0.9245          -0.3944 
    Row 2
            -0.02339         7.08e+07           0.1968 
    Row 3
          -0.0007686           0.4782          -0.1317

::

    // m1: single new line after each row.
    // l: left-justified.
    // z: decimal or scientific notation, whichever is more compact.
    // 12: field width is 12 places
    // 4: 4 digits after the decimal point, or 4 significant digits.
    format /m1 /lz 12,4;
    print x;

::

    -1.178e-12   -0.9245      -0.3944      
    -0.02339      7.08e+07     0.1968      
    -0.0007686    0.4782      -0.1317

::

    // r: right-justified.
    // e: scientific notation.
    // c: follow each element with a comma.
    // 12: field width is 12 places
    // 4: 4 significant digits.
    format /rec 12,4;
    print x;

print

::

    -1.1778e-12, -9.2451e-01, -3.9443e-01,
     -2.3389e-02,  7.0796e+07,  1.9680e-01,
     -7.6865e-04,  4.7819e-01, -1.3174e-01,

.. seealso:: Functions :func:`formatcv`, :func:`formatnv`, :func:`print`, :func:`output`
