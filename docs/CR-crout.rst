
crout
==============================================

Purpose
----------------

Computes the Crout decomposition of a square matrix without row pivoting, such that: :math:`X = LU`.

Format
----------------
.. function:: crout(x)

    :param x: square nonsingular matrix
    :type x: Nxn matrix

    :returns: **y** (*NxN matrix*) - containing the lower (:math:`L`) and upper
        (:math:`U`) matrices of the Crout decomposition of *x*. The
        main diagonal of *y* is the main diagonal of the
        lower matrix *L*. The upper matrix has an implicit main
        diagonal of ones. Use :func:`lowmat` and :func:`upmat1` to extract the :math:`L` and :math:`U` matrices from *y*.

Remarks
-------

Since it does not do row pivoting, it is intended primarily for teaching
purposes. See :func:`croutp` for a decomposition with pivoting.

Examples
----------------

::

    X = { 1 2 -1,
          2 3 -2,
          1 -2 1 };

    // Perform crout decomposition
    y = crout(x);

    // Extract lower triangle of 'y' and assign it to 'L'
    L = lowmat(y);

    /*
    ** Extract upper triangle of 'y', fill the diagonal with
    ** ones and assign it to 'L'
    */
    U = upmat1(y);

After the code above:

::

        1.0  2.0 -1.0       1.0  0.0  0.0       1.0  2.0 -1.0
    y = 2.0 -1.0  0.0   L = 2.0 -1.0  0.0   U = 0.0  1.0  0.0
        1.0 -4.0  2.0       1.0 -4.0  2.0       0.0  0.0  1.0

.. seealso:: Functions :func:`croutp`, :func:`chol`, :func:`lowmat`, :func:`lowmat1`, :func:`lu`, :func:`upmat`, :func:`upmat1`
