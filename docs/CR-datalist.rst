
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

Remarks
-------

The variables are listed in an interactive mode. As many rows and
columns as will fit on the screen are displayed. You can use the cursor
keys to pan and scroll around in the listing.


Examples
----------------

::

    datalist freq age sex pay;

This command will display the variables age, sex, and pay
from the data set freq.dat.

Source
------

datalist.src

.. raw:: html

   </div>
