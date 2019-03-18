
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
