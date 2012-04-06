=========================================
FRBR-Redis Datastore Aristotle App Set-up
=========================================
Setting up the FRBR-Redis Datastore Aristotle App environment involves
a number of different components to run properly. This documentation
presumes that the App environment is being installed on `Ubuntu Server`_.
Other Linux distributions should be similar; the FRBR-Redis Datastore
has been under Microsoft Windows and Macintosh OSX but may require 
additional steps that are not covered in this documentation.

.. _`Ubuntu Server`: http://www.ubuntu.com/business/server/overview

Installing and Configuring nginx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Background
----------
While `Apache`_ is the most popular open-source web-server, it 
can be hard to configure properly. An alternative web-server used by 
such websites as `WordPress`_, `Hulu`_, and `Github`_. `nginx`_.

.. _`Apache`: http://httpd.apache.org/
.. _`Github`: https://github.com/
.. _`Hulu`: http://www.hulu.com/
.. _`nginx`: http://nginx.org/
.. _`WordPress`: http://www.wordpress.com/

Installing Redis
^^^^^^^^^^^^^^^^
Background
----------
`Redis`_ is an open-source, key-value datastore that is small and easy 
to deploy. Redis operates on in-memory dataset and can either 
periodically dump the data to disk or append the data to disk with each 
command to a log. Some large websites that use `Redis`_ include 
`craigslist`_, `Github`_, `Guardian UK Newspapers`_, `digg`_, `flickr`_,
and `stackoverflow`_ among `others`_.

.. _`craigslist`: http://www.craigslist.org
.. _`digg`: http://digg.com/
.. _`flickr`: http://www.flickr.com/
.. _`Github`: https://github.com/
.. _`Guardian UK Newspapers`: http://www.guardian.co.uk/
.. _`others`: http://redis.io/topics/whos-using-redis
.. _`Redis`: http://redis.io/
.. _`stackoverflow`: http://stackoverflow.com/

Installing virtualenv with pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Background
----------
.. _`virtualenv`: http://pypi.python.org/pypi/virtualenv

Installing uWSGI
^^^^^^^^^^^^^^^^
Background
----------
.. _`uWSGI`: http://projects.unbit.it/uwsgi/

Installing Django
^^^^^^^^^^^^^^^^^
Background
----------
.. _`Django`: https://www.djangoproject.com/

Installing FRBR-Redis-Datastore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Background
----------
.. _`FRBR-Redis-Datastore`: https://github.com/jermnelson/FRBR-Redis-Datastore

Installing supporting Python Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Background
----------
