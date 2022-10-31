
fred_series_observations
==============================================

Purpose
----------------
Get the observations or data values for an economic data series.

Format
----------------
.. function:: x = fred_series_observations(series_id[, ...])

    :param series_id: The id for a series. required

    :type series_id: string

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 100000

    :type limit: integer between 1 and 100000

    :param offset: Sort results is ascending or descending observation_date order. optional, default: 0

    :type offset: non-negative integer

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :param observation_start: The start of the observation period. optional, default: 1776-07-04 (earliest available)

    :type observation_start: YYYY-MM-DD formatted string

    :param observation_end: The end of the observation period. optional, default: 9999-12-31 (latest available)

    :type observation_end: YYYY-MM-DD formatted string

    :param units: A key that indicates a data value transformation. optional, default: lin (No transformation)

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
        
        https://alfred.stlouisfed.org/help#growth_formulas

    :type units: string

    :param frequency: An optional parameter that indicates a lower frequency to aggregate values to.
        The FRED frequency aggregation feature converts higher frequency data series into lower frequency data series (e.g. converts a monthly data series into an annual data series). 
        In FRED, the highest frequency data is daily, and the lowest frequency data is annual.   
        There are 3 aggregation methods available- average, sum, and end of period.  
        See the aggregation_method parameter.
        
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
          For instance if a series has the native frequency 'Monthly' (as returned by the :func:`fred_series` request), 
          it is not possible to aggregate the series to the higher 'Daily' frequency using the frequency parameter value 'd'. 
        
        - No frequency aggregation will occur if the frequency specified by the frequency parameter matches the native frequency of the series.  
          For instance if the value of the frequency parameter is 'm' and the native frequency of the series is 'Monthly' (as returned by the :func:`fred_series` request), 
          observations will be returned, but they will not be aggregated to a lower frequency. 
        
        - For most cases, it will be sufficient to specify a lower frequency without a period description (e.g. 'd', 'w', 'bw', 'm', 'q', 'sa', 'a') as opposed to frequencies with period descriptions 
          (e.g. 'wef', 'weth', 'wew', 'wetu', 'wem', 'wesu', 'wesa', 'bwew', 'bwem') which only exist for the weekly and biweekly frequencies.  
            
            - The weekly and biweekly frequencies with periods exist to offer more options and override the default periods implied by values 'w' and 'bw'.
            - The value 'w' defaults to frequency and period 'Weekly, Ending Friday' when aggregating daily series.
            - The value 'bw' defaults to frequency and period 'Biweekly, Ending Wednesday' when aggregating daily and weekly series.
            - Consider the difference between values 'w' for 'Weekly' and 'wef' for 'Weekly, Ending Friday'.    
              When aggregating observations from daily to weekly, the value 'w' defaults to frequency and period 'Weekly, Ending Friday' which is the same as 'wef'.   
              Here, the difference is that the period 'Ending Friday' is implicit for value 'w' but explicit for value 'wef'.
              However, if a series has native frequency 'Weekly, Ending Monday', an error will be returned for value 'wef' but not value 'w'.
        
        - Note that frequency aggregation is currently only available for file_type equal to xml or json due to time constraints.
        - Read the 'Frequency Aggregation' section of the FRED FAQs for implementation details.

    :type frequency: string

    :param aggregation_method: A key that indicates the aggregation method used for frequency aggregation. This parameter has no affect if the frequency parameter is not set. optional, default: avg

        One of the following values: 'avg', 'sum', 'eop'

        - avg = Average
        - sum = Sum
        - eop = End of Period

    :type aggregation_method: string

    :param output_type: An integer that indicates an output type. optional, default: 1

         One of the following values: '1', '2', '3', '4'
         
        - 1 = Observations by Real-Time Period 
        - 2 = Observations by Vintage Date, All Observations 
        - 3 = Observations by Vintage Date, New and Revised Observations Only 
        - 4 = Observations, Initial Release Only

    :type output_type: integer

    :param vintage_dates: A comma separated string of YYYY-MM-DD formatted dates in history (e.g. 2000-01-01,2005-02-24).

        - Vintage dates are used to download data as it existed on these specified dates in history.
        - Vintage dates can be specified instead of a real-time period using realtime_start and realtime_end. optional, no vintage dates are set by default.

    :type vintage_dates: string

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order', 'observation_start', 'observation_end', 'units', 'frequency', 'aggregation_method', 'output_type', 'vintage_dates']

Examples
----------------

::

    head(fred_series_observations("GNPCA"));

    
            date     realtime_end   realtime_start            value 
      1929-01-01       2022-10-31       2022-10-31         1120.718 
      1930-01-01       2022-10-31       2022-10-31         1025.678 
      1931-01-01       2022-10-31       2022-10-31          958.927 
      1932-01-01       2022-10-31       2022-10-31          834.769 
      1933-01-01       2022-10-31       2022-10-31          823.628 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_release`, :func:`fred_series_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

