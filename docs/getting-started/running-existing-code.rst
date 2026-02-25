
Running Existing Code
=====================

You've inherited GAUSS code from a colleague, downloaded replication files for a paper, or received code from your advisor. This guide helps you get it running.

Opening and Running a File
--------------------------

GAUSS programs are text files, typically with ``.e`` or ``.prg`` extensions.

**In the GAUSS IDE:**

1. File → Open (or Ctrl+O / Cmd+O)
2. Navigate to your ``.e`` or ``.prg`` file
3. Click the Run button (green arrow) or press F5

**From the command line:**

::

    # Run a program file
    tgauss -b myprogram.e

    # The -b flag runs in batch mode (exits when done)

Common First-Run Errors
-----------------------

File Not Found
^^^^^^^^^^^^^^

::

    error G0014 : 'loadd' : File not found: data.csv

**Cause:** GAUSS can't find a data file the code references.

**Solutions:**

1. **Check the working directory.** The code may assume files are in a specific location.

   ::

       // See current working directory
       print cdir(0);

       // Change to the folder containing your data
       chdir("/path/to/your/data");

2. **Use absolute paths.** Edit the code to specify the full path:

   ::

       // Instead of:
       data = loadd("mydata.csv");

       // Use:
       data = loadd("/Users/you/research/project/mydata.csv");

3. **Copy data files** to the same folder as the ``.e`` file.

Undefined Symbol
^^^^^^^^^^^^^^^^

::

    error G0025 : Undefined symbol: 'olsmt'

**Cause:** The code uses a function that isn't loaded.

**Solutions:**

1. **Missing library statement.** Add at the top of the file:

   ::

       library pgraph, cmlmt;  // Load required libraries

2. **Missing add-on package.** Some functions require separately installed packages:

   - ``olsmt``, ``glm`` → Base GAUSS (should work)
   - ``varma``, ``varmares`` → TSMT (Time Series MT)
   - ``dcc``, ``garch`` → FANPAC or TSMT
   - ``cmlmt``, ``comt`` → Optimization packages
   - ``dcm`` → Discrete Choice Models

   Check Help → Application Manager to see installed packages.

3. **Missing procedure definition.** The code may call a custom procedure defined in another file. Look for:

   ::

       // Load procedures from another file
       #include "helper_functions.src"

   Make sure that file exists in the same directory or in your GAUSS source path.

Library Not Found
^^^^^^^^^^^^^^^^^

::

    error G0044 : Library not found: tsmt

**Cause:** Code requires an add-on package you don't have.

**Solution:** Contact Aptech to purchase/license the required package, or comment out the library statement and related code to see what else runs.

Understanding Code Structure
----------------------------

GAUSS programs typically follow this structure:

::

    // 1. Library declarations (load functionality)
    library pgraph;

    // 2. Global settings or data paths
    data_path = "/path/to/data/";

    // 3. Load data
    data = loadd(data_path $+ "mydata.csv");

    // 4. Data preparation
    y = data[., 1];
    x = data[., 2:cols(data)];

    // 5. Analysis
    call olsmt(data, "y ~ x1 + x2");

    // 6. Output/plots
    plotXY(x, y);

Key Syntax to Recognize
-----------------------

**Semicolons** end statements (required):

::

    x = 5;      // Correct
    x = 5       // Error: missing semicolon

**Comments:**

::

    // Single line comment
    /* Multi-line
       comment */

**String concatenation** uses ``$+``:

::

    path = "/data/" $+ "file.csv";

**Matrix indexing** uses square brackets (1-based):

::

    x[1, 2]     // Row 1, column 2
    x[1:5, .]   // Rows 1-5, all columns
    x[., 1]     // All rows, column 1

**Procedures** are defined with ``proc`` and ``endp``:

::

    proc (1) = myfunction(x);
        local result;
        result = x^2;
        retp(result);
    endp;

Installing Required Libraries
-----------------------------

If code requires add-on packages:

1. **Check what's installed:** Help → Application Manager
2. **Install free updates:** Help → Check for Updates
3. **Purchase add-ons:** Contact sales@aptech.com

Common packages for econometrics:

================= ===============================================
Package           Functions
================= ===============================================
TSMT              Time series: VAR, GARCH, state-space, forecasting
Optmum/CO/ML      Optimization, maximum likelihood
DCM               Discrete choice models
FANPAC            Financial analysis, GARCH variants
================= ===============================================

Setting Up Source Paths
-----------------------

If code includes files from multiple directories:

::

    // Add a directory to the source path
    addpath("/path/to/shared/procedures");

Or set paths permanently in GAUSS:

1. Edit → Preferences → Source Path
2. Add directories containing your ``.src`` files

Debugging Tips
--------------

**Print intermediate values:**

::

    print "x dimensions:" rows(x) cols(x);
    print "First 5 rows:";
    print x[1:5, .];

**Step through code:** Use the GAUSS debugger (F8 to set breakpoint, F5 to run to breakpoint).

**Check variable types:**

::

    print type(x);   // 6 = matrix, 13 = dataframe, 15 = string

**Run code section by section:** Highlight lines and press F4 to run selection.

Getting Help
------------

For specific functions:

::

    // In the command window
    help loadd

Or press F1 with cursor on a function name.

.. seealso::

    :doc:`quickstart` — Learn GAUSS basics from scratch
    :doc:`../troubleshooting` — Common error messages explained
