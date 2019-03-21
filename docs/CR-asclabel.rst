
asclabel
==============================================

Purpose
----------------
To set up character labels for the X and Y axes. NOTE: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: asclabel(xl, yl)

    :param xl: labels for the tick marks on the X axis. Set to 0 if no character labels for this axis are desired.
    :type xl: string or Nx1 character vector

    :param yl: labels for the tick marks on the Y axis. Set to 0 if no character labels for this axis are desired.
    :type yl: string or Mx1 character vector

Examples
----------------

This illustrates how to label the X axis with the months of the year:

::

    library pgraph;				
    let lab = JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC;
    asclabel(lab, 0);

This will also work:

::

    lab = "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC";
    asclabel(lab, 0);

If the string format is used, then escape characters may be embedded
in the labels. For example, the following produces character labels
that are multiples of :math:`λ`. The font Simgrma must be previously
loaded in a fonts command.

::

    fonts("simplex simgrma");
    lab = "\2010.25\202l \2010.5\202l \2010.75\202l l";
    asclabel(lab, 0);

Here, the "\\202l" produces the ":math:`λ`" symbol from Simgrma.

Source
------------

pgraph.src

.. seealso:: Functions :func:`xtics`, :func:`ytics`, :func:`scale`, :func:`scale3d`, :func:`fonts`

