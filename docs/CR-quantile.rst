
quantile
==============================================

Purpose
----------------

Computes quantiles from data in a matrix, given specified probabilities.

Format
----------------
.. function:: quantile(x,  e) 
			  quantile(x,  e,  tp)

    :param x: NxK matrix of data.
    :type x: TODO

    :param e: quantile levels or probabilities.
    :type e: Lx1 vector

    :param tp: 1, 2, ..., 9. Sample quantile type.
        Default is 4.
    :type tp: Scalar

    :returns: y (*LxK matrix*), quantiles.

Examples
----------------

::

    //Set the rng seed for repeatable random numbers
                    
    rndseed 345567;
    
    //Create a 1000x4 random normal matrix
    x = rndn(1000,4);
    
    //Quantile levels
    e = { .025, .5, .975 };
    			
    y = quantile(x, e);
     
    print "medians";
    print y[2,.];
    print;
    print "95 percentiles";
    print y[1,.];
    print y[3,.];

Produces the following output:

::

    medians
        -0.037801917   0.029923972  -0.010477829  -0.023937160
    
    95 percentiles
          -2.0074122    -2.0798579    -1.9982702    -1.9605009
           2.0437573     2.0271770     1.9025695     1.9228044

Source
++++++

quantile.src

quantile probability data matrix
