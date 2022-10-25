
between
==============================================

Purpose
----------------
Returns a binary matrix with a 1 if the corresponding element of X is between 'a' and 'b', with an option to specify
whether the ends are inclusive.

Format
----------------
.. function:: mask = between(X, left, right [, inclusive])

    :param x: Data.
    :type x: NxK matrix or dataframe.

    :param left: Lower limit of the range.
    :type left: 1x1 matrix or dataframe.

    :param right: Upper limit of the range.
    :type right: 1x1 matrix or dataframe.

    :param inclusive: Optional argument, specifies which limits are included in range. Default = ``"both"``. Options are:


        ========= ==============================================================
        "left"     Include lower limit only.
        "right"    Include upper limit only.
        "neither"  Do not include either limit.
        "both"     Include both limits.
        ========= ==============================================================


    :type inclusive: string

    :return mask: Equal to 1 if the corresponding element of X is in the specified range, otherwise a 0.
    :rtype mask: NxK matrix

Examples
----------------

::

    x  = { 100 200 300,
           40  50  60,
           7   8   9 };

    left = 25;

    right = 125;

    between(x, left, right);

The above code prints the following matrix to screen:

::

     1.0000000        0.0000000        0.0000000
     1.0000000        1.0000000        1.0000000
     0.0000000        0.0000000        0.0000000

.. seealso:: Functions :func:`recode`, :func:`counts`, :func:`reclassify`
