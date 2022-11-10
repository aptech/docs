
dbnomics_series
==============================================

Purpose
----------------
Respond a list of series found by IDs, belonging potentially to different providers and datasets.

Format
----------------
.. function:: x = dbnomics_series(series_ids[, ...])
              x = dbnomics_series(provider_code, dataset_code, series_code[, ...])

    :param series_ids: List of series IDs separated by commas, or as a vector. A series ID is formatted like ``provider_code/dataset_code/series_code``. Series can belong to any provider and dataset.
    :type series_ids: array

    :param metadata: Optional. Default = 1. Return providers and datasets metadata in response. Used for reporting.
    :type metadata: bool

    :param limit: Optional. Default = 1000. The numbers of items to return.
    :type limit: integer

    :return x: A list of series
    :rtype x: Dataframe

Examples
----------------

Multiple series as a string
+++++++++++++++++++++++++++

::

    dbnomics_series("AMECO/ZUTN/EA19.1.0.0.0.ZUTN,AMECO/ZUTN/DNK.1.0.0.0.ZUTN,IMF/CPI/A.AT.PCPIT_IX");

::

    Provider: Annual macro-economic database of the European Commission's Directorate General for Economic and Financial Affairs (AMECO)
    Dataset: Unemployment rate: total :- Member States: definition EUROSTAT (ZUTN)
    Series: Annually – (Percentage of active population) – Euro area (EA19.1.0.0.0.ZUTN)
    Data last indexed on 2022-05-18T07:54:17.936Z

    Provider: Annual macro-economic database of the European Commission's Directorate General for Economic and Financial Affairs (AMECO)
    Dataset: Unemployment rate: total :- Member States: definition EUROSTAT (ZUTN)
    Series: Annually – (Percentage of active population) – Denmark (DNK.1.0.0.0.ZUTN)
    Data last indexed on 2022-05-18T07:54:17.936Z

    Provider: International Monetary Fund (IMF)
    Dataset: Consumer Price Index (CPI) (CPI)
    Series: Annual – Austria – Transport (A.AT.PCPIT_IX)
    Data last indexed on 2022-11-10T01:56:55.984Z

    period_start_day EA19.1.0.0.0.ZUT DNK.1.0.0.0.ZUTN    A.AT.PCPIT_IX 
          1958-01-01                .                .                . 
          1959-01-01                .                .                . 
          1960-01-01                .        2.0000000                . 
          1961-01-01                .        1.6000000                . 
          1962-01-01                .        1.4000000                . 
          1963-01-01                .        2.0000000                . 
          1964-01-01                .        1.2000000                . 


Multiple series as a vector
+++++++++++++++++++++++++++

::

    dbnomics_series("AMECO/ZUTN/EA19.1.0.0.0.ZUTN"$|
                    "AMECO/ZUTN/DNK.1.0.0.0.ZUTN"$|
                    "IMF/CPI/A.AT.PCPIT_IX");

::

    // Omitting output for brevity

    period_start_day EA19.1.0.0.0.ZUT DNK.1.0.0.0.ZUTN    A.AT.PCPIT_IX 
      1958-01-01                .                .                . 
      1959-01-01                .                .                . 
      1960-01-01                .        2.0000000                . 
      1961-01-01                .        1.6000000                . 
      1962-01-01                .        1.4000000                . 
      1963-01-01                .        2.0000000                . 
      1964-01-01                .        1.2000000                . 


Remarks
-----------

.. include:: remarks_dbnomics.rst
