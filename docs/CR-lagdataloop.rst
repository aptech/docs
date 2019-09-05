
lag (dataloop)
==============================================

Purpose
----------------

Lags variables a specified number of periods.


.. _lag:
.. index:: lag

Format
----------------

::

    lag nv1 = var1: p1 [[nv2 = var2:p2...]];

**Parameters:**

    :var: (*string*) name of the variable to lag
    :p:   (*scalar constant*) number of periods to lag.

    :return nv: name of the new lagged variable.
    :rtype nv: string

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
