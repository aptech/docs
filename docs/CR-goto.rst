
goto
==============================================

Purpose
----------------

Causes a branch to a label.

Format
----------------
.. function:: goto label 
			       . 
			       . 
			       . 
			  label:

Remarks
-------

Label names can be any legal GAUSS names up to 32 alphanumeric
characters, beginning with an alphabetic character or an underscore, not
a reserved word.

Labels are always followed immediately by a colon.

Labels do not have to be declared before they are used. GAUSS knows they
are labels by the fact that they are followed immediately by a colon.

When GAUSS encounters a goto statement, it jumps to the specified label
and continues execution of the program from there.

Parameters can be passed in a goto statement the same way as they can
with a gosub.


Examples
----------------

::

    x = seqa(.1,.1,5);
    n = { 1 2 3 };
    goto  fip;
    print x;
    end;
     
    fip:
    print n;

::

    1.0000000 2.0000000 3.0000000

.. seealso:: Functions :func:`gosub`, :func:`if`
