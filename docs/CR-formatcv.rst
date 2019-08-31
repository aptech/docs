
formatcv
==============================================

Purpose
----------------

Sets the character data format used by :func:`printfmt`.

Format
----------------
.. function:: oldfmt = formatcv(newfmt)

    :param newfmt: the new format specification.
    :type newfmt: 1x3 vector

    :return oldfmt: the old format specification.

    :rtype oldfmt: 1x3 vector

Remarks
-------

See :func:`printfm` for details on the format vector.


Examples
----------------
This example saves the old format, sets the format desired for
printing *x*, prints *x*, then restores
the old format. This code:

::

    // Create matrix with a mix of
    // character and numeric data
    x = { A 1, 
          B 2, 
          C 3 };

    // Set the global format control
    // for 'printfmt' and retrieve
    // the previous setting
    oldfmt = formatcv("*.*s" ~ 3 ~ 3);

    // Print the data with new format settings
    call printfmt(x, 0~1);

    // Reset the formatting to the original settings 
    call formatcv(oldfmt);

produces:

::

  A               1
  B               2
  C               3 

Source
------

gauss.src

Globals
-------

`\__fmtcv`

.. seealso:: Functions :func:`formatnv`, :func:`printfm`, :func:`printfmt`
