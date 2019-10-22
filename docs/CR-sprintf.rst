
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

    :param ....: One or more numeric or string vectors to add to the formatted string output.
    :type ....: Nx1 numeric or string vectors

    :return s: contains the formatted version of the input vectors.

    :rtype s: Nx1 string array

Format specifier basics
-------

:func:`sprintf` format specifiers start with a percent sign and are followed by optional *flags*, *width* and *precision* and finally a required *type*.

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
    * - u 
      - Unsigned decimal integer.
    * - b 
      - Unsigned binary.
    * - o 
      - Unsigned octal.
    * - x 
      - Unsigned hexadecimal (lower case).
    * - X 
      - Unsigned hexadecimal (upper case).
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

.. seealso:: Functions :func:`ftocv`, :func:`stof`, :func:`format`
