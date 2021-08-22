.. ChillBoss documentation master file, created by
   sphinx-quickstart on Wed Mar  3 09:41:58 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ChillBoss's documentation!
=====================================

|Downloads| |MonthlyDownloads| |WeeklyDownloads| |Hygiene|
|chillboss| |PyPI version fury.io|

Version: 0.4.0

ChillBoss keeps your mouse moving to keep your status alive 😎.

Homepage: https://naveenkumarreddy8.github.io/ChillBoss/

Installation
============

ChillBoss is published on PyPI: https://pypi.org/project/chillboss/

.. code:: shell

    pip install chillboss

.. figure:: https://media.giphy.com/media/aDoezJuCfRnEf4KErq/source.gif
   :alt: ChillBoss Installation

Note: On Linux you may need to install python3-tk python3-dev

.. code:: shell

    sudo apt-get install python3-tk python3-dev


Usage
=====

.. code:: shell

    chillboss [options]

Command line argument accepted:

-  -m, --movement: ``random`` and ``square`` movements are accepted. Default
   set to ``random``.
-  -l, --length: Accepted for ``square`` type of movement. Default set to
   ``None``.
-  -s, --sleeptime: Time to be taken till next movement. Default set to 30
   seconds.
-  -mt, --motiontime: Time consumption of pointer to move from present
   coordinates to the next coordinates. Default set to 0 seconds.
-  -v, --verbose: Flag argument when given as input, sets the log level to
   Debug, else Warning.

.. figure:: https://media.giphy.com/media/TrlvEhASiYMqNZ7Gy9/source.gif
   :alt: ChillBoss Usage

️

.. |Downloads| image:: https://static.pepy.tech/personalized-badge/chillboss?period=total&units=international_system&left_color=blue&right_color=green&left_text=Total%20Downloads
   :target: https://pepy.tech/project/chillboss
.. |MonthlyDownloads| image:: https://static.pepy.tech/personalized-badge/chillboss?period=month&units=international_system&left_color=blue&right_color=green&left_text=Downloads/Month
   :target: https://pepy.tech/project/chillboss
.. |WeeklyDownloads| image:: https://static.pepy.tech/personalized-badge/chillboss?period=week&units=international_system&left_color=blue&right_color=green&left_text=Downloads/Week
   :target: https://pepy.tech/project/chillboss
.. |Hygiene| image:: https://github.com/NaveenKumarReddy8/ChillBoss/actions/workflows/main.yml/badge.svg
   :target: https://github.com/NaveenKumarReddy8/ChillBoss/actions/workflows/main.yml
.. |chillboss| image:: https://snyk.io/advisor/python/chillboss/badge.svg
   :target: https://snyk.io/advisor/python/chillboss
.. |PyPI version fury.io| image:: https://badge.fury.io/py/chillboss.svg
   :target: https://pypi.python.org/pypi/chillboss/


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Made with love ❤️