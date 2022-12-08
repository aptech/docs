======
tsFill
======

10.0.61tsFill
=============

Purpose
-------
Transforms stacked unbalanced time series data into a 'balanced' wide
   form matrix of panel data with missing values.

Library
-------
tsmt

Format
------
y_filled = tsFill( y, timecol, idcol );

Input
-----
======= =====================================================
y       Matrix, |image1|, stacked panel series data.
timecol Scalar, number of column containing time data.
idcol   Scalar, number of column containing group identifier.
======= =====================================================

Output
------
========= =================================================
y_stacked Matrix, |image2|, wide form matrix of panel data.
========= =================================================

Example
-------

::

   new;

   cls;

   library tsmt;


   // Load data
   data = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/ab_data.dat");

   // Fill data for unbalanced data
   stacked_data = tsFill( data, 3, 14 );

Source
------
tsFill.src

.. |image1| image:: _static/images/Equation708.svg
   :class: mcReset
.. |image2| image:: _static/images/Equation709.svg
   :class: mcReset
