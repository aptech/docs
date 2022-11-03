
dbnomics_series_dataset_filter
==============================================

Purpose
----------------
Respond a specific series from a dataset.

Format
----------------
.. function:: x = dbnomics_series_dataset_filter(provider_code, dataset_code, series_code[, ...])

    :param provider_code: The code of a provider.
    :type provider_code: string

    :param dataset_code: The code of a dataset.
    :type dataset_code: string

    :param series_code: A series code mask is an alternative way to express a dimension filter.

        Series codes masks can designate many series by:

        - removing a constraint on a dimension, for example ``M..PCPIEC_WT``;
        - enumerating many values for a dimension, separated by a '+', for example ``M.FR+DE.PCPIEC_WT``;

          - if values contains '+', they can be protected with double quotes. Example: 'A+"FR+BE"' will enumerate series for 'A' and 'FR+BE' dimensions.

        - combining these possibilities many times in the same code mask.

        If the rightmost dimension value code is removed, then the final '.' can be removed too: ``A.FR.`` = ``A.FR```.

    :type series_code: string

    :param q: Full-text search query. Optional.
    :type q: string

    :param metadata: Optional. Default = True. Return providers and datasets metadata in response.
    :type metadata: bool

    :param limit: Optional. Default = 1000. The numbers of items to return.
    :type limit: integer

    :return x: A list of series
    :rtype x: Dataframe

Examples
----------------

::

    head(dbnomics_series_dataset_filter("AMECO", "ZUTN", "AUS.1.0.0.0.ZUTN"));

::

    Dataset: Unemployment rate: total :- Member States: definition EUROSTAT (ZUTN)
    Series: Annually – (Percentage of active population) – Australia (AUS.1.0.0.0.ZUTN)
    Data last indexed on 2022-05-18T07:54:17.936Z

    period_start_day AUS.1.0.0.0.ZUTN 
          1960-01-01        1.2465941 
          1961-01-01        2.4554879 
          1962-01-01        2.3192186 
          1963-01-01        1.8671577 
          1964-01-01        1.4482868 

Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: :func:`dbnomics_series`, :func:`dbnomics_series_dataset`

