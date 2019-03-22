
drop (dataloop)
==============================================

Purpose
----------------

Specifies columns to be dropped from the output data set in a data loop.

Format
----------------
.. function:: drop variable_list

Remarks
-------

Commas are optional in *variable_list*.

Deletes the specified variables from the output data set. Any variables
referenced must already exist, either as elements of the source data
set, or as the result of a previous :func:`make`, :func:`vector`, or :func:`code` statement.

If neither :func:`keep` nor :func:`drop` is used, the output data set will contain all
variables from the source data set, as well as any defined variables.
The effects of multiple keep and drop statements are cumulative.

Examples
----------------

::

    drop age, pay, sex;

.. seealso:: Functions 

