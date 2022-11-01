
dbnomics_search
==============================================

Purpose
----------------
Respond a list of datasets from a full-text search.

Format
----------------
.. function:: x = dbnomics_search(q[, ...])

    :param q: Full-text search query
    :type q: string

    :param limit: Optional. Default = 10. The numbers of items to return.
    :type limit: integer

    :return x: A list of datasets
    :rtype x: Dataframe

Examples
----------------

::

    head(dbnomics_search("GDP France"));

                code         dir_hash       indexed_at             name nb_matching_seri        nb_series    provider_code    provider_name       updated_at 
         gov_10a_exp fab720436a1f72a3 2022-04-22T11:17 General governme        12800.000           129902         Eurostat         Eurostat 2022-04-22T00:00 
    CHELEM-TRADE-IND 7cfd7c7a78b84ede 2022-09-02T09:35 CHELEM - Interna        4937.0000           797304            CEPII Centre d'études                . 
        nasa_10_f_cp aa9a1cb003e7d567 2022-10-15T10:03 Financial accoun        4330.0000           163206         Eurostat         Eurostat 2022-10-15T00:00 
        nasa_10_f_bs 5fe95bd760e282a4 2022-10-27T11:06 Financial balanc        3670.0000           344205         Eurostat         Eurostat 2022-10-27T00:00 
        nasa_10_f_tr b69e7b63f3d59d44 2022-10-27T11:06 Financial transa        3655.0000           329303         Eurostat         Eurostat 2022-10-27T00:00 


Remarks
-----------

.. include:: remarks_dbnomics.rst

.. seealso:: 

