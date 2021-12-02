
setColDateFormats
==============================================

Purpose
----------------

Specifies how GAUSS should display dates using the BSD strftime format specifiers. Note that this will also convert the type of the columns specified by *column* to *Date*.

Format
----------------
.. function:: x_date = setColDateFormats(X, fmt, columns)

    :param X: data.
    :type X: NxK matrix or dateframe

    :param fmt: contains strftime date/time format characters.
    :type fmt: Mx1 string array

    :param columns: The names or indices of the date columns in *X* to set format of.
    :type columns: Mx1 scalar or string

    :return x_date: contains metadata assigning the date display format specified by *fmt* to the variables in *x* specified by *columns*.
    :rtype x_date: NxK dataframe


Examples
----------------

::


    // Load data
    fname = getGAUSSHome $+ "examples/xle_daily.xlsx";
    xle = loadd(fname, "date(Date) + Volume");

    // Print the first 2 observations
    print "Dates in original format:";
    print xle[1:2,.];

    // Set date format to month/day/Year
    xle_2 = setcoldateformats(xle, "%m/%d/%Y", "Date");

    // Print the first 2 observations
    print "";
    print "Dates in new format:";
    print xle_2[1:2,.];


The above code will print out:

::

    Dates in original format:
                Date          Volume
          2017-06-13        15807900
          2017-06-14        30280200

    Dates in new format:
                Date          Volume
          06/13/2017        15807900
          06/14/2017        30280200


Remarks
------------

You can find a list of the available date format specifiers in the Command Reference entry for :func:`posixtostrc`.

.. seealso:: Functions :func:`dftype`, :func:`getColDateFormats`
