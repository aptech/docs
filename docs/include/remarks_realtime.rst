Real-Time Periods
+++++++++++++++++++

You can read extensively about the real-time period parameters directly on the FRED Website at https://fred.stlouisfed.org/docs/api/fred/realtime_period.html

Per the FRED website:

    The real-time period marks when facts were true or when information was known until it changed. Economic data sources, releases, series, and observations are all assigned a real-time period. Sources, releases, and series can change their names, and observation data values can be revised.

    On almost all URLs, the default real-time period is today. This can be thought of as FRED® mode- what information about the past is available today. ALFRED® users can change the real-time period to retrieve information that was known as of a past period of history.

    The real-time period can be specified by setting the realtime_start and realtime_end variables. Variables realtime_start and realtime_end are optional YYYY-MM-DD formatted dates that default to today's date. The real-time period set by realtime_start and realtime_end is a (closed, closed) period. This means that the real-time period includes the dates or boundaries set by realtime_start and realtime_end. 

