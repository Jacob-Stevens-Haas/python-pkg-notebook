=========================
Jupyter Notebooks Example
=========================

An example of a python package sourcetree with Jupyter notebooks.  These
notebooks need to be:

1. tested with ``pytest`` (and therefore have an accompanying .py file).
2. kept equivalent to matching python scripts with ``jupytext``.
3. documented with ``nbsphinx``.

It's nice to have ``examples`` as a top-level directory, because it's where a
lot of people expect them.  Moreover, for notebooks to be tested, they need to
offload data generation to local modules ``example_data.py`` and ``mock_data.py``.
The former may generate a full time series of, say, the Lorenz attractor.  The
latter may just generate a small time series.

This helps verify that changes to the package do not break the notebooks.
One can test the notebooks quickly using 
``pytest -k test_notebook_script``, but open and run the notebooks with full data. 

Currently, only the ``pytest`` tool provides full regex directory configuration.
