=========
stackData
=========

10.0.52stackData
================

Purpose
-------

.. container::
   :name: Purpose

   Stacks columns of panel series into a single stacked vector of data.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   y_st = stackData( yt );

Input
-----

.. container::
   :name: Input

   == ===================================
   yt TxK matrix of cross sectional data.
   == ===================================

Output
------

.. container::
   :name: Output

   ==== ==================================================================
   y_st (T*K)x1 Matrix of stacked cross sectional data, i.e.
        ::
        
           y_st = yt[ . , 1] | yt[ . , 2] | yt[ . , 3] | ... | yt[ . , K].
   ==== ==================================================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Loading data
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/dynam.fmt";
      dat = loadd(fname);

      y_stacked = stackData(dat);

      print "Rows in y_stacked :";; rows( y_stacked );
      print;
      print "Columns in y_stacked :";; cols( y_stacked );
      print;

Source
------

.. container:: gfunc
   :name: Source

   stackdata.src
