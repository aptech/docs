The GC Compiler
===============

The **GC** compiler can be used in Makefiles or at a system command line to compile **GAUSS** programs. The syntax is as follows:

**gc [-**\ *flags*\ **]-o** *output_file source\_ file*

**gc [-**\ *flags*\ **][-d** *output directory*\ **]**\ *source_file source_file*\ **...**

The **-o** flag allows you to specify the name of the compiled file. If your *source_file* has a **.gau** extension, the default is to replace the **.gau** extension with **.gcg**. Otherwise, the default is to append **.gcg** to the name of your *source_file*. **GAUSS** will run compiled files only if they have a **.gcg** extension. Therefore, if you use the **-o** flag to specify an *output_file* name, you should give it a name with a **.gcg** extension.

The **-d** flag allows you to specify the directory in which the compiled files will reside. If you set the **-d** flag, all of the *source_files* you compile in that execution of **gc** will be placed in the specified directory. The default *output_directory* is the current working directory.

To specify a read only compile or execute, use **-roc** or **-roe**, respectively.
