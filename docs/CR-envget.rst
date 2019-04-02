
envget
==============================================

Purpose
----------------

Searches the environment table for a defined name.

Format
----------------
.. function:: envget(s)

    :param s: the name to be searched for.
    :type s: string

    :returns: y (*string*), the string that corresponds to that
        name in the environment table or a null string if it
        is not found.

Examples
----------------

Example 1
+++++++++

::

    //%USERPROFILE% is the user's home
    //directory on most Windows systems
    hm_dir = envget("USERPROFILE");

Example 2
+++++++++

Below is an example of a procedure that will open a data file using a path stored in an environment string called ``DPATH``.

::

    proc dopen(file);
       local fname,fp;
       fname = envget("DPATH");
       //Check to see if DPATH is set or empty
       if fname $== "";
          fname = file;
       else;
          //Check to see if 'fname' ends with
          //a path separator
          if strsect(fname,strlen(fname),1) $== "\\";
             fname = fname $+ file;
          else;
             fname = fname $+ "\\" $+ file;
          endif;
       endif;
       open fp = ^fname;
       retp(fp);
    endp;

The procedure returns the file handle and is called as follows:

::

    fp = dopen("myfile");

.. seealso:: Functions :func:`cdir`

