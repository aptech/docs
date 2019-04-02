
erfcplx, erfccplx
==============================================

Purpose
----------------

Computes the Gaussian error function (:func:`erfcplx`) and its complement (:func:`erfccplx`) for complex inputs.

Format
----------------
.. function:: erfcplx(z) 
              erfccplx(z)

    :param z: z must be > 0
    :type z: NxK complex matrix

    :returns: f (*NxK complex matrix*)

Technical Notes
---------------

Accuracy is better than 12 significant digits.

References
----------

#. Abramowitz & Stegun, section 7.1, equations 7.1.9, 7.1.23, and 7.1.29

#. Main author Paul Godfrey

#. Small changes by Peter J. Acklam

