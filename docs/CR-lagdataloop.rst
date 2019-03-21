
lag (dataloop)
==============================================

Purpose
----------------

Lags variables a specified number of periods.

Format
----------------
.. function:: var2:p2...]]

    :param var: 
    :type var: name of the variable to lag

    :param p: number of periods to lag.
    :type p: scalar constant

    :returns: nv (*TODO*), name of the new lagged variable.



Remarks
-------

You can specify any number of variables to lag. Each variable can be
lagged a different number of periods. Both positive and negative lags
are allowed.

Lagging is executed before any other transformations. If the new
variable name is different from that of the variable to lag, the new
variable is first created and appended to a temporary data set. This
temporary data set becomes the input data set for the dataloop, and is
then automatically deleted.

