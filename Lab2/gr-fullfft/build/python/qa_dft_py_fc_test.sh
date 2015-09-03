#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/meetshah1995/Desktop/Third_Year/EE340/Lab2/gr-fullfft/python
export PATH=/home/meetshah1995/Desktop/Third_Year/EE340/Lab2/gr-fullfft/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/meetshah1995/Desktop/Third_Year/EE340/Lab2/gr-fullfft/build/swig:$PYTHONPATH
/usr/bin/python2 /home/meetshah1995/Desktop/Third_Year/EE340/Lab2/gr-fullfft/python/qa_dft_py_fc.py 
