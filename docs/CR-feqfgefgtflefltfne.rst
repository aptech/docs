
feq,fge,fgt,fle,flt,fne
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use _fcmptol to fuzz the comparison operations to allow for roundoff error.

Format
----------------
.. function:: fne(a, b)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with  a.
    :type b: LxM matrix

    :returns: y (*scalar*), 1 (TRUE) or 0 (FALSE).

Remarks
-------

The return value is TRUE if every comparison is TRUE.

The statement:

::

   y = feq(a,b);

is equivalent to:

::

   y = a eq b;

For the sake of efficiency, these functions are not written to handle
missing values. If a and b contain missing values, use missrv to convert
the missing values to something appropriate before calling a fuzzy
comparison function.

The calling program can reset \_fcmptol before calling these procedures:

::

   _fcmptol = 1e-12;


Examples
----------------

::

    _fcmptol = 1e-12;
    
    x = rndu(2,2);
    
    y = x + 0.5*(_fcmptol);
    
    if fge(x,y);
       print "each element of x is greater than";
       print "or equal to each element of y";
    else;
       print "at least one element of x is less";
       print "its corresponding element in y";
    endif;

Source
------

fcompare.src

.. seealso:: Functions 

equal greater bigger less than not
