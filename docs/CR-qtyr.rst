
qtyr
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix :math:`X` and returns :math:`Q'Y` and :math:`R`.

.. DANGER:: fix all equations

Format
----------------
.. function:: { qty, r } = qtyr(y, X)

    :param y: data
    :type y: NxL matrix

    :param X: data
    :type X: NxP matrix

    :return qty: unitary matrix

    :rtype qty: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

Remarks
-------

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X` is zero below its
diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of
:math:`X'X`. For most problems :math:`Q` or :math:`Q\ 1` is not what is required. Rather, we
require :math:`Q'Y` or :math:`Q\ 1'Y` where :math:`Y` is an NxL matrix (if either :math:`QY` or :math:`Q\ 1\ Y`
are required, see :func:`qyr`). Since :math:`Q` can be a very large matrix, :func:`qtyr` has
been provided for the calculation of :math:`Q'Y` which will be a much smaller
matrix. :math:`Q\ 1'Y` will be a submatrix of :math:`Q'Y`. In particular,

.. math::

and :math:`Q\ 2'Y` is the remaining submatrix:

.. math::

Suppose that :math:`X` is an NxK dataset of independent variables, and :math:`Y` is an
Nx1 vector of dependent variables. Then it can be shown that

.. math::

and

.. math::

   sj= N−PΣi=1⁢Hi,j,⁢j = 1,2,...L

where *b* is a PxL matrix of least squares coefficients and *s* is a 1xL
vector of residual sums of squares. Rather than invert :math:`R` directly,
however, it is better to apply :func:`qrsol` to

.. math::

   Rb⁢= Q1′Y

For rank deficient least squares problems, see :func:`qtyre` and :func:`qtyrep`.

Examples
----------------
The QR algorithm is the numerically superior method for the solution of least squares problems:

::

    loadm x, y;
    { qty, r } = qtyr(y,x);
    q1ty = qty[1:rows(r),.];
    q2ty = qty[rows(r)+1:rows(qty),.];
    
    // LS coefficients 
    b = qrsol(q1ty,r);
    
    // Residual sums of squares 
    s2 = sumc(q2ty^2);

Source
------

qtyr.src

.. seealso:: Functions :func:`qqr`, :func:`qtyre`, :func:`qtyrep`, :func:`olsqr`

