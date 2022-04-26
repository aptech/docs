=======
arimamt
=======

10.0.2aggData
=============

Purpose
-------

.. container::
   :name: Purpose

   Aggregates time series data from higher to lower frequency.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   x_new = aggData(xt, st_freq, end_freq, method);

Input
-----

.. container::
   :name: Input

   +----------+----------------------------------------------------------+
   | xt       | NxK matrix, data.                                        |
   +----------+----------------------------------------------------------+
   | st_freq  | String, starting frequency of data: "M" for monthly or   |
   |          | "Q" for quarterly.                                       |
   +----------+----------------------------------------------------------+
   | end_freq | String, ending frequency of data: "M" for monthly or "Q" |
   |          | for quarterly.                                           |
   +----------+----------------------------------------------------------+
   | method   | String, method of aggregation, "B" for beginning of      |
   |          | period, "E" for end of period, "AVE" for moving average. |
   +----------+----------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ===== ========================
   x_new Matrix, aggregated data.
   ===== ========================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;
        
      //Real GNP data 
      //Seasonally adjusted 
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/gnp_4790.fmt";
      gnp = loadd(fname);

      //Aggregate the gnp data from Q to A using end-of-quarter
      gnp_A_end = AggData(gnp[., 1], "Q", "Y", "E");

Source
------

.. container:: gfunc
   :name: Source

   aggregatedata.src
