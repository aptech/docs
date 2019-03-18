
call
==============================================

Purpose
----------------

Calls a function or procedure when the returned
value is not needed and can be ignored, or when the
procedure is defined to return nothing.

Format
----------------
.. function:: call function_name(argument_list)call function_name

Examples
----------------

::

    // Create a positive definte matrix				
    x = moment(rndn(100,4),0); 
    // Call chol function 								
    call chol(x);
    // y is the determinant 				 
    y = detl;

The above example is the fastest way to compute the
determinant of a positive definite matrix. The
result of chol is discarded and detl is used to
retrieve the determinant that was computed during
the call to chol.

.. seealso:: Functions :func:`proc`
