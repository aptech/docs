======
macfmt
======

10.0.36macfmt
=============

Purpose
-------
Finds an autocorrelation function matrix for multiple dependent
   variables.

Library
-------
tsmt

Format
------
x = macfmt( y, lag );

Input
-----
+-----+---------------------------------------------------------------+
   | y   | TxL matrix of data.                                           |
   +-----+---------------------------------------------------------------+
   | lag | scalar, the lag for which an autocorrelation matrix is        |
   |     | desired. Specify 0 to obtain the initial correlation.         |
   +-----+---------------------------------------------------------------+

Output
------
= ========================================================
   x LxL matrix of autocorrelations, *res* and *res*\ (-lag).
   = ========================================================
::

new;
cls;
library tsmt;

// Load and process data

//Create file name with full path
fname = getGAUSSHome() $+ "pkgs/tsmt/examples/mink.csv";

// Load all rows of the second and third columns of
// a space separated file
y = loadd(fname, "LogMink + LogMusk" );

// Difference the data
y = vmdiffmt( y, 1 );

// Estimate Varima Model

// Declare 'vctl' to be a varmamtControl structure
struct varmamtControl vctl;

// Fill 'vctl' with default values
vctl = varmamtControlCreate( );

// Turn off output
vctl.output = 0;

// Declare 'vout' to be a varmamtOut structure
// to hold the return values from 'vout'
struct varmamtOut vout;

// Estimate the parameters of the VAR(3) model
// and print diagnostic information
vout = varmaFit(y, 3, 0, 0, vctl );

// Get residuala
res = vout.residuals;

// Estimate autocorrelation function matrix
macf = macfmt( res, y );

print "Multivariate autocorrelation function matrix : ";
macf;

Source
------
varmamt.src
