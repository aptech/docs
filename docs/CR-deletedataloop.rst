
delete (dataloop)
==============================================

Purpose
----------------

Removes specific rows in a data loop based on a logical expression.

Format
----------------
.. function:: delete logical_expression

Examples
----------------

::

    delete age < 40 or sex == 'FEMALE';

Remarks
-------

Deletes only those rows for which logical_expression is ``TRUE``. Any
variables referenced must already exist, either as elements of the
source dataset, as `extern`'s, or as the result of a previous make,
vector, or code statement.

GAUSS expects *logical_expression* to return a row vector of 1's and 0's.
The relational and other operators (e.g. ``<``) are already interpreted in
terms of their dot equivalents (``.<``), but it is up to the user to make
sure that function calls within *logical_expression* result in a vector.


.. seealso:: Function `select`

