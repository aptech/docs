
call
==============================================

Purpose
----------------

Calls a function or procedure when the returned
value is not needed and can be ignored, or when the
procedure is defined to return nothing.

.. _call:
.. index:: call

Format
----------------

::

    call function_name();
    call function_name(argument_list);

Examples
----------------

::

    // Create a positive definte matrix
    x = moment(rndn(100, 4), 0);

    // Call chol function
    call chol(x);

    // y is the determinant
    y = detl;

The above example is the fastest way to compute the
determinant of a positive definite matrix. The
result of :func:`chol` is discarded and *detl* is used to
retrieve the determinant that was computed during
the call to :func:`chol`.

Remarks
-------

This is useful when you need to execute a function or procedure and do
not need the value that it returns. It can also be used for calling
procedures that have been defined to return nothing.

*function_name* can be any intrinsic GAUSS function, a procedure (`proc`),
or any valid expression.

.. seealso:: keyword `proc`
