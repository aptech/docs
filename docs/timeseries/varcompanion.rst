varCompanion
============

Purpose
-------
Extract the companion matrix and stability diagnostics from a fitted VAR model.

Format
------

.. function:: { companion, eigenvalues, is_stable } = varCompanion(result)

   :param result: an instance of a :class:`varResult` structure.
   :type result: struct

   :return companion: (mp)x(mp) companion matrix.
   :rtype companion: matrix

   :return eigenvalues: (mp)x1 vector of eigenvalues, complex when any imaginary part exceeds 1e-12 times the largest modulus; otherwise a real vector.
   :rtype eigenvalues: complex or real vector

   :return is_stable: 1 if all eigenvalues are inside the unit circle, 0 otherwise.
   :rtype is_stable: scalar

Examples
--------

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"));
    result = varFit(data, 4, quiet=1);

    // Extract companion matrix and eigenvalues
    { companion, eigenvalues, is_stable } = varCompanion(result);

    if is_stable;
        print "VAR is stable.";
    else;
        print "WARNING: VAR is not stable.";
    endif;

    // Eigenvalue moduli
    moduli = abs(eigenvalues);
    print "Eigenvalue moduli:";
    print moduli;

    // sprintf needs real-valued arguments
    for root_idx (1, rows(eigenvalues), 1);
        print sprintf("%.6f %+.6fi", real(eigenvalues[root_idx]),
                      imag(eigenvalues[root_idx]));
    endfor;

Remarks
-------

Use ``abs(eigenvalues)`` for the moduli, and ``real()`` and ``imag()``
for formatted printing. *is_stable* is the fit's stored
*result.is_stationary* value.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`
