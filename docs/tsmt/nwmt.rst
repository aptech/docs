====
nwmt
====

10.0.40nwmt
===========

Purpose
-------
Finds the Newey-West covariance matrix.

Library
-------
tsmt

Format
------
x = nwmt( covb, resid, nwtrunc );

Input
-----
+---------+-----------------------------------------------------------+
   | covb    | QxQ matrix, covariance matrix for the AR parameters.      |
   +---------+-----------------------------------------------------------+
   | resid   | TxL matrix of residuals.                                  |
   +---------+-----------------------------------------------------------+
   | nwtrunc | scalar, the number of autocorrelations to use in          |
   |         | calculating the Newey-West correction (*q* in the Remarks |
   |         | section below). If nwtrunc = 0, GAUSS will use a          |
   |         | truncation lag given by Newey and West, |image3|.         |
   +---------+-----------------------------------------------------------+

Output
------
= ============================================
   x QxQ matrix, Newey-West adjusted covariances.
   = ============================================

Remarks
-------
The Newey-West correction is used to account for the effect of
   heteroskedasticity and residual serial correlation on estimated
   parameter standard errors. The adjusted parameter covariance matrix
   is |image4| where.

   .. image:: _static/images/Equation706.svg
:class: _inline_math_MCEquation_0 mcReset

Source
------
varmamt.src

.. |image1| image:: _static/images/Equation704.svg
   :class: mcReset
.. |image2| image:: _static/images/Equation704.svg
   :class: mcReset
.. |image3| image:: _static/images/Equation704.svg
   :class: mcReset
.. |image4| image:: _static/images/Equation705.svg
   :class: _inline_math_MCEquation_0 mcReset
