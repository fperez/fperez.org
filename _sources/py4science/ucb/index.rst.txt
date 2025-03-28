.. _py4science_ucb_local:

===================================
 Python for science at UC Berkeley
===================================

.. Note::

   **January 2014:** please see the new `Berkeley Python portal
   <http://python.berkeley.edu>`_ for all new information regarding Py4Science
   on campus, which is now coordinated by the `DLab
   <http://dlab.berkeley.edu>`_.  The rest of this page is kept for reference
   purposes, with material and slides about old meetings.


Past meetings
=============

November 18 2009, `Bryan Catanzaro`_ (UC Berkeley EECS), *Copperhead: Data-Parallel Python* [`Slides <talks/20091118_copperhead_bcatanzaro.pdf>`_]
  *Abstract:* The need for productive programming languages which can avail
  themselves of parallel hardware has never been more acute.  The Copperhead
  project attempts to address this problem by defining a subset of Python which
  can be compiled and executed in a data-parallel fashion.  Copperhead
  procedures are expressed as standard, fully-legal Python procedures operating
  on Numpy datatypes, which are intercepted, specialized, and compiled to
  parallel C code at runtime, and then executed on a high-performance parallel
  platform.  Since the Copperhead runtime supports only a subset of Python, the
  runtime will revert to standard Python execution if specialization fails.
  The current Copperhead runtime targets Nvidia Graphics Processors, which are
  highly suited for data-parallel computation and provide high performance.  In
  this talk, I will be discussing the current state of Copperhead, as well as
  plans for future development.

.. _Bryan Catanzaro: http://www.catanzaro.name
   
November 2009, Guido van Rossum at our Py4Science seminar
  On November 4, we had a very interesting session with Guido van Rossum, the
  creator of the Python language.  See `this page
  <../2009_guido_ucb/index.html>`_ for details.

September 2009, PyDy
  Luke Peterson from UC Davis gave a very interesting talk on PyDy_, a project
  under the SymPy_ umbrella to symbolically describe mechanical systems and
  derive their equations of motion.  Many thanks to Jeff Teeters for his
  continued work of `videotaping the lectures
  <http://www.archive.org/details/ucb_py4science_2009_09_30_Luke_Peterson>`_.

September 2009, decorators
  Some `notes about decorators for controlling execution <decorators.html>`_.

.. include:: links.txt
