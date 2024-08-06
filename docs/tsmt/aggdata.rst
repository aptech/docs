aggData
=======

Purpose
-------
Aggregates time series data from higher to lower frequency.

Format
------
.. function:: x_new = aggData(xt, st_freq, end_freq, method)

   :param xt: data.
   :type xt: NxK matrix

   :param st_freq: starting frequency of data: "M" for monthly or "Q" for quarterly.
   :type st_freq: string

   :param end_freq: ending frequency of data: "M" for monthly or "Q" for quarterly.
   :type end_freq: string

   :param method: method of aggregation, "B" for beginning of period, "E" for end of period, "AVE" for moving average.
   :type method: string

   :return x_new: aggregated data.
   :rtype x_new: matrix

Example
-------

::

   new;
   cls;
   library tsmt;

   // Real GNP data
   // Seasonally adjusted
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/gnp_4790.csv";
   gnp = loadd(fname, "real_gnp");

   // Aggregate the gnp data from Q to A using end-of-quarter
   gnp_A_end = AggData(gnp, "Q", "Y", "E");

The first five values of `gnp` and `gnp_A_end` are:

::

  gnp[1:5]
  1056.50
  1063.20
  1067.10
  1080.00
  1086.80

  gnp_A_end[1:5]
  1080.00
  1125.50
  1103.30
  1260.20
  1356.00
  
Library
-------
tsmt

Source
------
aggregatedata.src
