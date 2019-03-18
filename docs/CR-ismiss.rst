
ismiss
==============================================

Purpose
----------------

Returns a 1 if its matrix argument contains any missing
values, otherwise returns a 0.

Format
----------------
.. function:: ismiss(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*scalar*), 1 if x contains any missing values, otherwise 0.

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

To reset all missing values to a specified value, replace the call to packr
above with a call to  missrv.

.. seealso:: Functions :func:`scalmiss`, :func:`miss`, :func:`missrv`, :func:`contains`
