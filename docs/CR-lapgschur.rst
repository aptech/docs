
lapgschur
==============================================

Purpose
----------------

Compute the generalized Schur form of a pair of real or complex general matrices.

Format
----------------
.. function:: { sa, sb, q, z } = lapgschur(A, B[, sort_type])

    :param A: real or complex general matrix.
    :type A: NxN matrix

    :param B: real or complex general matrix.
    :type B: NxN matrix

    :param sort_type: Optional input. How to sort the eigenvalues. Options include:

        .. list-table::
            :widths: auto

            * - 1
              - "udi"
              - Absolute value of the eigenvalue less than 1.0. (Unit disk inside).
            * - 2
              - "udo"
              - Absolute value of the eigenvalue greater than or equal to 1.0. (Unit disk outside).
            * - 3
              - "lhp"
              - Value of the real portion of th eigenvalue less than 0. (Left hand plane).
            * - 4
              - "rhp"
              - Value of the real portion of th eigenvalue greater than 0. (Right hand plane).
            * - 5
              - "ref"
              - Real eigenvalues first. (Complex portion less than :func:`imagtol`).
            * - 6
              - "cef"
              - Complex eigenvalues first. (Complex portion greater than :func:`imagtol`).

    :type sort_type: scalar or string

    :return sa: Schur form of *A*, sometimes called *S*.

    :rtype sa: NxN matrix

    :return sb: Schur form of *B*, sometimes called *T*.

    :rtype sb: NxN matrix

    :return q: left Schur vectors.

    :rtype q: NxN matrix

    :return z: right Schur vectors.

    :rtype z: NxN matrix

Examples
----------------

Basic usage
+++++++++++

::

    // For repeatable random numbers
    rndseed 23434;

    // Matrix dimensions
    order = 4;

    // Create 2 square, complex matricies
    A = complex(rndn(order, order), rndn(order, order));
    B = complex(rndn(order, order), rndn(order, order));

    // Perform 'QZ' decomposition
    { sa, sb, q, z } =  lapgschur(A, B);

    // Calculate generalized eigenvalues
    eig_vals = diag(sa) ./ diag(sb);

    print "Generalized eigenvalues = ";
    print eig_vals;

    print "Absolute value of the generalized eigenvalues = ";
    print abs(eig_vals);

The above code should return the following output:

::

    Generalized eigenvalues =

    -0.76631163 -        1.3445924i
     0.65409426 -       0.18908938i
    -0.012440975 +       0.47626474i
    -0.75927986 +        1.6212326i

    Absolute value of the generalized eigenvalues =

    1.5476312
    0.68087745
    0.47642721
    1.7902237

Ordering eigenvalues
++++++++++++++++++++

You can order the eigenvalues by passing in the optional third input, *sort_type*. The code below uses the same *A* and *B* variables made in the example above.

::

    // Perform 'QZ' decomposition and
    // reorder generalized eigenvalues, placing
    // those with absolute value less than 1
    // on the upper left
    { sa, sb, q, z } =  lapgschur(A, B, "udi");

    // Calculate generalized eigenvalues
    eig_vals = diag(sa) ./ diag(sb);

    print "Generalized eigenvalues = ";
    print (eig_vals);

    print "Absolute value of the generalized eigenvalues = ";
    print abs(eig_vals);

The code above should print out the sorted eigenvalues as we see below.

::

    Generalized eigenvalues =

     0.65409426 -       0.18908938i
    -0.012440975 +      0.47626474i
    -0.76631163 -        1.3445924i
    -0.75927986 +        1.6212326i

    Absolute value of the generalized eigenvalues =

    0.68087745
    0.47642721
    1.5476312
    1.7902237

Remarks
-------

-  The pair of matrices *sa* (sometimes called *S*) and *sb* (sometimes called *T*) are in generalized real Schur form if:

   -  *sb* is upper triangular with non-negative diagonal.
   -  *sa* is block upper triangular with 1x1 and 2x2 blocks. The 1x1
      blocks correspond to real generalized eigenvalues and the 2x2
      blocks to pairs of complex conjugate eigenvalues.

-  The real generalized eigenvalues can be computed by dividing the
   diagonal element of *sa* by the corresponding diagonal element of *sb*.
-  The complex generalized eigenvalues are computed by first
   constructing two complex conjugate numbers from 2x2 block where the
   real parts are on the diagonal of the block and the imaginary part on
   the off-diagonal. The eigenvalues are then computed by dividing the
   two complex conjugate values by their corresponding diagonal elements
   of *sb*.
-  The generalized Schur vectors *q* and *z* are orthogonal matrices (:math:`q'q = I` and :math:`z'z = I`) that reduce *A* and *B* to Schur form:

   ::

       sa = q'A*z
       sb = q'B*z

       A = q*sa*z'
       B = q*sb*z'

-  If only the generalized eigenvalues are needed, you can call :func:`lapgeig`, or :func:`lapgeigv`.
