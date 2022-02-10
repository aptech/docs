
rndseed
==============================================

Purpose
----------------

Sets a new seed value, initializing the random number generators.

.. _rndseed:

.. index:: rndseed

Format
----------------

::

    rndseed seed;

**Parameters**

    :seed: (*scalar*) initial seed for the random number generator.
    


Examples
------------


::

    // Set the random number seed
    rndseed 2345;

    // Draw 4 random normal numbers
    x = rndn(4,1);
    print x;

::

      -1.8735651 
     -0.13259605 
      0.36674467 
      0.25466902 

Resetting the seed will give us the same random numbers. However, these numbers will be assigned to the resulting matrix in row major order as we see below.

::

    // Reset the seed to the previous starting value
    rndseed 2345;

    // Draw 8 random numbers assigned to 2 columns
    x = rndn(4,2);
    print x;

      -1.8735651      -0.13259605 
      0.36674467       0.25466902 
     -0.74397704      0.018069520 
       2.0880837       -1.8181213 


The seed value passed to :func:`rndseed` does not have to be a literal value. It can be set from a GAUSS variable as shown below.

::

    seed = 2345;
    rndseed seed;
    print rndn(4,1)

::

      -1.8735651 
     -0.13259605 
      0.36674467 
      0.25466902 


Remarks
-------

The main purpose of setting the seed is so that you can reproduce an identical series of random numbers.

When GAUSS is started the random number generator is seeded with the current time. 


.. seealso:: Functions :func:`rndu`, :func:`rndn`, :func:`rndi`
