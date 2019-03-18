
error
==============================================

Purpose
----------------

Allows the user to generate a user-defined error
code which can be tested quickly with the scalerr
function.

Format
----------------
.. function:: error(x)

    :param x: in the range 0-65535.
    :type x: scalar

    :returns: y (*TODO*), scalar error code which can be interpreted as
        an integer with the scalerr function.

Examples
----------------

Basic usage
+++++++++++

::

    //Set 'err_code' to contain a scalar error
    //code, holding the value 28
    err_code = error(28);
    
    //Decode error code
    err_num = scalerr(err_code);
    
    print err_num;

The above code will print out the value:

::

    28

The procedure syminv, below, returns error code 99 if the matrix is not
symmetric. If invpd fails, it returns error code 20. If
inv fails, it returns error code 50. The original trap state is
restored before the procedure returns.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    proc syminv(x);
       local oldtrap,y;
    
       //Check to see if 'x' is symmetric
       if not x == x';
          retp(error(99));
       endif;
    
       //Store current error trap state
       oldtrap = trapchk(0xffff);
    
       //Turn on trapping of errors
       trap 1;
    
       //Attempt matrix inversion with 'invpd'
       y = invpd(x);
    
       //Attempt inversion with 'inv' if
       //'invpd' returned an error code
       if scalerr(y);
          y = inv(x);
       endif;
    
       //Reset trap state 
       trap oldtrap,0xffff;
    
       retp(y);
    endp;

.. seealso:: Functions :func:`scalerr`, :func:`trap`, :func:`trapchk`
