
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
    :p:   (*scalar*) number of periods to lag.

**Returns**

    :nv: (*string*) name of the new lagged variable.

Remarks
-------

You can specify any number of variables to lag. Each variable can be
lagged a different number of periods. Both positive and negative lags
are allowed.

Lagging is executed before any other transformations. If the new
variable name is different from that of the variable to lag, the new
variable is first created and appended to a temporary dataset. This
temporary dataset becomes the input dataset for the dataloop, and is
then automatically deleted.
