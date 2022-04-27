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
     
   //Real GNP data 
   //Seasonally adjusted 
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/gnp_4790.fmt";
   gnp = loadd(fname);

   //Aggregate the gnp data from Q to A using end-of-quarter
   gnp_A_end = AggData(gnp[., 1], "Q", "Y", "E");

Library
-------
tsmt

Source
------
aggregatedata.src
