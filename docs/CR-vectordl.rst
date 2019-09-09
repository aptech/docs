
vector (dataloop)
==============================================

Purpose
----------------
Specifies the creation of a new variable within a data loop.

Format
----------------
.. function:: vector # numvar = numeric_expression
              vector # numvar = character_expression

Remarks
-------

A numeric_expression is any valid expression returning a numeric value.
A character_expression is any valid expression returning a character
value. If neither '$' nor '#' is specified, '#' is assumed.

vector is used in place of make when the expression returns a scalar
rather than a vector. vector forces the result of such an expression to
a vector of the correct length. vector could actually be used anywhere
that make is used, but would generate slower code for expressions that
already return vectors.

Any variables referenced must already exist, either as elements of the
source dataset, as extern's, or as the result of a previous make,
vector, or code statement.


Examples
----------------

::

    vector const = 1;

.. seealso:: Functions 
