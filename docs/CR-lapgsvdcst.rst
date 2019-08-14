
lapgsvdcst
==============================================

Purpose
----------------

Compute the generalized singular value decomposition of a pair of real or complex general matrices.

Format
----------------
.. function:: { C, S, R, U, V, Q } = lapgsvdcst(A, B)

    :param A: data
    :type A: MxN matrix

    :param B: data
    :type B: PxN matrix

    :returns: C (*Lx1 vector*), singular values for *A*.

    :returns: S (*Lx1 vector*), singular values for *B*.

    :returns: R (*(K+L)x(K+L)*), upper triangular matrix.

    :returns: U (*MxM matrix*), orthogonal transformation matrix.

    :returns: V (*PxP matrix*), orthogonal transformation matrix.

    :returns: Q (*NxN matrix*), orthogonal transformation matrix.



Remarks
-------

(1) The generalized singular value decomposition of *A* and *B* is

.. math::

    U'*A*Q = D1*Z

.. math::

    V'\*B\*Q = D2\*Z

where *U*, *V*, and *Q* are orthogonal matrices (see :func:`lapgsvdcst` and
:func:`lapgsvdst`). Letting K + L = the rank of :math:`A\|B` then *R* is a :math:`(K+L)x(K+L)` upper
triangular matrix, *D1* and *D2* are Mx(K+L) and Px(K+L) matrices with entries on the diagonal, :math:`Z = [0 R]`, and if :math:`M-K-L \geq 0`

::

                     K L
   D1 =         K  [ I 0 ]
                L  [ 0 C ]
        M - K - L  [ 0 0 ]

::

                 K L
   D2 =     P  [ 0 S ]
        P - L  [ 0 0 ]

::

                 N-K-L   K    L
   [ 0 R ] = K [   0    R11  R12 ]
             L [   0     0   R22 ]

or if :math:`M-K-L \lt 0`

::

               K  M-K  K+L-M
   D1 =   K  [ I   0     0  ]
        M-K  [ 0   0     0  ]

::

                     N-K-L  K   M-K  K+L-M
                 K [   0   R11  R12   R13  ]
   [ 0 R ] =   M-K [   0    0   R22   R23  ]
             K+L-M [   0    0    0    R33  ]

(2) Form the matrix

::

   X = Q [ I 0  ]
         [ 0 R-1 ]

then

::

   A = U'^{-1}E_1X

   B = V'^{-1}E_2X^{-1}

where

::

   E1 = [ 0  D1 ]

   E2 = [ 0  D2 ]

(3) The generalized singular value decomposition of *A* and *B* implicitly
produces the singular value decomposition of :math:`AB^{-1}`:

.. DANGER:: verify equations on this page

.. math::

   AB^{-1} = UD_1D_2^{-1}V'

This procedure calls the LAPACK routines *DGGSVD* and *ZGGSVD*.

.. seealso:: Functions :func:`lapgsvds`, :func:`lapgsvdst`
