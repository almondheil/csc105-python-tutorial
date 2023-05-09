.. _chap-getting-started:

===============
Getting Started
===============

.. _sec-introduction:

Introduction
============

Welcome to my little tutorial on some fun Python stuff! In this webpage-y thing
before you, I'm going to cover how to do a handful of fun and/or interesting
things in Python. Specifically, here are the things I want to cover:

* Reading and writing files using Python's built in tools

* Using pandas_ to make our data processing easier

* Plotting data graphically using matplotlib_ 

I'm doing my best to aim this tutorial so that it will match up with where we
left off with Python and data representation, but in doing that I explain a
handful of things that you already might know for one reason or another.

Definitely feel free to skip sections as needed! I don't want to bore you if
I can avoid it.

.. _sec-starting-a-project:

Starting a Project
==================

For our purposes here, we're going to use Replit to run our project. It'll
handle dependencies for us, and is generally about a million times easier than
it would be to set up Python on your computer directly. With that said, here's
how to create a new Repl if you haven't done so already!

#. First, go to Replit_ and click the "Create Repl" button.

#. Choose the Python template, and give it whatever sort of title you want. 
   Maybe ``totally-amazing-python-tutorial``?

Because of the limitations of Replit, I'll have you writing all of these
functions in your ``main.py``. For now, just add two imports to the top of the file
so we don't have to deal with them more.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt

Here, we're using the ``as`` keyword in order to give the packages a shorter name
that we can refer to to avoid typing the entire, long name. That'll be helpful
later on, but for now it'll just sit there.

The first time you run your program once the imports are added, it'll take a
minute to install everything for you. Then you should be good to go!

Throughout the tutorial, I mention running your code but don't go into how
exactly that will work. I chose to do things pretty much exactly the way we did
in class, where you'll press the run button to load up the functions in
``main.py`` and then call the functions manually from the console.

With all that done, let's get started with basic file I/O!

.. _matplotlib: https://matplotlib.org/

.. _pandas: https://pandas.pydata.org/

.. _Replit: https://replit.com

