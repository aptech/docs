
lncdfnc
==============================================

Purpose
----------------

Computes natural log of complement of Normal cumulative distribution function.

Format
----------------
.. function:: y = lncdfnc(x)

    :param x: values at which to evaluate the complement of the cumulative distribution function.
    :type x: NxK matrix

    :return y: the natural log of the complement of the cumulative distribution function.

        .. math:: ln\ (1 - Pr(X < x))

    :rtype y: NxK matrix

Examples
----------------

::

    // Value to compute
    x = 0.5;

    // Compute complement of the cdf
    pc = cdfnc(x);

    // Compute ln of the complement of the cdf
    lnpc = lncdfnc(x)

    print "pc ="; pc;
    print "ln(pc)"; lnpc;

::

  pc =
  0.30854
  ln(pc) =
  -1.17591

Source
------

lncdfn.src
