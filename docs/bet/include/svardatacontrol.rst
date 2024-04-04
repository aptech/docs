.. list-table::
   :widths: auto

   * - svard0.loadpath
     - String, source path for the file where data is stored.
   * - svard0.filename
     - String, filename where data is stored. For text or CSV files, the filename should include the extension.
   * - svard0.filetype
     - String, filetype. Options include "TXT", "CSV", "XLS", or "XLXS".
   * - svard0.range
     - String, range of cells where data is stored if the file is an XLS or XLXS.
   * - svard0.sheet
     - Scalar, sheet number where data is stored if the file is an XLS or XLXS.
   * - svard0.frequency
     - Scalar, annual frequency of data if the data is a time series.
   * - svard0.data
     - Matrix, data from the file is placed for storage in the data matrix. Should not be filled by the user.
   * - svard0.ti
     - Matrix, time index vector created during **GAUSS** initialization function.
