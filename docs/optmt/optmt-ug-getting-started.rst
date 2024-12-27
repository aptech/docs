Getting Started
===============
The **Optimization MT** module contains a set of procedures for the solution of the optimization problem.

**GAUSS** version 16+ is required to use these routines.

The **Optimization MT 2.0** version number is stored in a global variable:

.. list-table::
    :widths: auto

    * - _optmt_ver 
      - 3x1 matrix the first element contains the major version number, the second element the minor version number, and the third element the revision number.

If you `contact technical support <https://www.aptech.com/support/submit-support-ticket/>`_, you may be asked for the version of your **Optimization MT** license.

README Files
----------------

If there is a **README.optmt** file, it contains any last-minute information on the **Optimization MT 2.0** procedures. Please read it before using them.

Setup
--------

In order to use the procedures in **Optimization MT** or **OPTMT** module, the **OPTMT** library must be active. This is done by including 'optmt' in the library statement at the top of your program or command file:

::

    library optmt;

This enables **GAUSS** to find the **OPTMT** procedures.
