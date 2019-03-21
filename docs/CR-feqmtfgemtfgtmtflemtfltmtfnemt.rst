
feqmt,fgemt,fgtmt,flemt,fltmt,fnemt
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use the fcmptol argument to fuzz the comparison operations to allow
for roundoff error.

Format
----------------
.. function:: fnemt(a, b, fcmptol)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with  a.
    :type b: LxM matrix

    :param fcmptol: comparison tolerance.
    :type fcmptol: scalar

    :returns: y (*scalar*), 1 (TRUE) or 0 (FALSE).

Remarks
-------

The return value is TRUE if every comparison is TRUE.

The statement:

::

   y = feqmt(a,b,1e-15);

is equivalent to:

::

   y = a eq b;

For the sake of efficiency, these functions are not written to handle
missing values. If a and b contain missing values, use missrv to convert
the missing values to something appropriate before calling a fuzzy
comparison function.


Examples
----------------

::

    tol = 1e-12;
    
    x = rndu(2,2);
    
    y = x + 0.5*(tol);
    
    if fgemt(x,y,tol);
       print "each element of x is greater than";
       print "or equal to each element of y";
    else;
       print "at least one element of x is less";
       print "its corresponding element in y";
    endif;

Source
------

fcomparemt.src

.. seealso:: Functions 
