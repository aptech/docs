
ftos
==============================================

Purpose
----------------

Converts a scalar into a string containing the decimal character representation of that number.

Format
----------------
.. function:: y = ftos(x, fmat, field, prec)

    :param x: the number to be converted.
    :type x: scalar

    :param fmat: the format string to control the conversion.
    :type fmat: string

    :param field: the minimum field width. If *field* is 2x1, it
        specifies separate field widths for the real and imaginary parts of *x*.
    :type field: scalar or 2x1 vector

    :param prec: the number of places following
        the decimal point. If *prec* is 2x1, it specifies
        separate precisions for the real and imaginary parts of *x*.
    :type prec: scalar or 2x1 vector

    :return x_str: contains the decimal character equivalent of *x* in the format specified.

    :type x_str: string

Remarks
-------

The format string corresponds to the :code:`format /jnt` (justification,
notation, trailing character) slash parameter as follows:

.. list-table::
    :widths: auto

    * - */rdn*
      - :code:`"%\*.\*lf"`
    * - */ren*
      - :code:`"%\*.\*lE"`
    * - */ron*
      - :code:`"%#\*.\*lG"`
    * - */rzn*
      - :code:`"%\*.\*lG"`
    * - */ldn*
      - :code:`"%- \*.\*lf"`
    * - */len*
      - :code:`"%- \*.\*lE"`
    * - */lon*
      - :code:`"%-# \*.\*lG"`
    * - */lzn*
      - :code:`"%- \*.\*lG"`

If *x* is complex, you can specify separate formats for the real and
imaginary parts by putting two format specifications in the format
string. You can also specify separate fields and precisions. You can
position the sign of the imaginary part by placing a ``+`` between the two
format specifications. If you use two formats, no ``i`` is appended to the
imaginary part. This is so you can use an alternate format if you
prefer, for example, prefacing the imaginary part with a ``j``.

The format string can be a maximum of 80 characters.

If you want special characters to be printed after *x*, include them as
the last characters of the format string.


For example:

.. list-table::
    :widths: auto

    * - :code:`"%*.*lf,"`
      - right-justified decimal followed by a comma.
    * - :code:`"%-*.*s "`
      - left-justified string followed by a space.
    * - :code:`"%*.*lf"`
      - right-justified decimal followed by nothing.

 	You can embed the format specification in the middle of other text:

        ::

            "Time: %*.*lf seconds."

        If you want the beginning of the field padded with zeros, then put a ``0`` before the first ``*`` in the format string:

    * - :code:`"%0*.*lf"`
      - right-justified decimal.

 	If :math:`prec = 0`, the decimal point will be suppressed.

Examples
----------------
You can create custom formats for complex numbers with :func:`ftos`. For example,

::

    let c = 24.56124+6.3224e-2i;

    field = 1;
    prec = 3|5;
    fmat = "%lf + j%le is a complex number.";
    cc = ftos(c, fmat, field, prec);

results in

::

    cc = "24.561 + j6.32240e-02 is a complex number."

Some other things you can do with :func:`ftos`:

::

    let x = 929.857435324123;
    let y = 5.46;
    let z = 5;

    field = 1;
    prec = 0;
    fmat = "%*.*lf";
    zz = ftos(z, fmat, field, prec);

    field = 1;
    prec = 10;
    fmat = "%*.*lE";
    xx = ftos(x, fmat, field, prec);

    field = 7;
    prec = 2;
    fmat = "%*.*lf seconds";
    s1 = ftos(x, fmat, field, prec);
    s2 = ftos(y, fmat, field, prec);

    field = 1;
    prec = 2;
    fmat = "The maximum resistance is %*.*lf ohms.";
    om = ftos(x, fmat, field, prec);

The results:

::

    zz = "5"

    xx = "9.2985743532E+002"

    s1 = "929.86 seconds"

    s2 = "5.46 seconds"

    om = "The maximum resistance is 929.86 ohms."

.. seealso:: Functions :func:`ftocv`, :func:`stof`, :func:`format`
