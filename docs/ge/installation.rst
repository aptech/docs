Installation
============

Upgrading from a Previous Version
----------------------------------

All existing code, compiled **.gcg** files, and API calls are fully backward compatible with GAUSS Engine 26. To upgrade, replace the installation files and update your environment variable from **MTENGHOME25** to **MTENGHOME26**. No code changes are required.

Linux
----------

Installing the Files 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From CD or download, copy the **.tar.gz** file to **/tmp**

Choose a directory to install the **GAUSS Engine** to. We’ll assume the final path is going to be **/usr/local/mteng26**

Go to that directory.

cd /usr/local

Extract the files:

tar xvf /tmp/*tar_file_name*

Change to the newly created mteng26 directory:

cd mteng26

The **GAUSS Engine** files are now in place.

**NOTE**: If you choose to install **GAUSS Engine** in a directory which does not have write permissions for normal user accounts such as **/opt** or **/usr/local**, then you must choose the *Advanced Installation* and *Multi-User Installation* options during installation.

Run the executable script:

./**ginstall**

1. This script will give you the option of a *default* or *advanced* install. The default option will install everything under the current directory. The advanced installation allows you to choose a single-user or multi-user installation and also allows you to place the shared libraries that the **GAUSS Engine** depends on in another location. If you choose a multi-user installation, the binaries and most of the rest of the installation will reside in the current directory. Each time a new user (a user that has never started **GAUSS Engine** on this machine ) starts **GAUSS Engine** on this machine, **GAUSS Engine** will create a local working directory for that user under the user's home directory. This local working directory will contain the files and folders that which may be customized by the user. This allows the admin to install **GAUSS Engine** in a location without universal write privileges. No files will be placed under the home directory of any user who does not start **GAUSS Engine**. Place the installation directory in the executable path.

Licensing 
~~~~~~~~~~~~~~~~~

The hostid of your machine is written to a text file during installation in your **GAUSS Engine** installation directory called **myhostid.txt** You will need your computer’s hostid to receive your license. To receive a license and license installation instructions, go to: **https://www.aptech.com/support/license**/ and provide the requested information:

Configuring the Environment 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to set an environment variable called **MTENGHOME26** that points to the installation directory.

**Cshell** 
^^^^^^^^^^^

setenv MTENGHOME26 /usr/local/mteng26

**Korn, Bourne shell** 
^^^^^^^^^^^^^^^^^^^^^^^

export MTENGHOME26=/usr/local/mteng26

The **GAUSS Engine** looks in **$MTENGHOME26** for its configuration file, **gauss.cfg**. Anyone who will be running the **GAUSS Engine** needs to have at least *read* access to this file. The name of the environment variable can be changed to something other than **MTENGHOME26** by calling **GAUSS_SetHomeVar**

By default the **GAUSS Engine** creates temporary files in **/tmp**. You can change this by editing **gauss.cfg–look** for the **tmp_path** configuration variable. If you change it, anyone who uses the **GAUSS Engine** will need *read/write/execute* access to the directory you specify.

Testing the Installation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the above steps, you can build some of the sample programs to verify the correctness of the installation. See Chapter 2 for details.

Swap Space 
~~~~~~~~~~~~~~~~~~

The **GAUSS Engine** uses **malloc** and the normal system swap space. This system is dynamic and requires no workspace size setting. Make sure your system has enough swap space to handle the size and number of matrices you will be needing simultaneously. Each matrix takes 8 × rows × columns bytes.

GAUSS Run-Time Engine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have purchased the **GAUSS Run-Time Engine (GRTE)**, you will see the shared library lib **mtengrt**. To use the GRTE, use **-lmtengrt** instead of **-lmteng** in your Makefile. The **GRTE** will not create globals. It is to be used with compiled **.gcg** files that have been compiled with the **GAUSS Engine**.

To create compiled files, use the **compile** command from the command line interface, **engauss**, the graphical user interface, **gauss**, or the **gc** executable. Your application can call **GAUSS_LoadCompiledFile** to load the program contained in the .\ **gcg** file.

Any global variables that are assigned within a **GAUSS** program or using the API assignment functions must be initialized in the **.gcg** file. **GAUSS_CompileString** can be used with the **GRTE** as long as it does not create new globals.

macOS
---------


Installing the Files 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From CD or download:

- Save the .\ **zip** file on your hard drive

- Browse to the folder where you saved the .\ **zip** file

- Extract the files

- Double-click on the ***.pkg** file to launch the installer.

The **GAUSS Engine** files are now in place.


Licensing 
~~~~~~~~~~~~~~~~~

The hostid of your machine is written to a text file during installation in your **GAUSS Engine** installation directory called **myhostid.txt** You will need your computer’s hostid to receive your license. To receive a license and license installation instructions, go to: **https://www.aptech.com/support/license**/ and provide the requested information:


Configuring the Environment 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to set an environment variable called **MTENGHOME26** that points to the installation directory.


**Korn, Bourne shell** 
^^^^^^^^^^^^^^^^^^^^^^^

export MTENGHOME26=/Users/$USER/mteng26

The **GAUSS Engine** looks in **$MTENGHOME26** for its configuration file, **gauss.cfg**. Anyone who will be running the **GAUSS Engine** needs to have at least *read* access to this file. The name of the environment variable can be changed to something other than **MTENGHOME26** by calling **GAUSS_SetHomeVar**

By default the **GAUSS Engine** creates temporary files in **/tmp**. You can change this by editing **gauss.cfg**–look for the **tmp_path** configuration variable. If you change it, anyone who uses the **GAUSS Engine** will need *read/write/execute* access to the directory you specify.


Testing the Installation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the above steps, you can build some of the sample programs to verify the correctness of the installation. See Chapter 2 for details.


Swap Space 
~~~~~~~~~~~~~~~~~~

The **GAUSS Engine** uses **malloc** and the normal system swap space. This system is dynamic and requires no workspace size setting. Make sure your system has enough swap space to handle the size and number of matrices you will be needing simultaneously. Each matrix takes 8 × rows × columns bytes.


GAUSS Run-Time Engine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have purchased the **GAUSS Run-Time Engine (GRTE)**, you will see the shared library lib **mtengrt**. To use the GRTE, use **-lmtengrt** instead of **-lmteng** in your Makefile. The **GRTE** will not create globals. It is to be used with compiled **.gcg** files that have been compiled with the **GAUSS Engine**.

To create compiled files, use the **compile** command from the command line interface, **engauss**, the graphical user interface, **gauss**, or the **gc** executable. Your application can call **GAUSS_LoadCompiledFile** to load the program contained in the .\ **gcg** file.

Any global variables that are assigned within a **GAUSS** program or using the API assignment functions must be initialized in the **.gcg** file. **GAUSS_CompileString** can be used with the **GRTE** as long as it does not create new globals.


Windows 
------------


Installing the Files 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From CD 
^^^^^^^^

Insert the CD into a CD drive, and setup should start automatically. If setup does not start automatically:

- Browse to the CD-ROM drive

- Double-click on the ***.exe** file to launch the installer.

- Follow the prompts to select a directory to install to and copy the **GAUSS Engine** files to your hard drive.

From Download 
^^^^^^^^^^^^^^

Download the **GAUSS Engine** from your Premier Support Download Account and do the following:

- Save the .\ **zip** file on your hard drive

- Browse to the folder where you saved the .\ **zip** file

- Extract the files

- Double-click on the ***.exe** file to launch the installer.

- Follow the prompts to select a directory to install to and copy the **GAUSS Engine** files to your hard drive.


Licensing 
~~~~~~~~~~~~~~~~

To receive a license and license installation instructions, type this link in your internet browser and provide the content of **myhostid.txt** and other requested information: **https://www.aptech.com/support/license/**

The hostid number of your machine is usually generated automatically and will be displayed during installation in a text file that is stored in your main **GAUSS Engine** directory called **myhostid.txt**


Configuring the Environment 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **GAUSS Engine** examples require an environment variable called **MTENGHOME26** that points to the installation directory.

POSIX Threads 
~~~~~~~~~~~~~~~~~~~~

The **GAUSS Engine** for Windows is implemented using POSIX threads forWin32. you can obtain the Pthreads library from:

https://sources.redhat.com/pthreads-win32/

The **GAUSS Engine** for Windows was linked using **pthreadVC2.dll** and **pthreadVC2.lib**. You need both the .dll and the .lib

file to link with the **GAUSS Engine**.

You will also need:

pthread.h

semaphore.h

sched.h


Testing the Installation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the above steps, you can build some of the sample programs to verify the installation. See **Chapter 2** for details.


Swap Space 
~~~~~~~~~~~~~~~~~

The **GAUSS Engine** now uses **malloc** and the normal system swap space. This system is dynamic and requires no workspace size setting. Make sure your system has enough swap space to handle the size and number of matrices you will be needing simultaneously. Each matrix takes 8 × rows × columns bytes.


GAUSS Run-Time Engine 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have purchased the **GAUSS Run-Time Engine (GRTE)**, you will find **mtengrt.dll** and **mtengrt.lib**. To use it, link with these instead of **mteng.dll** and **mteng.lib** in your Makefile.

The **GRTE** will not create GAUSS global variables. It is to be used with compiled GAUSS code (**.gcg)** files that have been compiled with the **GAUSS Engine.**

To create compiled files, use the **compile** command from the command line interface, **engauss** or the **gc** executable. Your application can call **GAUSS_LoadCompiledFile** to load the program contained in the .\ **gcg** file.

Any global variables that are assigned within a **GAUSS** program or using the API assignment functions must be initialized in the **.gcg** file. **GAUSS_CompileString** can be used with the **GRTE** as long as it does not create new globals.
