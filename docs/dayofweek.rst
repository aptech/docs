
dayofweek
==============================================

Purpose
----------------

Returns day of week.

Format
----------------
.. function:: d = dayofweek(a)

    :param a: dates in DT format.
    :type a: Nx1 vector

    :return d: integers indicating day of week of each date:

        .. csv-table::
            :widths: auto

            "1", "Sunday"
            "2", "Monday"
            "3", "Tuesday"
            "4", "Wednesday"
            "5", "Thursday"
            "6", "Friday"
            "7", "Saturday"

    :rtype d: Nx1 vector

Remarks
-------

The DT scalar format is a double precision representation of the date
and time. In the DT scalar format, the number

::

   a = 20150415183207;

represents 18:32:07 or 6:32:07 PM on April 4, 2015.

::

   d = dayofweek(a);

After running above code, *d* is 4 which means Wednesday.



Examples
--------

::

    // April 15, 2015, 18:32:07
    a = 20150415183207;

    d = dayofweek(a);
    print d;

The code above produces the following output:

::

    4.0000000

The return value of 4 indicates Wednesday.

Source
------

time.src

.. seealso:: :func:`dtday`, :func:`dttime`, :func:`dtdate`, :func:`dttostr`
