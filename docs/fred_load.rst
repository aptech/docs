
fred_load
==============================================

Purpose
----------------
Get the observations or data values for one or more economic data series.

Format
----------------
.. function:: x = fred_load(formula[, ...])

    :param formula: Formula string made up of one or more series ids to fetch. Can be a single series id. See :func:`loadd` for reference on applying transformations. required

    :type formula: string

    :param options: Options to pass to the API. See below. These can be set directly when calling the function
        in the form of consecutive (key, value) pairs or via a dataframe constructed with :func:`fred_set`.
        All arguments can be specified in any order. For example:

        ::

            /* Retrieve the 'GNPCA' series with the following arguments:
            **   realtime_start = 2010-01-01
            **   realtime_end   = 2010-12-31
            **   frequency      = m
            */

            fred_load("GNPCA", "realtime_start", "2010-01-01", "realtime_end", "2010-12-31", "frequency", "m");

        This function supports the following options:

        .. list-table::
            :widths: auto

            * - realtime_start
              - YYYY-MM-DD formatted string. The start of the real-time period. For more information, see Remarks. optional, default: today's date

            * - realtime_end
              - YYYY-MM-DD formatted string. The end of the real-time period. For more information, see Remarks. optional, default: today's date

            * - limit
              - integer between 1 and 100000. The maximum number of results to return. optional, default: 100000

            * - offset
              - non-negative integer. Sort results is ascending or descending observation_date order. optional, default: 0

            * - sort_order
              - String. Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

            * - observation_start
              - YYYY-MM-DD formatted string. The start of the observation period. optional, default: 1776-07-04 (earliest available)

            * - observation_end
              - YYYY-MM-DD formatted string. The end of the observation period. optional, default: 9999-12-31 (latest available)

            * - units
              - string. A key that indicates a data value transformation. optional, default: lin (No transformation)

                One of the following values: 'lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log'
                
                - lin = Levels (No transformation)
                - chg = Change
                - ch1 = Change from Year Ago             
                - pch = Percent Change
                - pc1 = Percent Change from Year Ago             
                - pca = Compounded Annual Rate of Change
                - cch = Continuously Compounded Rate of Change
                - cca = Continuously Compounded Annual Rate of Change
                - log = Natural LogFor unit transformation formulas, see:
                
                Read more at https://alfred.stlouisfed.org/help#growth_formulas

            * - frequency
              - string. An optional parameter that indicates a lower frequency to aggregate values to.
                The FRED frequency aggregation feature converts higher frequency data series into lower frequency data series (e.g. converts a monthly data series into an annual data series). 
                In FRED, the highest frequency data is daily, and the lowest frequency data is annual.   
                There are 3 aggregation methods available- average, sum, and end of period.  
                See the *aggregation_method* parameter.
                
                - optional, default: no value for no frequency aggregation
                - One of the following values: 'd', 'w', 'bw', 'm', 'q', 'sa', 'a', 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem'

                  **Frequencies without period descriptions:**
                  
                  - d = Daily
                  - w = Weekly
                  - bw = Biweekly
                  - m = Monthly
                  - q = Quarterly
                  - sa = Semiannual
                  - a = Annual
                  
                  **Frequencies with period descriptions:**
                  
                  - wef = Weekly, Ending Friday
                  - weth = Weekly, Ending Thursday
                  - wew = Weekly, Ending Wednesday
                  - wetu = Weekly, Ending Tuesday
                  - wem = Weekly, Ending Monday
                  - wesu = Weekly, Ending Sunday
                  - wesa = Weekly, Ending Saturday
                  - bwew = Biweekly, Ending Wednesday
                  - bwem = Biweekly, Ending Monday
                
                - Note that an error will be returned if a frequency is specified that is higher than the native frequency of the series.
                  For instance if a series has the native frequency 'Monthly', it is not possible to aggregate the series to the higher 'Daily' 
                  frequency using the frequency parameter value 'd'. 
                
                - No frequency aggregation will occur if the frequency specified by the frequency parameter matches the native frequency of the series.  
                  For instance if the value of the frequency parameter is 'm' and the native frequency of the series is 'Monthly', observations will be
                  returned, but they will not be aggregated to a lower frequency. 
                
                - For most cases, it will be sufficient to specify a lower frequency without a period description (e.g. 'd', 'w', 'bw', 'm', 'q', 'sa', 'a') as opposed to frequencies with period descriptions 
                  (e.g. 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem') which only exist for the weekly and biweekly frequencies.  
                    
                  - The weekly and biweekly frequencies with periods exist to offer more options and override the default periods implied by values 'w' and 'bw'.
                  - The value 'w' defaults to frequency and period 'Weekly, Ending Friday' when aggregating daily series.
                  - The value 'bw' defaults to frequency and period 'Biweekly, Ending Wednesday' when aggregating daily and weekly series.
                  - Consider the difference between values 'w' for 'Weekly' and 'wef' for 'Weekly, Ending Friday'.    
                    When aggregating observations from daily to weekly, the value 'w' defaults to frequency and period 'Weekly, Ending Friday' which is the same as 'wef'.   
                    Here, the difference is that the period 'Ending Friday' is implicit for value 'w' but explicit for value 'wef'.
                    However, if a series has native frequency 'Weekly, Ending Monday', an error will be returned for value 'wef' but not value 'w'.
                
                - Read the 'Frequency Aggregation' section of the FRED FAQs for implementation details.

            * - aggregation_method
              - string. A key that indicates the aggregation method used for frequency aggregation. This parameter has no affect if the frequency parameter is not set. optional, default: avg

                One of the following values: 'avg', 'sum', 'eop'

                - avg = Average
                - sum = Sum
                - eop = End of Period

            * - output_type
              - integer. An integer that indicates an output type. optional, default: 1

                One of the following values: '1', '2', '3', '4'
                 
                - 1 = Observations by Real-Time Period 
                - 2 = Observations by Vintage Date, All Observations 
                - 3 = Observations by Vintage Date, New and Revised Observations Only 
                - 4 = Observations, Initial Release Only

            * - vintage_dates
              - string. A comma separated string of YYYY-MM-DD formatted dates in history (e.g. 2000-01-01,2005-02-24).

                - Vintage dates are used to download data as it existed on these specified dates in history.
                - Vintage dates can be specified instead of a real-time period using realtime_start and realtime_end. optional, no vintage dates are set by default.

    :type options: key, value pairs

    :return x: Results.
    :rtype x: Dataframe

Examples
----------------

Fetch a single series
+++++++++++++++++++++

::

    x = fred_load("DGDSRL1A225NBEA");

the first 5 rows of the dataframe are:

::

            date  DGDSRL1A225NBEA 
      1930-01-01       -7.9000000 
      1931-01-01       -3.6000000 
      1932-01-01       -11.700000 
      1933-01-01      -0.70000000 
      1934-01-01        9.1000000 

Fetch multiple series
+++++++++++++++++++++

::

    x = fred_load("DGDSRL1A225NBEA + DDURRL1A225NBEA + DNDGRL1A225NBEA");

the first 5 rows of the dataframe are:

::

            date  DDURRL1A225NBEA  DGDSRL1A225NBEA  DNDGRL1A225NBEA 
      1930-01-01       -17.200000       -7.9000000       -5.2000000 
      1931-01-01       -13.600000       -3.6000000       -1.1000000 
      1932-01-01       -24.000000       -11.700000       -8.8000000 
      1933-01-01       -2.6000000      -0.70000000      -0.40000000 
      1934-01-01        14.400000        9.1000000        8.2000000 


Fetch series with inline arguments
++++++++++++++++++++++++++++++++++

::

    x = fred_load("GNPCA", "realtime_start", "1980-01-01", "realtime_end", "1989-12-31")

the first 5 rows of the dataframe are:

::

            date            GNPCA 
      1929-01-01        314.70000 
      1929-01-01        315.70000 
      1929-01-01        709.60000 
      1930-01-01        285.20000 
      1930-01-01        285.60000 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_load`, :func:`fred_search`, :func:`fred_set`

