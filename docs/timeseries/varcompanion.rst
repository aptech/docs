varCompanion
============

Purpose
-------
Extract the companion matrix and stability diagnostics from a fitted VAR or BVAR model.

Format
------

.. function:: { companion, eigenvalues, is_stable } = varCompanion(result)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :return companion: (mp)x(mp) companion matrix.
   :rtype companion: matrix

   :return eigenvalues: (mp)x2 matrix with columns [real, imaginary] for each eigenvalue.
   :rtype eigenvalues: matrix

   :return is_stable: 1 if all eigenvalues are inside the unit circle, 0 otherwise.
   :rtype is_stable: scalar

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4, quiet=1);

    // Extract companion matrix and eigenvalues
    { companion, eigenvalues, is_stable } = varCompanion(result);

    if is_stable;
        print "VAR is stable.";
    else;
        print "WARNING: VAR is not stable.";
    endif;

    // Eigenvalue moduli
    moduli = sqrt(eigenvalues[., 1]^2 + eigenvalues[., 2]^2);
    print "Eigenvalue moduli:";
    print moduli;

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`bvarFit`
