What's this?
============

cpuspeed is a tiny configurable (currently only gtk2 based) applet to display the
Linux Kernel's cpu frequency setting for each core with properly background coloured
cells.

Installation
============

Install minimum GTK dependencies:

.. code-block:: bash
    apt-get install python-gtk2 python-gobject python-click

Then copy the script into a convenient binary folder in your path.


Usage
=====

Try the usage instructions for starters:

.. code-block:: bash
    cpuspeed --help

You can specify the count of cores you want to watch, as well as a basefrequency
and multipliers for the various colors. The refresh interval can be given in
milliseconds, don't pick this too high or low.
