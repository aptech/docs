
outtyp (dataloop)
==============================================

Purpose
----------------

Specifies the precision of the output data set.

Format
----------------
.. function:: outtyp num_constant

    :param num_constant: precision of output data set.
    :type num_constant: scalar

Remarks
-------

num_constant must be 2, 4, or 8, to specify integer, single precision,
or double precision, respectively.

If outtyp is not specified, the precison of the output data set will be
that of the input data set. If character data is present in the data
set, the precision will be forced to double.


Examples
----------------

::

    outtyp 8;

