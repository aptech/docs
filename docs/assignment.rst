
assignment
==============================================

Purpose
----------------

Assigns a value to a variable.

Format
----------------

::

    variable = expression

Parameters
----------------

    :param variable: Name of the variable to assign to.
    :type variable: symbol

    :param expression: Value to assign.
    :type expression: any type

Examples
----------------

Basic Assignment
++++++++++++++++

::

    x = 5;
    y = { 1, 2, 3 };
    name = "GAUSS";

Multiple Assignment
+++++++++++++++++++

::

    // Assign multiple variables from procedure return
    { mean, std } = meanstd(x);

Indexed Assignment
++++++++++++++++++

::

    x = zeros(5, 1);
    x[1:3] = { 10, 20, 30 };

::

    x =   10.0000000
          20.0000000
          30.0000000
           0.0000000
           0.0000000

Remarks
-------

- Assignment creates a new variable if it doesn't exist, or overwrites the existing value.
- Inside procedures, use ``local`` to declare local variables.
- Multiple return values from procedures can be assigned using brace notation.

.. seealso:: Keywords ``local``, ``let``
