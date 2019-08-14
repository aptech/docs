
quantile
==============================================

Purpose
----------------

Computes quantiles from data in a matrix, given specified probabilities.

.. DANGFER:: verify equations

Format
----------------
.. function:: y = quantile(x, e[, tp])

    :param x: data
    :type x: NxK matrix

    :param e: quantile levels or probabilities.
    :type e: Lx1 vector

    :param tp: 1, 2, ..., 9. Sample quantile type. Default is 4.
    :type tp: scalar

    :return y: quantiles.

    :type y: LxK matrix

Remarks
-------

Let { :math:`x_{(1)},...,x_{(n)}\,` } denote the order statistics, and let
:math:`{\overset{\hat{}}{Q}}_{i}\left( p \right)\, = \,\left( 1 - \gamma \right)x_{(j)} + \gamma x_{(j + 1)}`
denotes the sample quantiles, where
:math:`\frac{j - m}{n} \leq p < \frac{j - m - 1}{n},\, m \in {\mathbb{R}},\, 0 \leq \gamma \leq 1.`
The value of :math:`\gamma` is a function of integer part 
:math:`j = \, floor\left( pn + m \right)` and fractional part 
:math:`g = \, pn + m - j`. The :math:`m` is a constant determined by sample quantile type.

======== ================================
Type     Definition
======== ================================
1        Discrete sample quantile type 1. Inverse of empirical distribution function.
2        Discrete sample quantile type 2. Similar to type 1 except that averaging at discontinuities.
3        Discrete sample quantile type 3. SAS definition, choose the nearest even order statistics.
4        Continuous sample quantile type 4. Interpolating the step function of definition 1. 
5        Continuous sample quantile type 5. This is the value midway through each step of definition 1.
6        Continuous sample quantile type 6. The vertices divide the sample space into n+1 regions, each with probability 1/(n+1).
7        Continuous sample quantile type 7.  The vertices divide the range into n-1 regions, and 100p% of the intervals lie to the left and 100(1-p)% lie to the right.
8        Continuous sample quantile type 8. The resulting sample quantile is median unbiased regardless the distribution.
9        Continuous sample quantile type 9. The resulting sample quantile is median unbiased if normal distribution.
======== ================================

Examples
----------------

::

    // Set the rng seed for repeatable random numbers
                    
    rndseed 345567;
    
    // Create a 1000x4 random normal matrix
    x = rndn(1000,4);
    
    // Quantile levels
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
------

quantile.src

