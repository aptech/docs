
erf,erfc
==============================================

Purpose
----------------

Computes the Gaussian error function (erf) and its
complement (erfc).

Format
----------------
.. function:: erf(x) 
			  erfc(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*NxK matrix*) .

Remarks
-------

The erf and erfc functions are closely related to the Normal
distribution:

::

   if x > 0
      cdfn(x) = 0.5 * (1 + erf(x / sqrt(2));

   if x ≤ 0
      cdfn(x) = 0.5 * erfc(-x / sqrt(2)); 


Examples
----------------

::

    //Print 3 digits after the decimal point
    format /rd 5,3;
    
    x = { .5 .4 .3,
          .6 .8 .3 };
    y = erf(x);
    yc = erfc(x);
    
    //The '~' operator performs horizontal concatenation
    //and causes this print statement to format 'x', 
    //'y' and 'yc' as if they were one 2x9 matrix rather 
    //than 3 2x3 matrices
    //This does not change the variable values, only 
    //their appearance for this print statement
    print x~y~yc;

produces the following output:

::

    0.500 0.400 0.300 0.520 0.428 0.329 0.480 0.572 0.671
    0.600 0.800 0.300 0.604 0.742 0.329 0.396 0.258 0.671

.. seealso:: Functions :func:`cdfN`, :func:`cdfNc`

Technical Notes
+++++++++++++++

erf and erfc are computed by summing the appropriate series and
continued fractions. They are accurate to about 12 or more digits.

complement Gaussian error function
