
if, else, elseif, endif
==============================================

Purpose
----------------

Controls program flow with conditional branching.

.. _if:
.. _else:
.. _elseif:
.. _endif:
.. index:: if, else, elseif, endif

Format
----------------

::

    if scalar_expression;
        ...
    elseif scalar_expression;
        ...
    elseif scalar_expression;
        ...
    else;
        ...
    endif;

Remarks
-------

*scalar_expression* is any expression that returns a scalar. It is ``TRUE`` if
it is not zero, and ``FALSE`` if it is zero.

A list of statements is any set of GAUSS statements.

GAUSS will test the expression after the `if` statement. If it is ``TRUE``
(nonzero), then the first list of statements is executed. If it is ``FALSE``
(zero), then GAUSS will move to the expression after the first `elseif`
statement, if there is one, and test it. It will keep testing
expressions and will execute the first list of statements that
corresponds to a ``TRUE`` expression. If no expression is ``TRUE``, then the
list of statements following the `else` statement is executed. After the
appropriate list of statements is executed, the program will go to the
statement following the `endif` and continue on.

`if` statements can be nested.

One `endif` is required per `if` statement. If an `else` statement is used,
there may be only one per `if` statement. There may be as many `elseif`'s as
are required. There need not be any `elseif`'s or any `else` statement
within an `if` statement.

Note the semicolon after the `else` statement.


Examples
----------------

::

    if x < 0;
       y = -1;
    elseif x > 0;
       y = 1;
    else;
       y = 0;
    endif;

.. seealso:: keywords `do until`, `do while`

