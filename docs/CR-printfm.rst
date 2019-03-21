
printfm
==============================================

Purpose
----------------
Prints a matrix using a different format for each column of the matrix.

Format
----------------
.. function:: printfm(x, mask, fmt)

    :param x: 
    :type x: NxK matrix which is to be printed and which may contain both character and numeric data

    :param mask: ExE conformable with x,
        containing ones and zeros, which is used to
        specify whether the particular row,
        column, or element is to be printed as a
        character (0) or numeric (1) value.
    :type mask: LxM matrix

    :param fmt: 
    :type fmt: Kx3 or 1x3 matrix where each row specifies
        the format for the respective column of x

    :returns: y (*scalar*), 1 if the function is successful and 0 if it fails.

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
     
    d = printfm(x,mask,fmt);

::

    AGE 5.123, 2.2346E+00
    PAY 1.235, 1.2346E+00
    SEX 1.145, 3.4471E+00
    JOB 4.114, 8.5564E+00

When the column of x to be printed contains all
character elements, use a format string of "*.*s" if
you want it right-justified, or "-*.*s" if you want
it left-justified. If the column is mixed character
and numeric elements, then use the correct numeric
format and printfm will substitute a default format
string for those elements in the column that are
character.
Remember, the mask value controls whether an element
will be printed as a number or a character string.

.. seealso:: Functions :func:`print`, :func:`printdos`
