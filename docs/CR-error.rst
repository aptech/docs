
error
==============================================

Purpose
----------------

Allows the user to generate a user-defined error
code which can be tested quickly with the :func:`scalerr`
function.

Format
----------------
.. function:: y = error(x)

    :param x: in the range 0-65535.
    :type x: scalar

    :returns: y (*scalar*) error code which can be interpreted as
        an integer with the :func:`scalerr` function.

Remarks
-------

* You can test to see if a variable is a scalar error code with the function :func:`scalmiss`. For example:
  ::

      // Create scalar error code
      x = error(4);

      // Check to see if 'x' is a scalar error code
      if scalmiss(x);
          // If it is a scalar error code, print
          // the error code
          print scalerr(x);
      endif;

* The user may assign any number in the range 0-65535 to denote particular
  error conditions. This number may be tested for as an error code by
  :func:`scalerr`.

* The :func:`scalerr` function will return the value of the error code and so is
  the reverse of error. These user-generated error codes work in the same
  way as the intrinsic GAUSS error codes which are generated automatically
  when :code:`trap 1` is on and certain GAUSS functions detect a numerical
  error such as a singular matrix.

::

    error(0);

is equal to the missing value code.


Examples
----------------

Basic usage
+++++++++++

::

    // Set 'err_code' to contain a scalar error
    // code, holding the value 28
    err_code = error(28);
    
    // Decode error code
    err_num = scalerr(err_code);
    
    print err_num;

The above code will print out the value:

::

    28

Example 2
+++++++++

The example below creates a simple procedure which computes the square root of positive inputs, but
returns a scalar error code for negative inputs.

::

    x_sqrt = mySqrt(-2);
    
    // Check to see if 'x_sqrt' is a scalar error code
    if scalmiss(x_sqrt);
        print "Error code returned with value: "$+ntos(scalerr(x_sqrt));
    else;
        print x_sqrt;
    endif;
    
    proc (1) = mySqrt(x);
        local ret;
        
        // If 'x' is negative, return
        // a scalar error code
        if x < 0;
            ret = error(12);
        else;
            ret = sqrt(x);
        endif;
        
        retp(ret);
    endp;

The code above will print out:

::

    Error code returned with value: 12

.. seealso:: Functions :func:`scalerr`, `trap`, `trapchk`

