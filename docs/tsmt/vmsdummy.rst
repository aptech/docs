========
vmsdummy
========

10.0.76vmsdummy
===============

Purpose
-------

.. container::
   :name: Purpose

   Create matrix of indicators representing seasonal components.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   y_detrended = vmsdummy(y, freq, seas);

Input
-----

.. container::
   :name: Input

   +------+--------------------------------------------------------------+
   | y    | matrix, T×1, data representing seasonal.                     |
   +------+--------------------------------------------------------------+
   | freq | Scalar, frequency of the data per year. Valid options        |
   |      | include: [1] Yearly [4] Quarterly [12] Monthly.              |
   +------+--------------------------------------------------------------+
   | seas | Scalar, number of observations per season.                   |
   +------+--------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   =========== =======================
   y_detrended matrix, detrended data.
   =========== =======================

.. container::

   .. rubric:: Remarks
      :name: remarks
      :class: cr_section

   vmsdummy assumes that the start of the data corresponds with the
   start of a seasonal component.

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Generate random data
      y = rndn((25*12),1);

      //Monthly frequency
      freq = 12;

      //Seasonal dummy component every three months
      seas = 3;

      //Detrend data 
      {y_d, beta} = vmsdummy(y, freq, seas);

Source
------

.. container:: gfunc
   :name: Source

   vmsdummy.src
