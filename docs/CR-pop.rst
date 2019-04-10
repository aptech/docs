
pop
==============================================

Purpose
----------------

Provides access to a last-in, first-out stack for matrices.

Format
----------------
.. function:: pop b 
			  pop a



Remarks
-------

This is used with gosub, goto, and return statements with parameters. It
permits passing parameters to subroutines or labels, and returning
parameters from subroutines.

The gosub syntax allows an implicit push statement. This syntax is
almost the same as that of a standard gosub, except that the matrices to
be push'ed "into the subroutine" are in parentheses following the label
name. The matrices to be push'ed back to the main body of the program
are in parentheses following the return statement. The only limit on the
number of matrices that can be passed to and from subroutines in this
way is the amount of room on the stack.

No matrix expressions can be executed between the (implicit) push and
the pop. Execution of such expressions will alter what is on the stack.

Matrices must be pop'ped in the reverse order that they are push'ed,
therefore in the statements:

::

   goto label(x,y,z);
    .
    .
    .
   label:
   pop c;
   pop b;
   pop a;

After the code above:

::

   c = z
   b = y
   a = x

Note that there must be a separate pop statement for each matrix popped.

.. seealso:: Functions `gosub`, `goto`, :func:`return`
