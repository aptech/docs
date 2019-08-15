
pdfHyperGeo
==============================================

Purpose
----------------

Computes the probability mass function for the hypergeometric distribution.

Format
----------------
.. function:: p = pdfHyperGeo(x, m, k, n)

    :param x: must be a positive number and < *m*
    :type x: NxK matrix, Nx1 vector or scalar

    :param m: The size of the population from which draws will be made. ExE conformable with *x*. *m* must be > *x*, *k* and *n*.
    :type m: NxK matrix, Nx1 vector or scalar

    :param k: The number of marked items. ExE conformable with *x*.
    :type k: NxK matrix, Nx1 vector or scalar

    :param n: The number of items drawn from the population. ExE conformable with *x*. :math:`0 < k < m`.
    :type n: NxK matrix, Nx1 vector or scalar

    :return p: The probability of drawing *x* marked items.

    :rtype p: NxK matrix, Nx1 vector or scalar

Examples
----------------
You are given 50 hard drives, 4 of which are known to be bad. What is the probability of 
drawing exactly 1 bad hard drive if you randomly select 6 drives?

::

    p = pdfHyperGeo(1, 50, 4, 6);

After running the code above, *p* is equal to:

::

    0.34504559

Continuing with the example above, what are the probabilities of drawing exactly 2 or exactly 4 bad hard drives?

::

    x = { 2, 4 };
    p = pdfHyperGeo(x, 50, 4, 6);

After running the code above, *p* is equal to:

::

    0.061615284 
    6.5132436e-05

Remarks
-------

.. DANGER:: fix equations

The probability density function for the hypergeometric distribution is defined as:

:math:`P\left( x \middle| m,k,n \right)\text{ = }`
:math:`\frac{\left( \left. \begin{matrix}
k \\
x \\
\end{matrix} \right)\left( \left. \begin{matrix}
{m - k} \\
{n - x} \\
\end{matrix} \right) \right. \right.}{\begin{pmatrix}
m \\
n \\
\end{pmatrix}}`

For invalid inputs, :func:`pdfHyperGeo` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

.. seealso:: Functions :func:`cdfHyperGeo`, :func:`rndHyperGeo`, :func:`pdfBinomial`

