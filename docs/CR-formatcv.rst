
formatcv
==============================================

Purpose
----------------

Sets the character data format used by printfmt.

Format
----------------
.. function:: formatcv(newfmt)

    :param newfmt: the new format specification.
    :type newfmt: 1x3 vector

    :returns: oldfmt (*1x3 vector*), the old format specification.

Examples
----------------
This example saves the old format, sets the format desired for
printing x, prints x, then restores
the old format. This code:

::

    x = { A 1, B 2, C 3 };
    oldfmt = formatcv("*.*s" ~ 3 ~ 3);
    call printfmt(x,0~1);
    call formatcv(oldfmt);

produces:

::

    A 1
     B 2
     C 3

Source
++++++

gauss.src

Globals
+++++++

\__fmtcv

.. seealso:: Functions :func:`formatnv`, :func:`printfm`, :func:`printfmt`
