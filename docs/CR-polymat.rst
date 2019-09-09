
polymat
==============================================

Purpose
----------------

Returns a matrix containing the powers of the elements of x from 1 to p.

Format
----------------
.. function:: y = polymat(x, p)

    :param x: data
    :type x: NxK matrix

    :param p: positive integer.
    :type p: scalar

    :return y: contains powers of the elements of *x* from 1 to *p*. 
        The first *K* columns will contain first powers, the second *K* columns second powers, and so on.

    :rtype y: Nx(p*K) matrix

Remarks
-------

To do polynomial regression use ols:

::

   { vnam,m,b,stb,vc,stderr,sigma,cx,rsq,resid,dwstat } = ols(0,y, polymat(x,p));


Source
------

polymat.src
