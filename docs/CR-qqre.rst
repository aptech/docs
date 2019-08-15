
qqre
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:` X[.,E] = Q1R`

.. DANGER:: Fix all equations. all equations below are blank as they were corrupted during merge.

Format
----------------
.. function:: { q1, r, e } = qqre(x)

    :param x: data
    :type x: NxP matrix

    :return q1: :math:`K = min(N,P)`.

    :rtype q1: NxK unitary matrix

    :return r: 

    :rtype r: KxP upper triangular matrix

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

If you want only the :math:`R` matrix, see :func:`qre`. Not computing :math:`Q\ 1` can produce
significant improvements in computing time and memory usage.

If :math:`X` has rank :math:`P`, then the columns of :math:`X` will not be permuted. If :math:`X` has
rank :math:`M < P`, then the :math:`M` linearly independent columns are permuted to the
front of :math:`X` by :math:`E`. Partition the permuted :math:`X` in the following way:

.. math::

where :math:`X` is NxM and :math:`X\ 2` is Nx(P-M). Further partition :math:`R` in the following
way:

.. math::

where :math:`R\ 11` is MxM and :math:`R\ 12` is Mx(P-M). Then

.. math::

and

.. math::

that is, :math:`A` is an Mx(P-N) matrix defining the linear combinations of :math:`X\ 2` with respect to :math:`X\ 1`.

If :math:`N < P`, the factorization assumes the form:

.. math::

where :math:`R\ 1` is a PxP upper triangular matrix and :math:`R\ 2` is Px(N-P). Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R\ 1` and :math:`R\ 2`. This
type of factorization is useful for the solution of underdetermined systems. For the solution of

.. math::

it can be shown that

::

    b = qrsol(Q'Y, R1)|zeros(N-P,1);

The explicit formation here of :math:`Q`, which can be a very large matrix, can
be avoided by using the function :func:`qtyre`.

For further discussion of QR factorizations see the remarks under :func:`qqr`.

Source
------

qqr.src

.. seealso:: Functions :func:`qtyre`, :func:`olsqr`

