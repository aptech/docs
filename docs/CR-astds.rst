
astds
==============================================

Purpose
----------------
Computes the biased standard deviation of the elements across one dimension of an N-dimensional array.

Format
----------------
.. function:: astds(x,  dim)

    :param x: N-dimensional array.
    :type x: TODO

    :param dim: number of dimension to sum across.
    :type dim: scalar

    :returns: y (*TODO*), N-dimensional array, standard deviation across specified dimension of x.

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

In this example, 16 standard Normal random variables are generated. They
are multiplied by 25 and areshape'd into a
4x2x2 array, and the standard deviation is computed
across the third dimension of the array.

.. seealso:: Functions :func:`astd`, :func:`stdsc`

sample standard deviation dimension array
