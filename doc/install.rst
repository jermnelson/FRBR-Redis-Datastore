Installing FRBR Redis Datastore
===============================
Directions for installing `FRBR-Redis-Datastore` on an Ubuntu_ 11.10 
server. Directions for installing `FRBR-Redis-Datastore` on
Windows or Macintosh are similar but will require different installation
directions for some of the project's dependencies.

.. _Ubuntu: http://www.ubuntu.com


Install Redis
-------------
#. Use ``wget`` to download Redis tar file
   ``$ wget http://redis.googlecode.com/files/redis-2.4.6.tar.gz``
#. Untar the file
   ``$ tar xzf redis-2.4.6.tar.gz``
#. Run make
   ``$ make``

Install virtualenv
------------------
#. Install virtualenv. If you already have 
   `pip <http://pypi.python.org/pypi/pip>`_ installed, then run the command
   ``$ pip install virtualenv``. If you do not have 
   `pip <http://pypi.python.org/pypi/pip>`_, download the following
   file 
   `https://raw.github.com/pypa/virtualenv/master/virtualenv.py <https://raw.github.com/pypa/virtualenv/master/virtualenv.py>`_ 
#. To create your virtual environment use either ``$ virtualenv ENV`` or
   if you are using the virtualenv.py file, then ``$ python virtualenv.py ENV``.
   (ENV should be the name of your `FRBR-Redis-Datastore` virtual environment, say, **frbr-redis-env** or some easy to remember name)
#. Activate your new virtual environment with the following command: ``$ source ENV/bin/activate``, you should
   now see your prompt change to ``(ENV)$``.
   
Clone `FRBR-Redis-Datastore` from github
----------------------------------------
#. Clone `FRBR-Redis-Datastore` from github at
   ``(ENV)$ git clone git://github.com/jermnelson/FRBR-Redis-Datastore.git`` 
   You should now have a new directory named FRBR-Redis-Datastore. For 
   now, you need to manually change this directory to all lowercase so
   run the following command: ``(ENV)$ mv FRBR-Redis-Datastore frbr-redis-datastore``.
   This will be changed in future versions.
#. Change directories ``(ENV)$ cd frbr-redis-datastore`` and then run
   the following command, ``(ENV)$ pip install -r requirements.txt``. This
   will install most of the dependencies required by the`FRBR-Redis-Datastore`
   project.
 
   
