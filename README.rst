.. image:: http://i.imgur.com/BIcvhtP.jpg
   :width: 100%
   :alt: grappa logo
   :align: center


|Build Status| |PyPI| |Coverage Status| |Documentation Status| |Stability| |Quality| |Versions|

About
-----

``grappa`` is a behavior-oriented, self-declarative, expressive and developer-friendly
lightweight assertion library for Python that aims to be easy to use, adopt and hack.

``grappa`` comes with two flavors: ``expect`` and ``should`` declarative assertion styles.
It also comes with a gentle, human-friendly and frictionless error reporting built-in.

To get started, take a look to the `documentation`_.

Status
------

``grappa`` is currently beta quality software and under active development and improvements.

API is not stable yet and prone to introduce breaking changes.

Why grappa?
-----------

``grappa`` aims to assist humans while doing a very recurrent and not very fun task in software development: testing things.

The core idea behind ``grappa`` comes from the fact that human time is considerably more expensive than machine time,
and therefore any machine assistance to optimize processes and close the gap is beneficial.

With ``grappa`` you can express almost in plain English what the test contract actually is, but in a way that's
fun and easy to write but also more easy and pleasant to read or maintain by other developers.


The Zen of grappa
-----------------

- Frictionless testing: introducing self-declarative behavior testing patterns can make testing more fun for test writers and more enjoyable for test readers.
- Expressivity is paramount: humans should easily understand what the code is doing.
- Human time is expensive: any modern software should assist people to identify and understand errors easily.
- Make error reporting great again: feedback in testing is key, let's make it more handy and less frustration as possible.
- Testing patterns consolidation: software expectations are limited to the boundaries of language data types and structures.
- Less hurt feelings: seeing errors is not a good thing, but it can be less frustrating if things are told you in a more gentle way.


Features
--------

-  Behavior-oriented expressive Pythonic fluent API.
-  Provides both ``expect`` and ``should`` assertion styles.
-  Full-featured built-in assertions.
-  Human-friendly and frustration-less error reporting.
-  Composable assertions chaining.
-  Extensible assertions based on third-party plugins.
-  Testing framework agnostic. Works with ``unittest``, ``nosetests``, ``pytest`` ...
-  Lightweight and (almost) dependency-free.
-  Works with Python 2.6+, 3+ and PyPy.


Installation
------------

Using ``pip`` package manager:

.. code-block:: bash

    pip install --upgrade grappa

Or install the latest sources from Github:

.. code-block:: bash

    pip install -e git+git://github.com/grappa-python/grappa.git#egg=grappa


.. _Python: http://python.org
.. _`documentation`: http://grappa.readthedocs.io

.. |Build Status| image:: https://travis-ci.org/grappa-python/grappa.svg?branch=master
   :target: https://travis-ci.org/grappa-python/grappa
.. |PyPI| image:: https://img.shields.io/pypi/v/grappa.svg?maxAge=2592000?style=flat-square
   :target: https://pypi.python.org/pypi/paco
.. |Coverage Status| image:: https://coveralls.io/repos/github/grappa-python/grappa/badge.svg?branch=master
   :target: https://coveralls.io/github/grappa-python/grappa?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/paco/badge/?version=latest
   :target: http://grappa.readthedocs.io/en/latest/?badge=latest
.. |Quality| image:: https://codeclimate.com/github/grappa-python/grappa/badges/gpa.svg
   :target: https://codeclimate.com/github/grappa-python/grappa
   :alt: Code Climate
.. |Stability| image:: https://img.shields.io/pypi/status/grappa.svg
   :target: https://pypi.python.org/pypi/grappa
   :alt: Stability
.. |Versions| image:: https://img.shields.io/pypi/pyversions/grappa.svg
   :target: https://pypi.python.org/pypi/grappa
   :alt: Python Versions