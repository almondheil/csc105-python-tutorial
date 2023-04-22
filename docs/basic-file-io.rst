.. _chap-basic-file-io:

==============
Basic File I/O
==============

.. _sec-introduction:

Introduction
============

In this chaoter, we're going to cover how we can take input and put output into
files instead of just using input and print to do those things in the terminal.
This concept is also known as file I/O.

To start off, we'll go over why we actually want to use file I/O. Then, we'll
go through a couple short examples: reading text from a file that's already
written and writing text into a file to change it. Finally, we'll cover why
this method can be a little frustrating to motivate our next steps with more
libraries written by other people.

.. _sec-fileio-motivation:

Motivation
==========

Have you ever felt like it was tedious to type in the same thing each time you
ran a function and asked for user input? It can make sense to ask for input when
it'll be a different result every time you run the file, but sometimes you'd
rather store your input somewhere else. 

That can help you especially if you need to run the code several times and need
the same input every time, or if there is so much input (like data from a
study) that you'd never want to type all of it in manually.

On the side of file output, it can be really nice to put the results of your
program into a file where you can read them later, instead of printing them out
and risking losing your work if you don't use it immediately. With those
reasons stated, let's jump into how to handle those things from Python!

.. _sec-reading-a-file:

Reading a File 
==============

To start off, make a new file in your Replit and name it something like
``plaintext-data.txt``. As shown in the file extension, this file is meant to hold
normal text with no fancy formatting. Then, just enter some sort of data into
the file, to make it look like a list of things with one item on each line. I've
made mine a list of fake emotions.

.. literalinclude:: code/plaintext_data.txt 

Once that's done, we're going to make a program that will print out a random one
of those items. Make a new Python file called ``basic_file_io.py`` or something
along those lines, and start off with the following outline for a function
called ``read_file()``:

.. literalinclude:: code/reading_text_0.py 
   :language: python 

There are a few things to unpack with this short function, especially on line 3.
There are two new pieces of syntax that this line alone introduces, so I'll
break them down below from the center of the statement outwards:

#. At the center of the statement is ``open("plaintext_data.txt", "r")``. This
   snippet tells Python to open up the file by searching for its filename, and
   the ``"r"`` tells it to open the file for reading, which will stop us from
   accidentally modifying what's inside.

#. The next layer out is the ``with ... as file:`` block that we're creating. I
   find it most helpful to think of this instruction running the command in the
   middle, and assigning its result to the variable name ``file``. We could
   also do this differently by entering ``file = open("plaintext_data.txt",
   "r")``, but the benefit of the method I'm using here is that Python will
   automatically close the file when we are done using it. If the file never
   gets closed, there's a (small but existent) chance that the file will become
   corrupted.

Then, inside the with block on line 7, we have the expression
``lines = file.readlines()``. As you can probably guess from the method name,
this is getting all the lines from the file and putting them into a list. Then,
we just use a simple ``for`` loop to print out all the lines one by one.

If you run the program at this point, you might notice that there is something
strange going on. Every time a line gets printed out, there is an extra newline between it and the next item.

You might already have a hunch on why this is happening, but for the
sake of this tutorial we're going to modify the program to print out some more
information on each line since that might make the issue clearer. Here are the
changes that I made to my copy of the program:

.. literalinclude:: code/reading_text_1.py 
   :language: python
   :emphasize-lines: 6

When I run this file, I get the following output:

.. code-block:: text

  The feeling of sturror
   is a feeling that really exists.
  The feeling of gleeb
   is a feeling that really exists.
  The feeling of ermity
   is a feeling that really exists.
  The feeling of frabjousness
   is a feeling that really exists.
  The feeling of flasure
   is a feeling that really exists.

Now, it might be more obvious why this is happening--there is still a newline
character in the ``line`` variable that we print out, and that means that a new
line starts right after it. So, how can we fix that?

Here's my suggestion for one way to not print out that newline. Since we know
that the newline is always at the end of the string we *want* to print, it's
not too difficult to take advantage of Python's list indexing to use all except
the last character in the string. Here's how that looked when I did it:

.. literalinclude:: code/reading_text_final.py 
   :language: python 
   :emphasize-lines: 5

Now when we run the code, it works the way we expect it to. Hurrah!

.. _sec-writing-to-a-file:

Writing to a File 
=================

Next, let's practice opening a file so we can write data to it. Go ahead and
make a new function in your existing file, and call this one something like
``write_to_file()``. Here's a start for what that might look like.

.. literalinclude:: code/writing_text_0.py 
   :language: python 


.. _sec-difficulties-with-this-method:

Difficulties with this Method
=============================

