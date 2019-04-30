
trap
==============================================

Purpose
----------------
Sets the trap flag to enable or disable trapping of numerical errors.

Format
----------------
.. function:: trap val 
			  trap val, mask

    :param val: new trap value.
    :type val: scalar

    :param mask: optional mask to allow leaving some bits of the trap flag unchanged.
    :type mask: scalar

Examples
----------------

First we will create some code that will return an error, stopping the program. Then we will show how to trap and handle the error:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a singular matrix
    x = { 1 1 1,
          1 1 1,
          1 1 1 };
    
    // Attempt to calculate inverse, but error
    //'matrix singular' stops program
    x_inv = inv(x);

In some cases, we would like our program to be able to detect certain errors and recover from them. The next section of code will be the same as above, with the exception of setting the trap flag. We will see that it will not cause an error.

::

    // Create a singular matrix
    x = { 1 1 1,
          1 1 1,
          1 1 1 };
    
    // Set the trap flag, to supress the error
    trap 1;
    
    // Attempt to calculate inverse
    x_inv = inv(x);

If you run the above code, you will notice that an error was not returned. With the trap set to 1, instead of stopping the program with an error message, GAUSS will set the variable x_inv equal to a scalar error code. A scalar error code is a missing value that contains an integer which can be used to identify the error. For more information on error codes, see scalerr and error. In this example, however, our main concern is with determining whether or not the return value is a scalar error code. We can do this with the GAUSS function, scalmiss.

::

    // Create a singular matrix
    x = { 1 1 1,
          1 1 1,
          1 1 1 };
    
    // Set the trap flag, to supress the error
    trap 1;
    
    // Attempt to calculate inverse
    x_inv = inv(x);
    
    // Check to see if 'x_inv', contains a scalar error code
    if scalmiss(x_inv);
        print  "matrix was singular";
    endif;

This example will built from the concepts in the example above to do something more useful.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

   // Create a coefficient matrix with linear dependencies
   x = { 1 1 0.8,
         1 1 1.5,
         1 1 0.6 };

   // Create a dependent variable
   y = { -0.36, 
         -1.55, 
         -0.02 };

   // Set the trap flag, to supress the error
   trap 1;

   // Attempt to compute the inverse of the moment matrix
   mmi = inv(x'x);

   // Check to see if 'mmi', contains a scalar error code
   if scalmiss(mmi);
       // Compute the pseudo-inverse of the moment matrix
       mmi = pinv(x'x);
   endif;

   // Solve the linear equations
   b_hat = mmi * x'y;

After the above code, b_hat is equal to:

::

    0.5
    0.5
   -1.7

Remarks
-------

The trap flag is examined by some functions to control error handling.
There are 16 bits in the trap flag, but most GAUSS functions will
examine only the lowest order bit:

+-------------+-------------------+
| **trap 1;** | turn trapping on  |
+-------------+-------------------+
| **trap 0;** | turn trapping off |
+-------------+-------------------+

If we extend the use of the trap flag, we will use the lower order bits
of the trap flag. It would be wise for you to use the highest 8 bits of
the trap flag if you create some sort of user-defined trap mechanism for
use in your programs. (See the function trapchk for detailed
instructions on testing the state of the trap flag; see error for
generating user-defined error codes.)

To set only one bit and leave the others unchanged, use two arguments:

+---------------+--------------------+
| **trap 1,1;** | set the ones bit   |
+---------------+--------------------+
| **trap 0,1;** | clear the ones bit |
+---------------+--------------------+

.. seealso:: Functions :func:`scalerr`, :func:`trapchk`, :func:`error`
