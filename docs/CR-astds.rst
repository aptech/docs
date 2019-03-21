
astds
==============================================

Purpose
----------------
Computes the biased standard deviation of the elements across one dimension of an N-dimensional array.

Format
----------------
.. function:: astds(x, dim)

    :param x: 
    :type x: N-dimensional array

    :param dim: number of dimension to sum across.
    :type dim: scalar

    :returns: y (N-dimensional array), standard deviation across specified dimension of *x*.

Remarks
-------

The output *y*, will have the same sizes of dimensions as *x*, except that
the dimension indicated by *dim* will be collapsed to 1.

This function essentially computes:

.. math:: σ=1n⁢×∑i=1n(Xi−μ)2

Thus, the divisor is *N* rather than *N-1*, where *N* is the number of
elements being summed. See astd for the alternate definition.

Examples
----------------

::

    a = areshape(25*rndn(16,1),4|2|2);
    y = astds(a,3);
    
    print "a = " a;
    print "y = " y;

The code above produces the following output (due to the use of random data in this example your answers will be different):

::

    a =
    
    Plane [1,.,.]
    
      12.538  -56.786
     -40.283  -58.287
    
    Plane [2,.,.]
    
       4.047   -0.325
      17.617   -9.248
    
    Plane [3,.,.]
    
      17.908   40.048
       8.916  -37.247
    
    Plane [4,.,.]
    
      -0.977   16.058
     -38.189    0.984
    
     y =
    
     Plane [1,.,.]
    
        7.321   35.659
       26.441   23.333

In this example, 16 standard Normal random variables are generated. They are multiplied by 25 and :func:`areshape`'d into a 4x2x2 array, and the standard deviation is computed across the third dimension of the array.

.. seealso:: Functions :func:`astd`, :func:`stdsc`

