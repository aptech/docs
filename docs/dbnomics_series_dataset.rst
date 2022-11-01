
dbnomics_series_dataset
==============================================

Purpose
----------------
Respond a list of series belonging to the same dataset.

Format
----------------
.. function:: x = dbnomics_series_dataset(dimensions, q[, ...])

    :param dimensions: JSON object describing the dimensions filtering the search. Can't be used with `series_code` parameter.
    :type dimensions: string

    :param q: Full-text search query
    :type q: string


    :param metadata: Optional. Default = True. Return providers and datasets metadata in response.
    :type metadata: bool

    :param format: Optional. Default = json. Format of the output. If using `csv` and response includes series of different frequencies, many CSV files will be produced, one per frequency, wrapped in a single ZIP file. Implies `observations=1` automatically.
    :type format: string

    :param limit: Optional. Default = 1000. The numbers of items to return.
    :type limit: integer

    :return x: A list of series
    :rtype x: Dataframe

Examples
----------------

::

    head(dbnomics_series_dataset("{"FREQ": ["A"]}", "GDP France"));

    

Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: 

