
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

    :returns: y (*Nx(p*K) matrix*) containing powers of the elements of *x* from 1 to *p*. 
        The first *K* columns will contain first powers, the second *K* columns second powers, and so on.

Remarks
-------

To do polynomial regression use ols:

::

   { vnam,m,b,stb,vc,stderr,sigma,cx,rsq,resid,dwstat } = ols(0,y, polymat(x,p));


Source
------

polymat.src

