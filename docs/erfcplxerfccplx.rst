
erfcplx, erfccplx
==============================================

Purpose
----------------

Computes the Gaussian error function (:func:`erfcplx`) and its complement (:func:`erfccplx`) for complex inputs.

Format
----------------
.. function:: f_cplx = erfcplx(z)
              f_cplx = erfccplx(z)

    :param z: The complex inputs used to compute the Gaussian error function or its complement. :math:`z > 0`
    :type z: NxK complex matrix

    :return f_cplx: the Gaussian error function (:func:`erfcplx`) or the complement of the Gaussian error function (:func:`erfccplx`).

    :rtype f_cplx: NxK complex matrix

Examples
----------------

The Gaussian error function of a complex matrix
++++++++++++++++++++++++++++++++++++++++++++++++
::

    // Real component of x
    x_real = 1;

    // Imaginary component of x
    x_imag = -2;

    // Form complex x matrix
    x_cplx = complex(x_real, x_imag);

    // Find Gaussian error function
    f_cplx = erfcplx(x_cplx);

After this:

::

    f_cplx = -0.537 +    5.049i

The complement of the Gaussian error function of a complex matrix
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    f_ccplx = erfccplx(x_cplx);

Now

::

    f_ccplx = 1.537 -    5.049i

Which is equal to:

::

    1 - f_cplx;
    

Remarks
---------------

Accuracy is better than 12 significant digits.

References
----------

#. Abramowitz & Stegun, section 7.1, equations 7.1.9, 7.1.23, and 7.1.29

#. Main author Paul Godfrey

#. Small changes by Peter J. Acklam
