
print
==============================================

Purpose
----------------

Prints matrices, arrays, strings and string arrays to the screen and/or auxiliary output.

.. _print:
.. index:: print

Format
----------------

::


    print list_of_expressions;
    print [[/typ]] [[/fmted]] [[/mf]] [[/jnt]] list_of_expressions[[;]];

**Parameters**

:list_of_expressions: (*any*) GAUSS expressions that produce matrices, arrays, stings, or string arrays
    and/or names of variables to print, separated by spaces.

:/typ: (*literal*) symbol type flag.

    ====================== =====================================================
    */mat*, */sa*, */str*  Indicate which symbol types you are setting the output format for:
                           matrices and arrays (*/mat*), string arrays (*/sa*), and/or strings
                           (*/str*). You can specify more than one ``/`` *typ* flag; the format
                           will be set for all types indicated. If no ``/`` *typ* flag is listed,
                           `print` assumes */mat*.
    ====================== =====================================================

:/fmted: (*literal*) enable formatting flag.

    ============== ===================================================
    */on*, */off*  Enable/disable formatting. When formatting is disabled, the contents of a
                   variable are dumped to the screen in a "raw" format. */off* is currently
                   supported only for strings. "Raw" format for strings means that the entire
                   string is printed, starting at the current cursor position. When formatting is
                   enabled for strings, they are handled the same as string arrays. This shouldn't
                   be too surprising, since a string is actually a 1x1 string array.
    ============== ===================================================

:/mf: (*literal*) matrix format. It controls the way rows of a matrix are separated from one another. The possibilities are:

    ================ =================================================
    */m0*            no delimiters before or after rows when printing out matrices.
    */m1* or */mb1*  print 1 carriage return/line feed pair before each row of a matrix with more than 1 row.
    */m2* or */mb2*  print 2 carriage return/line feed pairs before each row of a matrix with more than 1 row.
    */m3* or */mb3*  print "Row 1", "Row 2"... before each row of a matrix with more than one row.
    */ma1*           print 1 carriage return/line feed pair after each row of a matrix with more than 1 row.
    */ma2*           print 2 carriage return/line feed pairs after each row of a matrix with more than 1 row.
    */a1*            print 1 carriage return/line feed pair after each row of a matrix.
    */a2*            print 2 carriage return/line feed pairs after each row of a matrix.
    */b1*            print 1 carriage return/line feed pair before each row of a matrix.
    */b2*            print 2 carriage return/line feed pairs before each row of a matrix.
    */b3*            print "Row 1", "Row 2"... before each row of a matrix.
    ================ =================================================

:/jnt: (*literal*) controls justification, notation, and the trailing character.

    **Right-Justified**

    ====== =======================================================
    */rd*  Signed decimal number in the form [[-]]####.####, where #### is
           one or more decimal digits. The number of digits before the decimal
           point depends on the magnitude of the number, and the number of digits
           after the decimal point depends on the precision. If the precision is 0,
           no decimal point will be printed.
    */re*  Signed number in the form [[-]]#.##E±###, where # is one decimal digit,
           ## is one or more decimal digits depending on the precision, and ### is three
           decimal digits. If precision is 0, the form will be [[-]]#E±### with no decimal
           point printed.
    */ro*  This will give a format like */rd* or */re* depending on which is most compact
           for the number being printed. A format like */re* will be used only if the exponent
           value is less than -4 or greater than the precision. If a */re* format is used,
           a decimal point will always appear. The precision signifies the number
           of significant digits displayed.
    */rz*  This will give a format like */rd* or */re* depending on which is most compact
           for the number being printed. A format like */re* will be used only if the
           exponent value is less than -4 or greater than the precision. If a */re*
           format is used, trailing zeros will be supressed and a decimal point will appear
           only if one or more digits follow it. The precision signifies the number of significant
           digits displayed.
    ====== =======================================================

    **Left-Justified**

    ====== =======================================================
    */ld*  Signed decimal number in the form [[-]] ####.####, where #### is one or
           more decimal digits. The number of digits before the decimal point depends
           on the magnitude of the number, and the number of digits after the decimal
           point depends on the precision. If the precision is 0, no decimal point will
           be printed. If the number is positive, a space character will replace the
           leading minus sign.
    */le*  Signed number in the form [[-]]#.##E±###, where # is one decimal digit, ## is
           one or more decimal digits depending on the precision, and ### is three decimal
           digits. If precision is 0, the form will be [[-]]#E±### with no decimal point
           printed. If the number is positive, a space character will replace the leading minus sign.
    */lo*  This will give a format like */ld* or */le* depending on which is most compact for the
           number being printed. A format like /le will be used only if the exponent value is
           less than -4 or greater than the precision. If a */le* format is used, a decimal point
           will always appear. If the number is positive, a space character will replace the
           leading minus sign. The precision specifies the number of significant digits displayed.
    */lz*  This will give a format like */ld* or */le* depending on which is most compact for the
           number being printed. A format like */le* will be used only if the exponent value is less
           than -4 or greater than the precision. If a */le* format is used, trailing zeros will be
           supressed and a decimal point will appear only if one or more digits follow it.
           If the number is positive, a space character will replace the leading minus sign.
           The precision specifies the number of significant digits displayed.
    ====== =======================================================

    **Trailing Character**

    The following characters can be added to the */jnt* parameters above to control the trailing character if any:

    ::

        format /rdn 1,3;

    .. list-table::
        :widths: auto

        * - *s*
          - The number will be followed immediately by a space character. This is the default.
        * - *c*
          - The number will be followed immediately by a comma.
        * - *t*
          - The number will be followed immediately by a tab character.
        * - *n*
          - No trailing character.

            The default when GAUSS is first started is:

            ::

                format /m1 /ro 16,8;

        * - *;;*
          - Double semicolons following a `print` statement will suppress the final carriage return/line feed.

Examples
----------------

Print a matrix
++++++++++++++

::

    x = { 1 2,
          3 4 };
    print x;

::

    1.0000000        2.0000000
    3.0000000        4.0000000

Print an expression
+++++++++++++++++++

::

    x = 3;
    print (x + 2);

returns:

::

    5.0000000

.. NOTE:: Notice the parentheses in the code above. Remember that `print` statements in GAUSS take
    a space separated list of items to print. The parentheses tell GAUSS to first evaluate
    the expression and then print the result. Without the parentheses (i.e. ``print x + 2;``),
    the statement would tell GAUSS to print a list of three items (first ``print x``, then
    ``print +``, and finally ``print 2``. Since the second item in that list is an operator
    (the ``+`` sign), an error will occur.

Example 3
+++++++++

::

    x = rndn(3, 3);
    format /rd 16,8;
    print x;

returns:

::

          0.14357994  -1.39272762  -0.91942414
          0.51061645  -0.02332207  -0.02511298
         -1.04675893  -1.04988540   0.07992059

Scientific notation
+++++++++++++++++++

::

    format /re 12,2;
    print x;

returns:

::

      1.44E-001  -1.39E+000  -9.19E-001
      5.11E-001  -2.33E-002  -2.51E-002
     -1.55E+000  -1.05E+000   7.99E-002

Append commas
+++++++++++++

::

    x = rndn(3, 3);
    format /rd 16,8;
    print x;

returns:

::

          0.14357994,  -1.39272762,  -0.91942414,
          0.51061645,  -0.02332207,  -0.02511298,
         -1.04675893,  -1.04988540,   0.07992059,

Add row numbers
+++++++++++++++

::

     print /rd /m3 x;

returns:

::

     Row 1
           0.14       -1.39       -0.92
     Row 2
           0.51       -0.02       -0.03
     Row 3
          -1.55       -1.05        0.08

.. NOTE:: This example does not specify the precision and spacing, so you may see more decimal places printed if that is your default setting

Printing character data
+++++++++++++++++++++++

Character data is text inside a GAUSS matrix. To print elements of a matrix as characters, you need to
prepend the dollar sign (``$``) to the name of the variable you want to print. In most cases,
string arrays are recommended over character matrices..

::

    x = { AGE, PAY, SEX };
    format /m1 8,8;
    print $x;

::

     AGE
     PAY
     SEX

Remarks
-------

The list of expressions MUST be separated by spaces. In `print`
statements, because a space is the delimiter between expressions, NO
SPACES are allowed inside expressions unless they are within index
brackets, quotes, or parentheses.

The printing of special characters is accomplished by the use of the
backslash (``\\``) within double quotes. The options are:

+-------------------+-----------------------------------------------------+
| *\\b*             | backspace (ASCII 8)                                 |
+-------------------+-----------------------------------------------------+
| *\\e*             | escape (ASCII 27)                                   |
+-------------------+-----------------------------------------------------+
| *\\f*             | form feed (ASCII 12)                                |
+-------------------+-----------------------------------------------------+
| *\\g*             | beep (ASCII 7)                                      |
+-------------------+-----------------------------------------------------+
| *\\l*             | line feed (ASCII 10)                                |
+-------------------+-----------------------------------------------------+
| *\\r*             | carriage return (ASCII 13)                          |
+-------------------+-----------------------------------------------------+
| *\\t*             | tab (ASCII 9)                                       |
+-------------------+-----------------------------------------------------+
| *\\###*           | the character whose ASCII value is "###"            |
|                   | (decimal).                                          |
+-------------------+-----------------------------------------------------+

Thus, *\\13\\10* is a carriage return/line feed sequence. The first three
digits will be picked up here. So if the character to follow a special
character is a digit, be sure to use three digits in the escape
sequence. For example: *\\0074* will be interpreted as 2 characters (ASCII
7, "4")

An expression with no assignment operator is an implicit `print` statement.

If ``output on`` has been specified, then all subsequent `print` statements
will be directed to the auxiliary output as well as the window. (See
output.) The `locate` statement has no effect on what will be sent to the
auxiliary output, so all formatting must be accomplished using tab
characters or some other form of serial output.

If the name of the symbol to be printed is prefixed with a ``$``, it is
assumed that the symbol is a matrix of characters.

::

    print $x;

Note that GAUSS makes no distinction between matrices containing
character data and those containing numeric data, so it is the
responsibility of the user to use functions which operate on character
matrices only on those matrices containing character data.

These matrices of character strings have a maximum of 8 characters per
element. A precision of 8 or more should be set when printing out
character matrices or the elements will be truncated.

Complex numbers are printed with the sign of the imaginary half
separating them and an "i" appended to the imaginary half. Also, the
current field width setting (see `format`) refers to the width of field
for each half of the number, so a complex number printed with a field of
8 will actually take (at least) 20 spaces to print.

`print`'ing a sparse matrix results in a table of the non-zero values
contained in the sparse matrix, followed by their corresponding row and
column indices, respectively.

A `print` statement by itself will cause a blank line to be printed:

::

   print;


.. seealso:: Functions :func:`printfm`, :func:`printdos`
