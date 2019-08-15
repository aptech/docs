
qtyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X and returns :math:`Q'Y` and :math:`R`.

.. DANGER:: fix all equations

Format
----------------
.. function:: { qty, r, e } = qtyre(y, x)

    :param y: data
    :type y: NxL matrix

    :param x: data
    :type x: NxP matrix

    :return qty: unitary matrix

    :rtype qty: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

    :return e: 

    :rtype e: Px1 permutation vector

Remarks
-------

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below
its diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X[.,E]`.

If :math:`X` has rank :math:`P`, then the columns of :math:`X` will not be permuted. If :math:`X` has
rank :math:`M < P`, then the :math:`M` linearly independent columns are permuted to the
front of :math:`X` by :math:`E`. Partition the permuted :math:`X` in the following way:

.. math::

   X[.⁢ , E] = [  X1⁢   X2⁢ ]

where :math:`X\ 1` is NxM and :math:`X\ 2` is Nx(P-M). Further partition :math:`R` in the following way:

.. math::

where :math:`R\ 11` is MxM and :math:`R\ 12` is Mx(P-M). Then

.. math::

and

.. math::


that is, :math:`A` is an Mx(P-N) matrix defining the linear combinations of :math:`X\ 2`
with respect to :math:`X\ 1`.

For most problems :math:`Q` or :math:`Q\ 1` is not it is required. Rather, we require
:math:`Q'Y` or :math:`Q\ 1'Y` where :math:`Y` is an NxL matrix. Since :math:`Q` can be a very large
matrix, :func:`qtyre` has been provided for the calculation of :math:`Q'Y` which will be
a much smaller matrix. :math:`Q\ 1'Y` will be a submatrix of :math:`Q'Y`. In particular,

.. math::

and :math:`Q\ 2'Y` is the remaining submatrix:

.. math::

Suppose that :math:`X` is an NxK data set of independent variables and :math:`Y` is an
Nx1 vector of dependent variables. Suppose further that :math:`X` contains
linearly dependent columns, i.e., :math:`X` has rank :math:`M < P`. Then define

.. math::

and the vector (or matrix of :math:`L > 1`) of least squares coefficients of the
reduced, linearly independent problem is the solution of

.. math::

To solve for *b* use :func:`qrsol`:

::

   b = qrsol(C, A);

If :math:`N < P`, the factorization assumes the form:

.. math::

where :math:`R\ 1` is a PxP upper triangular matrix and :math:`R\ 2` is Px(N-P). Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R\ 1` and :math:`R\ 2`. This
type of factorization is useful for the solution of underdetermined systems. For the solution of

.. math::

it can be shown that

::

   b = qrsol(Q'Y, R1)|zeros(N-P,1);

Source
------

qtyr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`qtyr`

