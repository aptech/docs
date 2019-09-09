
keep (dataloop)
==============================================

Purpose
----------------

Specifies columns (variables) to be saved to the output dataset in a data loop.

.. _keep:
.. index:: keep

Format
----------------

::

    keep variable_list;

Remarks
-------

Commas are optional in *variable_list*.

Retains only the specified variables in the output dataset. Any
variables referenced must already exist, either as elements of the
source dataset, or as the result of a previous `make`, `vector`, or `code`
statement.

If neither `keep` nor `drop` is used, the output dataset will contain all
variables from the source dataset, as well as any newly defined
variables. The effects of multiple `keep` and `drop` statements are
cumulative.


Examples
----------------

::

    keep age, pay, sex;

.. seealso:: `drop`

