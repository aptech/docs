
formatnv
==============================================

Purpose
----------------

Sets the numeric data format used by :func:`printfmt`.

Format
----------------
.. function:: formatnv(newfmt)

    :param newfmt: the new format specification.
    :type newfmt: 1x3 vector

    :returns: **oldfmt** (*1x3 vector*) - the old format specification.

Remarks
-------

See :func:`printfm` for details on the format vector.

Examples
----------------
This example saves the old format, sets the format desired for
printing *x*, prints *x*, then restores the
old format. This code:

::

    x = { A 1, B 2, C 3 };

    /*
    ** Set print format and save
    ** old format 
    */
    oldfmt = formatnv("*.*lf" ~ 8 ~ 4);

    call printfmt(x, 0~1);

    /*
    ** Set print format for printing
    ** back to old format
    */
    call formatnv(oldfmt);

::

     A   1.0000
     B   2.0000
     C   3.0000

Source
------

gauss.src

Globals
------------

`\__fmtnv`

.. seealso:: Functions :func:`formatcv`, :func:`printfm`, :func:`printfmt`
