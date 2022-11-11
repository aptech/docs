
dbnomics_series_dataset
==============================================

Purpose
----------------
Respond a list of series belonging to the same dataset.

Format
----------------
.. function:: x = dbnomics_series_dataset(provider_code, dataset_code, [, ...])

    :param provider_code: The code of a provider.
    :type provider_code: string

    :param dataset_code: The code of a dataset.

    :type dataset_code: string

    :param dimensions: Optional. JSON object describing the dimensions filtering the search.
    :type dimensions: string

    :param q: Optional. Full-text search query
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

    dbnomics_series_dataset("AMECO", "ZUTN");

::

    // <Report Information Omitted>

    period_start_day ALB.1.0.0.0.ZUTN AUS.1.0.0.0.ZUTN AUT.1.0.0.0.ZUTN BEL.1.0.0.0.ZUTN BGR.1.0.0.0.ZUTN CAN.1.0.0.0.ZUTN CHE.1.0.0.0.ZUTN CYP.1.0.0.0.ZUTN CZE.1.0.0.0.ZUTN DA12.1.0.0.0.ZUT DEU.1.0.0.0.ZUTN DNK.1.0.0.0.ZUTN DU15.1.0.0.0.ZUT D_W.1.0.0.0.ZUTN EA12.1.0.0.0.ZUT EA19.1.0.0.0.ZUT ESP.1.0.0.0.ZUTN EST.1.0.0.0.ZUTN EU15.1.0.0.0.ZUT EU27.1.0.0.0.ZUT FIN.1.0.0.0.ZUTN FRA.1.0.0.0.ZUTN GBR.1.0.0.0.ZUTN GRC.1.0.0.0.ZUTN HRV.1.0.0.0.ZUTN HUN.1.0.0.0.ZUTN IRL.1.0.0.0.ZUTN ISL.1.0.0.0.ZUTN ITA.1.0.0.0.ZUTN JPN.1.0.0.0.ZUTN KOR.1.0.0.0.ZUTN LTU.1.0.0.0.ZUTN LUX.1.0.0.0.ZUTN LVA.1.0.0.0.ZUTN MKD.1.0.0.0.ZUTN MLT.1.0.0.0.ZUTN MNE.1.0.0.0.ZUTN NLD.1.0.0.0.ZUTN NOR.1.0.0.0.ZUTN NZL.1.0.0.0.ZUTN POL.1.0.0.0.ZUTN PRT.1.0.0.0.ZUTN ROM.1.0.0.0.ZUTN SRB.1.0.0.0.ZUTN SVK.1.0.0.0.ZUTN SVN.1.0.0.0.ZUTN SWE.1.0.0.0.ZUTN TUR.1.0.0.0.ZUTN USA.1.0.0.0.ZUTN 
          1960-01-01                .        1.2465941        2.0000000        2.2000000                .        6.8751050      0.050324600                .                .        2.3976968                .        2.0000000                .       0.70000000                .                .        2.4000000                .                .                .        1.4000000        1.4000000                .        5.8000000                .                .        5.7000000                .        5.3000000        1.7000000                .                .        0.0000000                .                .                .                .        1.0000000        1.2000000                .                .        2.0000000                .                .                .                .        1.9000000        8.0000000        5.5000000 
          1961-01-01                .        2.4554879        1.5000000        1.8000000                .        7.0646304      0.025357700                .                .        2.1535685                .        1.6000000                .       0.50000000                .                .        2.4000000                .                .                .        1.1000000        1.2000000                .        5.6000000                .                .        5.3000000                .        4.8000000        1.5000000                .                .        0.0000000                .                .                .                .       0.70000000       0.90000000                .                .        2.4000000                .                .                .                .        1.7000000        7.9000000        6.7000000 
          1962-01-01                .        2.3192186        1.6000000        1.7000000                .        5.8350488      0.022605900                .                .        1.9414196                .        1.4000000                .       0.40000000                .                .        1.6000000                .                .                .        1.2000000        1.4000000                .        4.9000000                .                .        5.2000000                .        4.3000000        1.3000000                .                .        0.0000000                .                .                .                .       0.70000000        1.0000000                .                .        2.6000000                .                .                .                .        1.7000000        8.9000000        5.5000000 
          1963-01-01                .        1.8671577        1.7000000        1.5000000                .        5.4842802      0.030661200                .                .        1.8953517                .        2.0000000                .       0.50000000                .                .        2.0000000                .                .                .        1.4000000        1.5000000                .        4.9000000                .                .        5.4000000                .        3.6000000        1.3000000                .                .        0.0000000                .                .                .                .       0.80000000        1.3000000                .                .        2.8000000                .                .                .                .        1.9000000        8.5000000        5.7000000 
          1964-01-01                .        1.4482868        1.6000000        1.4000000                .        4.6253888      0.010540900                .                .        2.0072257                .        1.2000000                .       0.50000000                .                .        2.8000000                .                .                .        1.4000000        1.2000000                .        4.7000000                .                .        5.2000000       0.20000000        4.1000000        1.2000000                .                .        0.0000000                .                .                .                .       0.60000000        1.1000000                .                .        2.9000000                .                .                .                .        1.8000000        8.3000000        5.2000000 

Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: :func:`dbnomics_series`, :func:`dbnomics_series_dataset_filter`

