====
nwmt
====

10.0.40nwmt
===========

Purpose
-------

.. container::
   :name: Purpose

   Finds the Newey-West covariance matrix.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   x = nwmt( covb, resid, nwtrunc );

Input
-----

.. container::
   :name: Input

   +---------+-----------------------------------------------------------+
   | covb    | Q×Q matrix, covariance matrix for the AR parameters.      |
   +---------+-----------------------------------------------------------+
   | resid   | T×L matrix of residuals.                                  |
   +---------+-----------------------------------------------------------+
   | nwtrunc | scalar, the number of autocorrelations to use in          |
   |         | calculating the Newey-West correction (*q* in the Remarks |
   |         | section below). If nwtrunc = 0, GAUSS will use a          |
   |         | truncation lag given by Newey and West, |image3|.         |
   +---------+-----------------------------------------------------------+

Output
------

.. container::
   :name: Output

   = ============================================
   x Q×Q matrix, Newey-West adjusted covariances.
   = ============================================

Remarks
-------

.. container::
   :name: Remarks

   The Newey-West correction is used to account for the effect of
   heteroskedasticity and residual serial correlation on estimated
   parameter standard errors. The adjusted parameter covariance matrix
   is |image4| where.

   .. image:: GeneratedImages/Equations/Equation706.svg
      :class: _inline_math_MCEquation_0 mcReset

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src

.. |image1| image:: GeneratedImages/Equations/Equation704.svg
   :class: mcReset
.. |image2| image:: GeneratedImages/Equations/Equation704.svg
   :class: mcReset
.. |image3| image:: GeneratedImages/Equations/Equation704.svg
   :class: mcReset
.. |image4| image:: GeneratedImages/Equations/Equation705.svg
   :class: _inline_math_MCEquation_0 mcReset
