Getting Started
===============
The **Constrained Maximum Likelihood MT** module contains a set of procedures for the solution of the maximum likelihood problem.

**GAUSS** version 16+ is required to use these routines.

The **Constrained Maximum Likelihood MT 3.0** version number is stored in a global variable:

.. list-table::
    :widths: auto

    * - _cmlmt_ver 
      - 3x1 matrix the first element contains the major version number, the second element the minor version number, and the third element the revision number.

If you `contact technical support <https://www.aptech.com/support/submit-support-ticket/>`_, you may be asked for the version of your **Constrained Maximum Likelihood MT** license.

README Files
----------------

If there is a **README.cmlmt** file, it contains any last-minute information on the **Constrained Maximum Likelihood MT 3.0** procedures. Please read it before using them.

Setup
--------

In order to use the procedures in **Constrained Maximum Likelihood MT** or **CMLMT** module, the **CMLMT** library must be active. This is done by including 'cmlmt' in the library statement at the top of your program or command file:

::

    library cmlmt;

This enables **GAUSS** to find the **CMLMT** procedures.
