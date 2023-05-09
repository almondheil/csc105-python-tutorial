.. _chap-basic-file-io:

==============
Basic File I/O
==============

.. _sec-basic-file-io-introduction-and-motivatioj:

Introduction and Motivation
===========================

In this chapter, we're going to cover how we can take input and put output into
files instead of just using input and print to do those things in the terminal.
This concept is also known as file I/O.

So, why would we ever want to do file I/O? It can be useful when we have a lot
of data (say, from the measuring device you use in lab) to enter into our
program and don't want to enter it every time, or when we want to run something
a bunch of times and not type the same thing every time.

On the side of writing to files specifically, it can be really nice to put the
results of your program into a file where you can read them later, instead of
printing them out and risking losing your work if you don't use it immediately.
Similarly, if you ever run a complex program you might want it to report errors
to a file where you can check them later and figure out why it broke.

.. _sec-reading-a-file:

Reading a File 
==============

To start off, make a new file in your Replit and name it something like
``plaintext-data.txt``. You can do this by pressing the button in the files
pane that looks like a page with a plus icon, then typing the filename. As
shown in the file extension, this file is meant to hold normal text with no
fancy formatting. Then, just enter some sort of data into the file, to make it
look like a list of things with one item on each line. I've made mine a list of
absurd emotions.

.. literalinclude:: code/plaintext_data.txt 

Once that's done, we're going to make a function that will print out each item
in the file. Make a new function called ``read_file()`` and give it the
following starting code.

.. literalinclude:: code/reading_text_0.py 
   :language: python 

There are a few things to unpack with this short function, especially on line 3.
There are two new pieces of syntax that this line alone introduces, so I'll
break them down below from the center of the statement outwards:

* At the center of the statement is ``open("plaintext_data.txt", "r")``. This
  snippet tells Python to open up the file by searching for its filename, and
  the ``"r"`` tells it to open the file for reading, which will stop us from
  accidentally modifying what's inside.

* The next layer out is the ``with ... as file:`` block that we're creating. I
  find it most helpful to think of this instruction running the command in the
  middle, and assigning its result to the variable name ``file``. We could also
  do this differently by writing ``file = open("plaintext_data.txt", "r")``, but
  the benefit of the method I'm using here is that Python will automatically
  close the file when we are done using it. 

.. note:: 
   If we never close the file (either manually or letting Python do it), there's
   a small chance that the file can become corrupted because some of the
   metadata will not get saved properly. This is much less common on modern
   computers than it was a few years ago, but it's still worth being safe about.

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
line starts right after it where we don't want it to.

To fix that, one possible solution is to only print out the part of the line
that doesn't contain the newline, or everything except the last character. To do
that, we just need to use Python's list indexing like so:

.. literalinclude:: code/reading_text_final.py 
   :language: python 
   :emphasize-lines: 5

Now, this will print everything out correctly, with exactly one entry per line:

.. code-block:: text

  The feeling of sturror is a feeling that really exists.
  The feeling of gleeb is a feeling that really exists.
  The feeling of ermity is a feeling that really exists.
  The feeling of frabjousness is a feeling that really exists.
  The feeling of flasure is a feeling that really exists.

.. _sec-writing-to-a-file:

Writing to a File 
=================

Next, let's practice opening a file so we can write data to it. Go ahead and
make a new function in your existing file, and call this one something like
``write_to_file()``. For now, feel free to copy down this code block below. 

.. literalinclude:: code/writing_text.py 
   :language: python 

So, what is this one actually doing? The first thing to notice is that we're
opening a file using a ``with ... as`` expression like we did before, but this
time we use the parameter ``"w"`` instead of ``"r"``. That means that Python
will open the file for writing, or create it if it does not exist. Be careful,
because it also clears the file if it already does exist! 

.. note:: 
   If that's not the behavior you want, you could use ``"a"`` to append to the
   end of an existing file, or ``"x"`` to create a file if it does not exist but
   fail if the file is already present. However, for our purposes here we want
   to overwrite old files. Just make sure not to accidentally save over your
   code!

The next thing to notice is the calls inside the function to ``outfile.write``.
This is quite similar to how we already use print statements, but instead of
printing into the terminal it essentially prints into the file named
``outfile``. Also, notice that there is a single ``\n`` character on the end of
each line. This isn't something that we need to do when printing, but it's
necessary when we write to a file to make sure the lines advance.

So, what if we want to do something slightly more complicated when we output to
our file? We've already managed to read from one file, so let's extend our
previous work in a new function called ``read_and_write()``.

.. literalinclude:: code/read_and_write.py 
   :language: python 

We've already interacted with all the individual parts of this function, but
here's a breakdown of what it does anyway.

* We open a file called ``infile`` using the inline method, which we haven't
  used before. It's very similar to the ``with ... as`` expression, but when
  we're done with the file we simply call ``infile.close()`` to close it
  properly. 

  * The main reason I did this was so that even after closing the file, the
    ``lines`` list would be in scope for the program. You could also nest two
    ``with ... as`` expressions inside each other, but I thought that would be
    less elegant for this case.

* Then, we open our output file (overwriting the previous contents), and print
  out each item in the list of lines. Notice that we put a ``\n`` at the end of
  each line, just as we needed to in the previous example.
