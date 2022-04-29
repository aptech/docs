vmsdetrend
==========

Purpose
-------
Seasonally detrends data.

Format
------
.. function:: y_detrended = vmsdetrend(y, freq, seas)

   :param y: Tx1, data to be detrended.
   :type y: matrix

   :param freq: frequency of the data per year. Valid options include: [1] Yearly [4] Quarterly [12] Monthly.
   :type freq: Scalar

   :param seas: number of observations per season.
   :type seas: Scalar

   :return y_detrended: detrended data.
   :rtype y_detrended: matrix


Example
-------
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
   {y_d, beta} = vmsdetrend(y, freq, seas);

Library
-------
tsmt

Source
------
vmsdetrend.src
