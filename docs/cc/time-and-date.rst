Time and Date
=======================

.. note:: Date variables in a GAUSS dataframe store dates in Posix format, so all "posix" functions work with GAUSS date variables.

Conversion and formatting
--------------------------------

============================     ======================================================================
:doc:`../asdate`                  Converts columns of matrices, string arrays or dataframes to dates, with the option to specify the display format.
:doc:`../dttoposix`               Converts DT scalar format to POSIX date/time format.
:doc:`../dttostr`                 Converts a matrix containing dates in DT scalar format to a string array.
:doc:`../dttostrc`                Converts a date in DT Scalar format into a string array.
:doc:`../etstr`                   Converts elapsed time in hundredths of a second to a string, with days, minutes, hours and seconds.
:doc:`../posixtostrc`             Converts a date in Posix time (seconds since the Epoch) into a string array.
:doc:`../strtodt`                 Converts a string array of dates to a matrix in DT scalar format.
:doc:`../strctodt`                Converts string dates to a matrix containing dates in DT Scalar date/time format.
:doc:`../strctoposix`             Converts string dates to a matrix containing dates in Posix date/time format.
============================     ======================================================================

Sequences
-----------------------------

============================     ======================================================================
:doc:`../seqadt`                  Creates a sequence of dates in DT scalar format.
:doc:`../seqaposix`               Creates a sequence of dates in Posix date/time format.
============================     ======================================================================

Differences and arithmetic
-----------------------------

============================     ======================================================================
:doc:`../etdays`                  Difference between two times, as a 4x1 date vector returned by :doc:`../date`, in days.
:doc:`../ethsec`                  Difference between two times, as a 4x1 date vector returned by :doc:`../date`, in hundredths of a second.
:doc:`../hsec`                    Returns elapsed time since midnight in hundredths of a second.
:doc:`../timedeltadt`             Adds (or subtracts) time to a DT scalar.
:doc:`../timedeltaposix`          Adds (or subtracts) time to a posix date-time.
:doc:`../timediffdt`              Computes the difference between two dates in DT scalar format.
:doc:`../timediffposix`           Computes the difference between two dates in Posix date/time format.
============================     ======================================================================

Current time and date
-------------------------

============================     ======================================================================
:doc:`../dttime`                  Creates a matrix in DT scalar format containing only the hour, minute, and second. The date information is zeroed out.
:doc:`../todaydt`                 Returns system date in DT scalar format. The time returned is always midnight (00:00:00), the beginning of the returned day.
:doc:`../timedt`                  Returns system date and time in DT scalar format.
============================     ======================================================================

Other
-----------------

DTV Date Time Vectors
+++++++++++++++++++++++++

============================     ======================================================================
:doc:`../date`                    Returns current system date in a 4x1 vector.
:doc:`../datestr`                 Formats a 4x1 date vector, as returned by :doc:`../date`, as ``mm/dd/yy``.
:doc:`../datestring`              Formats a 4x1 date vector, as returned by :doc:`../date`, as ``mm/dd/yyyy``.
:doc:`../datestrymd`              Formats a 4x1 date vector, as returned by :doc:`../date`, as ``yyyymmdd``.
:doc:`../dayinyr`                 Returns the day of year as an integer from a 3x1 or 4x1 vector as returned by :doc:`../date`.
:doc:`../dayofweek`               Returns the day of week as an integer from a 3x1 or 4x1 vector as returned by :doc:`../date`.
:doc:`../dttodtv`                 Converts DT scalar format to DTV vector format.
:doc:`../dtvnormal`               Normalizes a date and time (DTV) vector.
:doc:`../dtvtodt`                 Converts DTV vector format to DT scalar format.
:doc:`../time`                    Returns current system time as a 4x1 vector.
:doc:`../timestr`                 Formats time as ``hh:mm:ss``
============================     ======================================================================

UTC functions
++++++++++++++++++

These functions are generally not recommended, because they will make adjustments based on your current time zone.

============================     ======================================================================
:doc:`../dttoutc`                 Converts DT scalar format to UTC scalar format.
:doc:`../dtvtoutc`                Converts DTV vector format to UTC scalar format.
:doc:`../timeutc`                 Returns the number of seconds since January 1, 1970 Greenwich Mean Time.
:doc:`../utctodt`                 Converts UTC scalar format to DT scalar format.
:doc:`../utctodtv`                Converts UTC scalar format to DTV vector format.
============================     ======================================================================

Other DT scalar functions
+++++++++++++++++++++++++++++

============================     ======================================================================
:doc:`../dtdate`                  Combines separate scalars or vectors representing year, month, day, hour, minute, second to create a matrix in DT scalar format.
:doc:`../dtday`                   Creates a matrix in DT scalar format containing only the year, month, and day. Time of day information is zeroed out.
============================     ======================================================================

Dataframe date variables
--------------------------

============================     ==========================================================================
:doc:`../asdate`                 Converts vectors in Posix time or string dates to a GAUSS date variable and optionally sets the date display format.
:doc:`../dtdayname`              Extracts the day from a date/time variable as a string name.
:doc:`../dtdayofmonth`           Extracts the day of the month from a date/time variable as a decimal number (1-31).
:doc:`../dtdayofweek`            Extracts the day of the week from a date/time variable as a decimal number. 
:doc:`../dtdayofyear`            Extracts the day of the year from a date/time variable as a decimal number (1-366). 
:doc:`../dthour`                  Extracts the hour from a date/time variable as a number (1-12 or 1-24).
:doc:`../dtminute`                Extracts the minute from a date/time variable as a number (0-59).
:doc:`../dtmonth`                 Extracts the month from a date/time variable as a decimal number(1-12).
:doc:`../dtmonthname`             Extracts the month from a date/time variable as a string name.
:doc:`../dtquarter`               Extracts the quarter from a date/time variable (1-4).
:doc:`../dtsecond`                Extracts the seconds from a date/time variable as a number (0-59).
:doc:`../dtweek`                  Extracts the week from a date/time variable as a number (0-53).
:doc:`../dtyear`                  Extracts the year from a date/time variable as a number.
:doc:`../getcoldateformats`      Gets BSD strftime format specifiers for specified columns of a dataframe.
:doc:`../setcoldateformats`      Specifies how GAUSS should display dates using the BSD strftime format specifiers. Note that this will also convert the type of the columns specified by column to Date.
============================     ==========================================================================
