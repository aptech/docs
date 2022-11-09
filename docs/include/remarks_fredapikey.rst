API Key
++++++++++

This function **requires a valid API key**. `Read here <https://fred.stlouisfed.org/docs/api/api_key.html>`_ to find out more on how to obtain one.

Set your API key using any of the following methods in GAUSS:

#. Set the API key directly at the top of your program:

   ::

       FRED_API_KEY = "your_api_key"

#. Set the environment variable ``FRED_API_KEY`` to your API key.
#. Edit your gauss.cfg file and modify the ``fred_api_key`` value:

   ::
    
       fred_api_key = your_api_key

Disclaimer
++++++++++++

.. note:: This product uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis.
