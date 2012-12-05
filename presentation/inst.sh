#!/bin/bash

mkdir -p .local/lib/python2.7/site-packages
easy_install --upgrade --prefix=~/.local tornado
easy_install --upgrade --prefix=~/.local pyzmq
easy_install --upgrade --prefix=~/.local ipython
easy_install --upgrade --prefix=~/.local scikit-learn
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
. ~/.bashrc
