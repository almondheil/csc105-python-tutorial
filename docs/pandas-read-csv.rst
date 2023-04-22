.. _chap-reading-files:

=============
Reading Files
=============
]
.. _sec-csv-files:

CSV Files
=========

Before we start, we'll want to create a couple of files. In your replit, make a new file called `file-io.py`. For now, it will stay empty.

Then, make a new file called simple-data.csv. In it, paste in the following
text which represents the stock of some warehouse.

.. literalinclude:: code/simple-data.csv

This data is in something called "Comma Separated Value (CSV)" format. You're
probabily familiar with it if you've taken a science course here before, but if
you're not it can be read as follows:

* The top row represents titles that the data has. Our three fields are "Part
  Name", "Part Number", and "Number in Stock".

* Each row after that contains the data for an item, and each one is separated
  by commas. For instance, the store has 12 levers and a lever has a part
  number of 1234.

One thing that's pretty obvious from looking at it

.. _sec-loading-data-python:

Opening the file in Python
==========================

TODO WRITE

