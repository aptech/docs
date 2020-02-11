
sprintf
==============================================

Purpose
----------------

Converts numeric vectors, string vectors and their combinations into formatted strings.

Format
----------------
.. function:: s = sprintf(fmt, ...)

    :param fmt: A sprintf style format string.
    :type fmt: string 

    :param ....: One or more matrices or string arrays to add to the formatted string output.
    :type ....: NxK numeric or string vectors

    :return s: contains the formatted version of the input vectors.

    :rtype s: Nx1 string array

Format specifier basics
-------

:func:`sprintf` format strings use format specifiers to describe the desired formatting.

Format specifiers start with a percent sign and are followed by optional *flags*, *width* and *precision* and finally a required *type*.

::

    %[flags][width][.precision]type

For example:

::

    // Flags: +
    // Width: 8
    // Precision: .4
    // Type: f
    fmt = "%+8.4f";

In this example:

* The flag is ``+`` which forces all numbers to start with a + or -.
* The width is 8 which means that the number will be in a field 8 spaces wide.
* The precision, .4, specifies that 4 numbers will be shown after the decimal.
* The type is *f* which is decimal floating point format.

Using this format string:

::

    print sprintf(fmt, 3.1415926536);

will print out:

::

 +3.1416

Notice that there are 7 printed characters plus the initial space which make up the 8 character field width.



Supported Flags
-----------------

.. list-table::
    :widths: auto

    * - \-
      - Left-justify within the given field. Right justification is the default.
    * - \+
      - Precede all numbers with a plus or minus sign. By default only negative numbers start with a sign.
    * - (space) 
      - If no sign is written, include a blank space before the number.
    * - #
      - Used with type f, a decimal point will be written even if no numbers would follow. Used with o, b, or X the number will
        be preceded by a zero and then o, b, or X respectively.
    * - 0
      - Left-pads the number with zeros instead of spacing when padding is specified. See the width subs-specifier.

Supported Width
-----------------

.. list-table::
    :widths: auto

    * - (integer)
      - The minimum number of characters to print. If the value is shorter, the result is padded with blank spaces.
        Note that the value will not be truncated if it is longer.
    * - \*
      - The width will be passed in as an input before the input argument to be formatted.

Supported Precision
---------------------

.. list-table::
    :widths: auto

    * - (integer)
      - For integer specifiers (d,i,o,u,x,X), this is the minimum number of digits to print. If the value is shorter, the result is padded with leading zeros. The value is not truncated even if the result is longer.

        For floating point specifiers f and F, this is the number of digits after the decimal point.
        The default is 6 and the maximum is 15.

        For s this is the maximum number of characters to be printed. By default all characters will be printed.

        If the period is included without an explicit precision, a precision of zero is assumed.
    * - .\*
      - The precision will be passed in as an input before the input argument to be formatted.

Supported Types
-----------------

.. list-table::
    :widths: auto

    * - d or i 
      - Signed decimal integer.
    * - b 
      - Unsigned binary.
    * - f or F 
      - Decimal floating point.
    * - e or E 
      - Scientific-notation (exponential) floating point.
    * - g or G 
      - Scientific or decimal floating point--whichever is more compact.
    * - c 
      - Single character.
    * - s 
      - String of characters.
    * - %
      - Two consecutive % signs will write a single % character.


Examples
----------------

Basic single number examples 
+++++++++++++++++++++++++++++

::

    // Floating point. Default precision: 6 digits after decimal point
    s1 = sprintf("%f", pi);

    // Floating point or scientific notation, whichever
    // is more compact. Default precision: 6 significant digits
    s2 = sprintf("%g", pi);

    // Floating point with 4 digits after decimal point
    s3 = sprintf("%.4f", pi);

    // Print as an integer
    s4 = sprintf("%d", pi);

The above code will make the following assignments:

::

    s1 = "3.141593"
    s2 = "3.14159"
    s3 = "3.1416"
    s4 = "3"

Insert numbers into a string 
+++++++++++++++++++++++++++++

::

    // Floating point with 4 digits after decimal point
    s1 = sprintf("Pi is equal to %.4f", pi);

    // Floating point with 3 digits after decimal point
    s2 = sprintf("Pi is equal to %.3f (to 4 digits).", pi);

    // Insert two numbers into the format string
    s3 = sprintf("Pi is equal to %.5f (to %d digits).", pi, 6);

The above code will make the following assignments:

::

    s1 = "Pi is equal to 3.1416"
    s2 = "Pi is equal to 3.142 (to 4 digits)."
    s3 = "Pi is equal to 3.14159 (to 6 digits)."

Formatting numeric columns
+++++++++++++++++++++++++++

::

Each format specifier corresponds to a symbol. In our previous examples, these were scalars. In this example,
the format specifier will be used for all elements of a matrix.

::

    x = { 0.20530317    0.81596981,
          2.11547392   -0.22456817,
         0.084284295   11.14733020 };

    // Use default field width and precision
    s1 = sprintf("%f", x);

The above code will create a 3x1 string array with inadequate spacing:

::

         "0.2053030.815970"
    s1 = "2.115474-0.224568"
         "0.08428411.147330"

To make a more readable matrix, we need to increase the field width for each number like this:

::

    // Increase field width to 10 characters
    // for each element in the matrix.
    s2 = sprintf("%10f", x);

This results in a string array which is more readable:

::

        "  0.205303  0.815970"
   s2 = "  2.115474 -0.224568"
        "  0.084284 11.147330"

Since we set the field width to 10, each number in the above string array is aligned to the right of a space which is 10 characters wide.

Here are some more examples using the same *x*:

::

    // Floating point format with field width of 8
    // and precision of 4 (4 digits after decimal).
    s3 = sprintf("%8.4f", x);

    // Floating point or scientific notation, whichever
    // is more compact. Field with of 8 and precision
    // of 4 (4 significant digits).
    s4 = sprintf("%8.4g", x);

    // Scientific notation with field width of 10
    // and precision of 2 (2 digits after decimal).
    s5 = sprintf("%10.2e", x);


The above code will result in the following assignments:

::

         "  0.2053  0.8160" 
    s3 = "  2.1155 -0.2246"
         "  0.0843 11.1473"

         "  0.2053  0.8160"
    s4 = "   2.115 -0.2246"
         " 0.08428   11.15"

         "  2.05e-01  8.16e-01"
    s5 = "  2.12e+00 -2.25e-01"
         "  8.43e-02  1.11e+01"




.. seealso:: Functions :func:`ftocv`, :func:`stof`, `format`
