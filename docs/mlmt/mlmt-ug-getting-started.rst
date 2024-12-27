Getting Started
===============
The **Maximum Likelihood MT 3.0** module contains a set of procedures for the solution of the maximum likelihood problem.

**GAUSS** version 18+ is required to use these routines.

The **Maximum Likelihood MT 3.0** version number is stored in a global variable:

.. list-table::
    :widths: auto

    * - _maxlikmt_ver 
      - 3x1 matrix the first element contains the major version number, the second element the minor version number, and the third element the revision number.

If you `contact technical support <https://www.aptech.com/support/submit-support-ticket/>`_, you may be asked for the version of your **Maximum Likelihood MT** license.

README Files
----------------

If there is a **README.mlmt** file, it contains any last-minute information on the **Maximum Likelihood MT 3.0** procedures. Please read it before using them.

Setup
--------

In order to use the procedures in **Maximum Likelihood MT** or **MLMT** module, the **maxlikmt** library must be active. This is done by including 'cmlmt' in the library statement at the top of your program or command file:

::

    library cmlmt;

This enables **GAUSS** to find the **MLMT** procedures.
