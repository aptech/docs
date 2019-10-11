
outtyp (dataloop)
==============================================

Purpose
----------------

Specifies the precision of the output dataset.

Format
----------------
.. function:: outtyp num_constant

    :param num_constant: precision of output dataset.
    :type num_constant: scalar

Examples
----------------

::

    outtyp 8;

Remarks
-------

*num_constant* must be 2, 4, or 8, to specify integer, single precision,
or double precision, respectively.

If :func:`outtyp` is not specified, the precision of the output dataset will be
that of the input dataset. If character data is present in the data
set, the precision will be forced to double.


