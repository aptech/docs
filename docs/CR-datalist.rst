
datalist
==============================================

Purpose
----------------

List selected variables from a data set.

Format
----------------
.. function:: datalist dataset [[var 1 [[var 2 ...]]]]

    :param dataset: name of the data set.
    :type dataset: literal

    :param var#: the names of the variables to list.
    :type var#: literal

Global Input
------------

.. data:: __range

    scalar, the range of rows to list. The default is all rows.

.. data:: __miss

    scalar, controls handling of missing values.

    .. csv-table::
        :widths: auto

        0, "display rows with missing values."
        1, "do not display rows with missing values."


    The default is 0.

.. data:: __prec

    scalar, the number of digits to the right of the decimal point to display. The default is 3.

Remarks
-------

The variables are listed in an interactive mode. As many rows and
columns as will fit on the screen are displayed. You can use the cursor
keys to pan and scroll around in the listing.


Examples
----------------

::

    datalist freq age sex pay;

This command will display the variables ``age``, ``sex``, and ``pay`` from the data set freq.dat.

Source
------

datalist.src

