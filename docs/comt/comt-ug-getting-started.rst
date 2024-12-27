Getting Started
===============
The **Constrained Optimization MT** module contains a set of procedures for the solution of the optimization problem.

**GAUSS** version 16+ is required to use these routines.

The **Constrained Optimization MT 2.0** version number is stored in a global variable:

.. list-table::
    :widths: auto

    * - _comt_ver 
      - 3x1 matrix the first element contains the major version number, the second element the minor version number, and the third element the revision number.

If you `contact technical support <https://www.aptech.com/support/submit-support-ticket/>`_, you may be asked for the version of your **Constrained Optimization MT** license.

README Files
----------------

If there is a **README.comt** file, it contains any last-minute information on the **Constrained Optimization MT 2.0** procedures. Please read it before using them.

Setup
--------

In order to use the procedures in **Constrained Optimization MT** or **COMT** module, the **COMT** library must be active. This is done by including 'comt' in the library statement at the top of your program or command file:

::

    library comt;

This enables **GAUSS** to find the **COMT** procedures.
