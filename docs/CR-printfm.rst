
printfm
==============================================

Purpose
----------------
Prints a matrix using a different format for each column of the matrix.

Format
----------------
.. function:: retcode = printfm(x, mask, fmt)

    :param x: matrix which is to be printed and which may contain both character and numeric data
    :type x: NxK matrix

    :param mask: ExE conformable with *x*,
        containing ones and zeros, which is used to
        specify whether the particular row,
        column, or element is to be printed as a
        character (0) or numeric (1) value.
    :type mask: LxM matrix

    :param fmt: matrix where each row specifies the format for the respective column of *x*
    :type fmt: Kx3 or 1x3 matrix

    :return retcode: 1 if the function is successful and 0 if it fails.

    :rtype retcode: scalar

Examples
----------------
Here is an example of printfm being used to print a
mixed numeric and character matrix:

::

    let x[4,3] = "AGE" 5.12345564 2.23456788
                 "PAY" 1.23456677 1.23456789
                 "SEX" 1.14454345 3.44718234
                 "JOB" 4.11429432 8.55649341;

    let mask[1,3] = 0 1 1;      /* character numeric numeric */
    let fmt[3,3] = "-*.*s " 8 8 /* first column format */
    "*.*lf," 10 3               /* second column format */
    "*.*le " 12 4;              /* third column format */

    d = printfm(x, mask, fmt);

::

    AGE 5.123, 2.2346E+00
    PAY 1.235, 1.2346E+00
    SEX 1.145, 3.4471E+00
    JOB 4.114, 8.5564E+00

When the column of *x* to be printed contains all
character elements, use a format string of "\*.\*s" if
you want it right-justified, or "-\*.\*s" if you want
it left-justified. If the column is mixed character
and numeric elements, then use the correct numeric
format and `printfm` will substitute a default format
string for those elements in the column that are
character.

Remember, the mask value controls whether an element
will be printed as a number or a character string.

Remarks
-------

The mask is applied to the matrix *x* following the rules of standard
element-by-element operations. If the corresponding element of mask is
0, then that element of *x* is printed as a character string of up to 8
characters. If mask contains a 1, then that element of *x* is assumed to
be a double precision floating point number.

The contents of *fmt* are as follows:

============== =============== =============================
:math:`[K,1]`  format string,  a string 8 characters maximum.
:math:`[K,2]`  field width,    a number < 80.
:math:`[K,3]`  precision,      a number < 17.
============== =============== =============================

The format strings correspond to the format slash commands as follows:

======= ==============
*/rdn*  "\*.\*lf"
*/ren*  "\*.\*lE"
*/ron*  "#\*.\*lG"
*/rzn*  "\*.\*lG"
*/ldn*  "- \*.\*lf"
*/len*  "- \*.\*lE"
*/lon*  "-# \*.\*lG"
*/lzn*  "- \*.\*lG"
======= ==============

Complex numbers are printed with the sign of the imaginary half
separating them and an "i" appended to the imaginary half. The field
width refers to the width of field for each half of the number, so a
complex number printed with a field of 8 will actually take (at least)
20 spaces to print.

If the :math:`precision = 0`, the decimal point will be suppressed.

The format string can be a maximum of 8 characters and is appended to a
``%`` sign and passed directly to the ``fprintf`` function in the standard C
language I/O library. The *lf*, etc., are case sensitive. If you know C,
you will easily be able to use this.

If you want special characters to be printed after *x*, then include them
as the last characters of the format string. For example:

=========== =========================================
"\*.\*lf,"  right-justified decimal followed by a comma.
"-\*.\*s "  left-justified string followed by a space.
"\*.\*lf"   right-justified decimal followed by nothing.
=========== =========================================

If you want the beginning of the field padded with zeros, then put a "0"
before the first "``*``" in the format string:

=========== =========================
"0\*.\*lf"  right-justified decimal.
=========== =========================

.. seealso:: Functions :func:`print`, :func:`printdos`
