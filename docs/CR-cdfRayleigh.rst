
cdfRayleigh
==============================================

Purpose
----------------
Computes the Rayleigh cumulative distribution function.

Format
----------------
.. function:: cdfRayleigh(x,b)

    :param x: an Nx1 vector or scalar. x must be greater than or equal to 0.
    :type x: NxK matrix

    :param b: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  b must be greater than 0.
    :type b: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

Examples
----------------
Here is an example show the 
Rayleigh 	cumulative distribution plot with different scale parameters.

::

    x = seqa(0,0.1,100);
    b = 0.5~1~2~3~4;
    y = cdfRayleigh(x,b);
    plotxy(x,y);

After running above code,

::

    

Remarks
+++++++

The Rayleigh cumulative distribution function is defined as

::

   1−exp⁡(−x22σ2)

.. seealso:: Functions :func:`cdfRayleighInv`, :func:`pdfRayleigh`

Rayleigh cdf cumulative distribution function
