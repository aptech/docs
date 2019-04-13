
ismiss
==============================================

Purpose
----------------

Returns a 1 if its matrix argument contains any missing values, otherwise returns a 0.

Format
----------------
.. function:: ismiss(x)

    :param x: data
    :type x: NxK matrix

    :returns: y (*scalar*), 1 if *x* contains any missing values, otherwise 0.

Remarks
-------

An element of *x* is considered to be a missing if and only if it contains
a missing value in the real part. Thus, if :math:`x = 1 + .i`, ``ismiss(x)`` will
return a 0.


Examples
----------------

::

    x = { 1, 2, 3, 4 };
    
    //Set the second element of 'x' to be a missing value
    x[2] = miss(0,0);
    
    print "before 'if' block, x = " x;
    
    //If there are any missing values in 'x'
    if ismiss(x);
       //Remove all rows with missing values from 'x'
       x = packr(x);
    endif;
    
    print "after 'if' block, x = " x;

::

    before 'if' block, x = 
           1.0000000 
                   . 
           3.0000000 
           4.0000000 
    after 'if' block, x = 
           1.0000000 
           3.0000000 
           4.0000000

To reset all missing values to a specified value, replace the call to :func:`packr`
above with a call to :func:`missrv`.

.. seealso:: Functions :func:`scalmiss`, :func:`miss`, :func:`missrv`, :func:`contains`

