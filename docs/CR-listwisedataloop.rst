
listwise (dataloop)
==============================================

Purpose
----------------

Controls listwise deletion of missing values.

.. _listwise:
.. index:: listwise

Format
----------------

::

    listwise [[read]] [[write]];

Remarks
-------

If *read* is specified, the deletion of all rows containing missing values
happens immediately after reading the input file and before any
transformations. If *write* is specified, the deletion of missing values
happens after any transformations and just before writing to the output
file. If no `listwise` statement is present, rows with missing values are
not deleted.

The default is *read*.

