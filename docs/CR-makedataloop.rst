
make (dataloop)
==============================================

Purpose
----------------

Specifies the creation of a new variable within a data loop.


.. _make:
.. index:: make

Format
----------------

::

    make [#] numvar = numeric_expression;
    make $charvar = character_expression;

Remarks
-------

A *numeric_expression* is any valid expression returning a numeric vector.
A *character_expression* is any valid expression returning a character
vector. If neither '``$``' nor '``#``' is specified, '``#``' is assumed.

The expression may contain explicit variable names and/or GAUSS
commands. Any variables referenced must already exist, either as
elements of the source dataset, as `extern`'s, or as the result of a
previous `make`, `vector`, or `code` statement. The variable name must be
unique. A variable cannot be made more than once, or an error is
generated.


Examples
----------------

::

    make sqvpt = sqrt(velocity * pressure * temp);
    make $ gender = lower(gender);

.. seealso:: Functions `vector`

