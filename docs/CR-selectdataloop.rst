
select (dataloop)
==============================================

Purpose
----------------
Selects specific rows (observations) in a data loop based on a
logical expression.

Format
----------------
.. function:: select logical_expression

Examples
----------------

::

    select age > 40 AND sex $== 'MALE';

.. seealso:: Functions 
