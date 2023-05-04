.. _chap-plotting-data-with-matplotlib:

=============================
Plotting Data with Matplotlib
=============================

.. _sec-introduction-and-motivation:

Introduction and Motivation
===========================

In the previous chapter we used the CSV utilities that the Pandas library
provides to read a CSV and select certain parts of its data, and we've finally
built up to the point of plotting that data and making it display nicely.


.. _sec-how-does-matplotlib-work:

How does Matplotlib Work?
=========================

The general workflow we're going to follow in this chapter is as
follows:

#. Load data from a CSV into a dataframe using Pandas

#. Do any sort of data manipulation we need

#. Tell Matplotlib to plot that data (it won't show anything yet) 

#. Change features of the graph while it is still loading

#. Show or export the final graph

.. _sec-plotting-different-charts:

Simple charts with Fake Data
============================

First, I want to do a couple charts on fake data to show the very basics of how
we can use Matplotlib. Just download :download:`simple_data.csv
<code/simple_data.csv>` (click that text) and upload it to your Replit using the
three dots menu in the corner of the file browser pane.

Before plotting, go ahead and take a look at what's inside that file by opening
it in Replit. As you can see it's pretty simple, it keeps track of different
decades and their ability to be the future. Why, you ask? I just wanted an
obvious and stupid trend to follow.

Now, let's throw together a python script that will plot this for us. Go ahead
and start a new python file in Replit, something along the lines of
``plotting.py``. Let's start off with this outline for a function:

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt

   def plot_fake_data():
      # Read in the CSV as usual
      data = pd.read_csv("simple_data.csv")

      # Tell Matplotlib to make a line plot and specify which data to use
      # "Year" will be the X axis
      plt.plot(data["Year"], data["General Futuristic-ness"])

      # Show the plot
      plt.show()

If you now run this code, you should get the following somewhat underwhelming graph.

.. image:: images/simple_fake_plot.png

However, this lacks something that is generally pretty important for graphs:
axis labels and a title. To add those, we can use the ``plt.xlabel``,
``plt.ylabel``, and ``plt.title`` commands as shown below. Note how we make sure
to put these commands before showing the plot, so that their changes actually
get applied.

By the way, I've removed the imports from this code block to keep it all
cleaner. You'll still need the imports in your own file, of course!

.. code-block:: python
   :emphasize-lines: 9-12

   def plot_fake_data():
      # Read in the CSV as usual
      data = pd.read_csv("simple_data.csv")

      # Tell Matplotlib to make a line plot and specify which data to use
      # "Year" will be the X axis
      plt.plot(data["Year"], data["General Futuristic-ness"])

      # Set axis labels and title
      plt.xlabel("Year");
      plt.ylabel("General Futuristic-ness")
      plt.title("The Future Comes for Us All")

      # Show the plot
      plt.show()

You can run the program again to see how this changes things, but I want to add
one more interesting feature to the graph first. How about a line that shows
the tipping point between the past and future? That is, where the
futuristic-ness of a decade is exactly equal to zero. For that, we can use the
command ``plt.axhline`` as follows.

.. code-block:: python
   :emphasize-lines: 15 

   def plot_fake_data():
      # Read in the CSV as usual
      data = pd.read_csv("simple_data.csv")

      # Tell Matplotlib to make a line plot and specify which data to use
      # "Year" will be the X axis
      plt.plot(data["Year"], data["General Futuristic-ness"])

      # Set axis labels and title
      plt.xlabel("Year");
      plt.ylabel("General Futuristic-ness")
      plt.title("The Future Comes for Us All")

      # Horizontal line at y = 0
      plt.axhline(0, color="red")

      # Show the plot
      plt.show()

Now, your plot will look like this! Still basic, but much easier to understand.

.. image:: images/simple_fake_plot_hline.png

Using Real Data
===============

I have one particular example of plotting real data that I want to walk through,
based on our sorting algorithms lab from earlier this semester. Once again, you
can download :download:`sorting_algorithms.csv <code/sorting_algorithms.csv>` by
clicking on that piece of text. Once it's uploaded to Replit, we can start out
looking at the data and figuring out how to plot it.

TODO NEED TO WRITE THIS WHOLE DEALIO WHEEE I HATE MYSELF FOR THIS SOMETIMES

More Possibilities with Matplotlib
===================================

Matplotlib is a truly huge library, and it can do a lot more than we've touched
on here. For some truly stunning examples, I recommend you check out all the
different `types of graphs Matplotlib can create
<https://matplotlib.org/stable/plot_types/index.html>`_. In particular, some of
my favorites from that page are the `contour plot
<https://matplotlib.org/stable/plot_types/arrays/contourf.html#sphx-glr-plot-types-arrays-contourf-py>`_
and the `3D surface plot
<https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html#sphx-glr-plot-types-3d-surface3d-simple-py>`_.

.. note::

   Most of the examples in Matplotlib's documentation use a library we haven't
   really talked about called NumPy. One of the biggest features NumPy brings to
   the table is another really powerful datastructure called arrays. I won't get
   into them here, but you might notice that some of the examples are able to
   apply functions or random values to entire arrays at once. That's the main
   reason they're so good for these examples.

.. _sec-conclusion:

Conclusion
==========

TODO write 
