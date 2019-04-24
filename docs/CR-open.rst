
open
==============================================

Purpose
----------------

Opens an existing GAUSS data file.

.. _open:
.. index:: open

Format
----------------

::

    open fh = filename;
    open fh = filename for mode;
    open fh = filename for mode varindx ioffs;

**Parameters:**

:filename: (*literal or ^string*) name of the file on the disk. The name can include
    a path if the directory to be used is not the current directory. This
    filename will automatically be given the extension .dat. If an
    extension is specified, the *.dat* will be overridden. If the file
    is an *.fmt* matrix file, the extension must be explicitly given. If
    the name of the file is to be taken from a string variable, the name
    of the string must be preceded by the ``^`` (caret) operator.

:mode: (*literal*) the modes supported with the optional for subcommand are:

    .. csv-table::
        :widths: auto

        "read", "This is the default file opening mode and will be the one used if none is specified. Files opened in this mode cannot bewritten to. The pointer is set to the beginning of the file and the :func:`writer` function is disabled for files opened in this way. This is the only mode available for matrix files (*.fmt*), which are always written in one piece with the `save` command."
        "append", "Files opened in this mode cannot be read. The pointer will be set to the end of the file so that a subsequent write to the file with the :func:`writer` function will add data to the end of the file without overwriting any of the existing data in the file. The :func:`readr` function is disabled for files opened in this way. This mode is used to add additional rows to the end of a file."
        "update", "Files opened in this mode can be read from and written to. The pointer will be set to the beginning of the file. This mode is used to make changes in a file."

:offs: (*scalar*) offset added to "index variables"

    The optional *varindxi* subcommand tells GAUSS to
    create a set of global scalars that contain the index (column
    position) of the variables in a GAUSS data file. These "index
    variables" will have the same names as the corresponding variables
    in the data file but with "i" added as a prefix. They can be used
    inside index brackets, and with functions like submat to access
    specific columns of a matrix without having to remember the column
    position.

    The optional *offs* argument is an offset that will be added to the index
    variables. This is useful if data from
    multiple files are concatenated horizontally in one matrix. It can be
    any scalar expression. The default is 0.

    The index variables are useful for creating submatrices of specific
    variables without requiring that the positions of the variables be
    known. For instance, if there are two variables, xvar and yvar in
    the data set, the index variables will have the names *ixvar*,
    *iyvar*. If *xvar* is the first column in the data file, and *yvar*
    is the second, and if no offset, *offs*, has been specified, then
    *ixvar* and *iyvar* will equal 1 and 2 respectively. If an offset of
    3 had been specified, then these variables would be assigned the
    values 4 and 5 respectively.

    The *varindxi* option cannot be used with *.fmt* matrix
    files because no column names are stored with them.

    If *varindxi* is used, GAUSS will ignore the Undefined symbol
    error for global symbols that start with "i". This makes it much
    more convenient to use index variables because they don't have to be
    cleared before they are accessed in the program. Clearing is
    otherwise necessary because the index variables do not exist until
    execution time when the data file is actually opened and the names
    are read in from the header of the file. At compile time a statement like:
    ``y=x[.,ixvar];`` will be illegal if the compiler has never heard
    of *ixvar*. If *varindxi* is used, this error will be ignored for
    symbols beginning with "i". Any symbols that are accessed before
    they have been initialized with a real value will be trapped at
    execution time with a Variable not initialized error.


**Returns:**

:fh: (*scalar*), file handle.

    *fh* is the file handle which will be used by most
    commands to refer to the file within GAUSS. This file handle is
    actually a scalar containing an integer value that uniquely
    identifies each file. This value is assigned by GAUSS when the
    `open` command is executed. If the file was not successfully opened,
    the file handle will be set to -1.

Remarks
-------

The file must exist before it can be opened with the `open` command. To
create a new file, see `create` or `save`.

A file can be opened simultaneously under more than one handle. See the
second example following.

If the value that is in the file handle when the `open` command begins to
execute matches that of an already open file, the process will be
aborted and a *File already open* message will be given. This gives you
some protection against opening a second file with the same handle as a
currently open file. If this happens, you would no longer be able to
access the first file.

It is important to set unused file handles to zero because both `open` and
`create` check the value that is in a file handle to see if it matches
that of an open file before they proceed with the process of opening a
file. This should be done with `close` or `closeall`.


Examples
----------------

::

    fname = "/data/rawdat";
    open dt = ^fname for append;
    
    if dt == -1;
       print "File not found";
       end;
    endif;
    y = writer(dt,x);
    if y /= rows(x);
       print "Disk Full";
       end;
    endif;
    
    dt = close(dt);

In the example above, the existing data set ``/data/rawdat.dat`` is
opened for appending new data. The name of the file is in the string variable *fname*. In
this example the file handle is tested to see if the file was opened
successfully. The matrix *x* is written to this data set. The
number of columns in *x* must be the same as the number of columns in
the existing data set. The first row in *x* will be placed after the
last row in the existing data set. The :func:`writer` function will return
the number of rows actually written. If this does not equal the
number of rows that were attempted, then the disk is probably full.

::

    open fin = mydata for read;
    open fout = mydata for update;
    
    do until eof(fin);
       x = readr(fin,100);
       x[.,1 3] = ln(x[.,1 3];
       call writer(fout,x);
    endo;
    
    closeall fin,fout;

In the above example, the same file, *mydata.dat*, is opened twice with
two different file handles. It is opened for read with the handle
*fin*, and it is opened for update with the handle *fout*. This will
allow the file to be transformed in place without taking up the extra
space necessary for a separate output file. Notice that *fin* is
used as the input handle and *fout* is used as the output handle. The
loop will terminate as soon as the input handle has reached the end
of the file. Inside the loop the file is read into a matrix called
*x* using the input handle, the data are transformed (columns 1 and 3
are replaced with their natural logs), and the transformed data is
written back out using the output handle. This type of operation
works fine as long as the total number of rows and columns does not
change.

The following example assumes a data file named *dat1.dat* that has the
variables: *visc*, *temp*, *lub*, and *rpm*:

::

    open f1 = dat1 varindxi;
    dtx = readr(f1,100);
    x = dtx[.,irpm ilub ivisc];
    y = dtx[.,itemp];
    call seekr(f1,1);

In this example, the data set *dat1.dat* is opened for reading (the
*.dat* and the ``for read`` are implicit). *varindxi* is specified
with no constant. Thus, index variables are created that give the
positions of the variables in the data set. The first 100 rows of the
data set are read into the matrix *dtx*. Then, specified variables
in a specified order are assigned to the matrices *x* and *y* using
the index variables. The last line uses the :func:`seekr` function to
reset the pointer to the beginning of the file.

::

    open q1 = dat1 varindx;
    open q2 = dat2 varindx colsf(q1);
    nr = 100;
    y = readr(q1,nr)~readr(q2,nr);
    closeall q1,q2;

In this example, two data sets are opened for reading and index
variables are created for each. A constant is added to the indices
for the second data set (*q2*), equal to the number of variables
(columns) in the first data set (*q1*). Thus, if there are
three variables *x1*, *x2*, *x3* in *q1*, and three variables *y1*,
*y2*, *y3* in *q2*, the index variables that were created when the
files were opened would be *ix1*, *ix2*, *ix3*, *iy1*, *iy2*, *iy3*.
The values of these index variables would be 1, 2, 3, 4, 5, 6,
respectively. The first 100 rows of the two data sets are read in
and concatenated to produce the matrix *y*. The index variables will
thus give the correct positions of the variables in *y*.

::

    open fx = x.fmt;
    rf = rowsf(fx);
    sampsize = round(rf*0.1);
    rndsmpx = zeros(sampsize,colsf(fx));
    
    for(1, sampsize, 1);
       r = ceil(rndu(1,1)*rf);
       call seekr(fx,r);
       rndsmpx[i,.] = readr(fx,1);
    endfor;
    
    fx = close(fx);

In this example, a 10% random sample of rows is drawn from the
matrix file *x.fmt* and put into the matrix *rndsmpx*. Note that the
extension *.fmt* must be specified explicitly in the `open` statement.
The :func:`rowsf` command is used to obtain the number of rows in *x.fmt*.
This number is multiplied by 0.10 and the result is rounded to the
nearest integer; this yields the desired sample size. Then random
integers (*r*) in the range 1 to *rf* are generated. :func:`seekr` is used
to locate to the appropriate row in the matrix, and the row is read
with :func:`readr` and placed in the matrix *rndsmpx*. This is continued
until the complete sample has been obtained.

.. seealso:: Functions :func:`dataopen`, :func:`create`, :func:`close`, :func:`closeall`, :func:`readr`, :func:`writer`, :func:`seekr`, :func:`eof`

