
dbnomics_last_updates
==============================================

Purpose
----------------
Respond a list of providers and a list of datasets sorted by creation/conversion date, most recent first.

Format
----------------
.. function:: x = dbnomics_last_updates([...])
    
    :param datasets.limit: Optional. Default = 100. The numbers of datasets to return.
    :type datasets.limit: integer

    :param providers.limit: Optional. Default = 100. The numbers of providers to return.
    :type providers.limit: integer

    :return x: A list of providers and datasets
    :rtype x: Dataframe

Examples
----------------

::

    head(dbnomics_last_updates());

    
            code         dir_hash       indexed_at             name        nb_series    provider_code    provider_name 
     SNA_TABLE8A a0426da302835dd6 2022-10-31T16:43 8A. Capital form        102805.00             OECD Organisation for 
              EO e21d1933b7515f10 2022-10-31T16:43 Economic Outlook        12961.000             OECD Organisation for 
             KEI 8fc330e997c458cc 2022-10-31T16:43 Key Short-Term E        7087.0000             OECD Organisation for 
   FDI_AGGR_SUMM 0a26e7a83658fc05 2022-10-31T16:43 FDI main aggrega        3748.0000             OECD Organisation for 
             MEI 1e34cbff28fce3f2 2022-10-31T16:43 Main Economic In        102373.00             OECD Organisation for 


Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: :func:`dbnomics_search`

