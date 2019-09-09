
select (dataloop)
==============================================

Purpose
----------------
Selects specific rows (observations) in a data loop based on a logical expression.

.. _select:
.. index:: select

Format
----------------

::

    select logical_expression;

Remarks
-------

Selects only those rows for which *logical_expression* is ``TRUE``. Any
variables referenced must already exist, either as elements of the
source dataset, as `extern`'s, or as the result of a previous `make`,
`vector`, or `code` statement.

Examples
----------------

::

    select age > 40 AND sex $== 'MALE';

.. seealso:: `delete`

