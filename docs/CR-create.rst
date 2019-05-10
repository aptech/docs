
create
==============================================

Purpose
----------------

Creates and opens a GAUSS data set for subsequent writing.

Format
----------------
.. function:: create [[vflag]][[-w32]][[complex]] fh=filename with vnames, col, dtyp, vtyp 

    :param vflag: version flag.

        .. csv-table::
            :widths: auto
    
            "-v89", "obsoleted, use -v96."
            "-v92", "obsoleted, use-v96."
            "-v96", "supported on all platforms."

        For details on the various versions, see Foreign Language Interface, Chapter  1. 
        The default format can be specified in gauss.cfg by
        setting the dat_fmt_version configuration variable. The default, v96, should be used.

        .. DANGER:: FIX LINK TO FLI CHAP 1

    :type vflag: literal

    :param filename: filename is the name to be given to the file on the disk.
        The name can include a path if the
        directory to be used is not the current
        directory. This file will automatically be
        given the extension .dat. If an extension is
        specified, the .dat will be overridden. If
        the name of the file is to be taken from a
        string variable, the name of the string must be
        preceded by the ``^`` (caret) operator.
    :type filename: literal or ^string
        
    :param vnames: controls the names to be given to the
        columns of the data file. If the names are to
        be taken from a string or character matrix, the
        ``^`` (caret) operator must be placed before the
        name of the string or character matrix. The
        number of columns parameter, col, also has an
        effect on the way the names will be created. See
        below and see the examples for details on the
        ways names are assigned to a data file.
    :type vnames: literal or ^string or ^character matrix

    :param col: scalar expression containing the
        number of columns in the data file. If *col* is
        0, the number of columns will be controlled by
        the contents of *vnames*. If *col* is positive, the
        file will contain *col* columns and the names to
        be given each column will be created as
        necessary depending on the *vnames* parameter.
        See the examples.
    :type col: scalar expression

    :param dtyp: the precision used to store the data.
        This is a scalar expression containing 2, 4, or
        8, which is the number of bytes per element.

        .. csv-table::
            :widths: auto
    
            "2", "signed integer"
            "4", "single precision"
            "8", "double precision"
    
        .. csv-table::
            :widths: auto
            :header-rows: 1
    
            "Data Type", Digits, Range
            "integer",4,":math:`-32768 < X < 32768`"
            "single",6-7,":math:`43x10^{-37} < |X| < 3.37x10^{+38}`"
            "double",15-16,":math:`19x10^{-307} < |X| < 1.67x10^{-308}`"

        If the integer type is specified, numbers will berounded to the nearest integer as they are writtento the data set. If the data to be written to thefile contains character data, the precision must be 8 or the character information will be lost.

    :type dtyp: scalar

    :param vtyp: types of variables.
        The types of the variables
        in the data set. If :code:`rows(vtyp) * cols(vtyp) < col`, only the first element is used. Otherwise nonzero elements indicate
        a numeric variable and zero elements indicate character variables.
    :type vtyp: matrix

    :returns: fh (*scalar*) the file handle which will be used by most commands to refer to the file within
        GAUSS. This file handle is actually a scalar containing an integer value that uniquely
        identifies each file. This value is assigned by GAUSS when the
        create (or open) command is executed.

.. function:: create [[vflag]][[-w32]][[complex]] fh=filename using comfile

    :param vflag: version flag.

        .. csv-table::
            :widths: auto
    
            "-v89", "obsoleted, use -v96."
            "-v92", "obsoleted, use-v96."
            "-v96", "supported on all platforms."
    
        For details on the various versions, see Foreign Language Interface, Chapter  1. 
        The default format can be specified in gauss.cfg by
        setting the dat_fmt_version configuration variable. The default, v96, should be used.
    
        .. DANGER:: FIX LINK TO FLI CHAP 1

    :type vflag: literal

    :param filename: filename is the name to be given to the file on the disk.
        The name can include a path if the
        directory to be used is not the current
        directory. This file will automatically be
        given the extension .dat. If an extension is
        specified, the .dat will be overridden. If
        the name of the file is to be taken from a
        string variable, the name of the string must be
        preceded by the ``^`` (caret) operator.
    :type filename: literal or ^string

    :param comfile: the name of a command file that
        contains the information needed to create the
        file. The default extension for the command
        file is .gcf, which can be overridden.
        There are three possible commands in this file:

        ::

            numvar  n str;
            outvar  varlist;
            outtyp  dtyp;

        *numvar* and *outvar* are alternate ways of specifying the number and names of the
        variables in the data set to be created.
        
        When *numvar* is used, *n* is a constant which specifies the number of variables (columns) in
        the data file and  str is a string literal specifying the prefix to be given to all the variables. Thus:

        ::

            numvar 10 xx;
        
        says that there are 10 variables and that they are to be named *xx01* through *xx10*. The numeric
        part of the names will be padded on the left with zeros as necessary so the names will sort correctly:

        .. csv-table::
            :widths: auto
    
            "xx1 ... xx9","1-9 names"
            "xx01 ... xx10","10-99 names"
            "xx001 ... xx100","100-999 names"
            "xx0001 ... xx1000","1000-8100 names"
    
        If *str* is omitted, the variable prefix will be "X". When *outvar* is used, *varlist* is a list 
        of variable names, separated by spaces or commas. For instance: :code:`outvar x1, x2, zed;` specifies 
        that there are to be 3 variables per row of the data set, and that they are to be named ``X1, X2, ZED``, 
        in that :code:`order.outtyp` specifies the precision. It can be a constant: 2, 4, or 8, or it can be 
        a literal: ``I, F, or D``. For an explanation of the available data types, see dtyp in ``create... with...`` 
        previously. The *outtyp* statement does not have to be included. If it is not, then all data will 
        be stored in 4 bytes as single precision floating point numbers.

    :type comfile: literal or ^string

    :returns: fh (*scalar*) the file handle which will be used by most commands to refer to the file within
        GAUSS. This file handle is actually a scalar containing an integer value that uniquely
        identifies each file. This value is assigned by GAUSS when the
        create (or open) command is executed.

Remarks
-------

If the complex flag is included, the new data set will be initialized to
store complex number data. Complex data is stored a row at a time, with
the real and imaginary halves interleaved, element by element.

The -w32 flag is an optimization for Windows. It is ignored on all other
platforms. GAUSS 7.0 and later use Windows system file write commands
that support 64-bit file sizes. These commands are slower on Windows XP
than the 32-bit file write commands that were used in GAUSS 6.0 and
earlier. If you include the -w32 flag, successive writes to the file
indicated by fh will use 32-bit Windows write commands, which will be
faster on Windows XP. Note, however, that the -w32 flag does not support
64-bit file sizes.


Examples
----------------

::

    let vnames = age sex educat wage occ;
    create f1 = simdat with ^vnames,0,8;
    
    obs = 0; nr = 1000;
    do while obs < 10000;
       data = rndn(nr,colsf(f1));
       if writer(f1,data) /= nr;
          print "Disk Full";
          end;
       endif;
       obs = obs+nr;
    endo;
    
    closeall f1;

This example uses ``create... with...`` to create a
double precision data file called simdat.dat on
the default drive with 5 columns. The :func:`writer`
command is used to write 10000 rows of Normal random
numbers into the file. The variables (columns) will
be named: ``AGE, SEX, EDUCAT, WAGE, OCC``.

Here are some examples of the variable names that will result when
using a character vector of names in the argument to
the create function.

::

    vnames = { AGE PAY SEX JOB };
    typ = { 1, 1, 0, 0 };
    create fp = mydata with ^vnames,0,8,typ;

The names in the this example will be: ``AGE, PAY, SEX, JOB``.

``AGE`` and ``PAY`` are numeric variables, ``SEX`` and ``JOB`` are character variables.

::

    create fp = mydata with ^vnames,3,2;

The names will be: ``AGE, PAY, SEX``.

::

    create fp = mydata with ^vnames,8,2;

The names will now be: ``AGE, PAY, SEX, JOB1, JOB2, JOB3, JOB4, JOB5``.

If a literal is used for the *vnames* parameter, 
the number of columns should be explicitly given in
the *col* parameter and the names will be created as
follows:

::

    create fp = mydata with var,4,2;

Giving the names: ``VAR1, VAR2, VAR3, VAR4``.

The next example assumes a command file
called comd.gcf containing the following lines, 
created using a text editor:

::

    outvar age, pay, sex;
    outtyp i;

Then the following program could be used to write
100 rows of random integers into a file called
smpl.dat in the subdirectory called /gauss/data:

::

    filename = "/gauss/data/smpl";
    create fh = ^filename using comd;
    x = rndn(100,3)*10;
    if writer(fh,x) /= rows(x);
      print "Disk Full"; 
      end;
    endif;
    closeall fh;

For platforms using the backslash as a path separator,
remember that two backslashes (''``\\``'') are required to
enter one backslash inside of double quotes. This
is because a backslash is the escape character used
to embed special characters in strings.

.. seealso:: Functions :func:`datacreate`, :func:`datacreatecomplex`, `open`, :func:`readr`, :func:`writer`, :func:`eof`, :func:`close`, `output`, :func:`iscplxf`

