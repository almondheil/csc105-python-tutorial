.. _chap-reading-csv-files-with-pandas:

=============================
Reading CSV Files with Pandas
=============================

.. _sec-what-are-csv-files:

Introduction and Motivation
===========================

In the previous chapter we were able to use Python's ``open`` command to
extract the text from a file and do things with it, but left off without being
able to read more complex data from a file. For instance, what if we care about
something more like a spreadsheet, with multiple values per row?

For that purpose, we'll turn to code that other people have written. It's
definitely possible to do all this work yourself (especially if you're more
familiar with Python's strings and how to break them up into chunks), but for
our purposes here we'll use the popular library Pandas which can do it (and as a
bonus, handles unexpected data or whitespace way better than we'll be able to).

First we'll look at what a CSV file is and how it's stored, and then we can jump
into using Pandas to manipulate them. 

What are CSV Files?
===================

A CSV file is one way to store a table in a plain text file, in a format that is
pretty easy for computers to parse and understand. Here's one example that shows
the inventory for a hypothetical supervillain supplies store.

.. literalinclude:: code/my_table.csv
   :language: text 

CSV stands for Comma Separated Values. Basically, each comma represents the
divider between two rows in a table. The commas in this file don't actually line
up, since the space between all the words has been compressed to make it more
computer-friendly. For your convenience, here's the table that this CSV file
encodes. 

See how the columns match up?

.. csv-table::
   :align: left
   :file: code/my_table.csv

.. _sec-using-pandas-to-read-a-csv:

Using Pandas to read a CSV
==========================

First, you'll want to make a CSV file of your own. You can copy the one from the
code box above, or make up your own. In all the code snippets I'm going to use
the name ``my_table.csv``, but **if your filename is different you will have to
adjust that.**

With your CSV file saved in the Replit workspace, create a new Python file and
name it something like ``dataframes.py``. In that file, enter this starter code. 

.. code-block:: python

  import pandas 

  def read_csv():
    data = pandas.read_csv("my_table.csv")
    print(data)

When we call ``pandas.read_csv``, it's opening the file for us automatically and
creating something out of it called a dataframe. This is essentially Pandas'
version of a table, with some different features. We won't be using all the
complicated features of it, just some of the simpler stuff.

When you save and run this code, you'll see a (relatively) pretty display of the
CSV you made before like this one.

.. code-block:: text

                          Name  Number in Stock     Price
  0             Big red button               12      3000
  1         Evil looking chair                1  12000000
  2            Large spiky hat               32        35
  3  Robot that kills everyone                0     45000
  4                Villain car                4     75000

As you can see, it successfully figured out what the different columns were.
Also, notice the numbers on the side. Those weren't part of our original CSV
file, but they represent the indices of the rows within the data frame.

.. _sec-selecting-certain-data-from-a-dataframe:

Selecting a Column from a Dataframe 
===================================

It was easy enough to print the whole data frame, but what if we want to work
with individual rows or columns? There are a bunch of options Pandas provides to
do this sort of stuff, but we're going to focus on the one that requires the
least specialized machinery: Selecting columns.

For instance, what if I wanted to see only which evil machines and objects I had
in stock, but I didn't care about their price or anything else? Then, I could
select that column like so (assuming pandas was imported at the top of the file):

.. code-block:: python

   def select_column():
    data = pandas.read_csv("my_table.csv")
    print(data["Name"])

.. note:: 

  If you're interested in doing more with dataframes, I recommend you start with
  the `documentation for the dataframe procedure loc
  <https://pandas.pydata.org/pandas-docs/stable/reference/pi/pandas.DataFrame.loc.html>`_.
  It can be really useful and it works on both rows and columns, but it's out of
  scope for this project and we won't need it to do a basic plot.

Similarly, I could loop over every item in one of those columns like so:

.. code-block:: python

   def select_column():
    data = pandas.read_csv("my_table.csv")
    for name in data["Name"]:
      print("The evil store has " + name + " in stock.")

If you run the updated version of the ``select_column()`` function, you should
see it print out one line with the data of each row in the CSV.

Using this same format, we could do something like sum up the number of items we
have in stock in total. I don't know how that could be useful here, but we can
sure do it!

.. code-block:: python

   def sum_stock():
        data = pandas.read_csv("my_table.csv")
        sum = 0
        for number in data["Number in Stock"]:
                # Add the int version of that string number to the total sum
                sum = sum + int(number)

        # Print out the int version of that sum (convert the other direction)
        print("The total sum of items was " + str(sum))

Tada!!

.. _sec-conclusion:

Conclusion
==========

Okay, that's everything that we're going to cover having to do with Pandas!
We've really only brushed the surface of what that library can do, and it's
great for data manipulation of all sorts. As I mentioned earlier, check out the
documentation if you want to learn more!

Next up, we're going to concern ourselves with actually plotting the data that
we've been reading so far.
